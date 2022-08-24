import base64
import io
import os
from pathlib import Path

import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "image_select", url="http://localhost:3001"
    )
else:
    path = (Path(__file__).parent / "frontend" / "build").resolve()
    print(path)
    _component_func = components.declare_component("image_select", path=path)


@st.experimental_memo
def _encode_file(img):
    with open(img, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64, {encoded}"


@st.experimental_memo
def _encode_numpy(img):
    pil_img = Image.fromarray(img)
    buffer = io.BytesIO()
    pil_img.save(buffer, format="JPEG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/jpeg;base64, {encoded}"


def image_select(label: str, images: list, key: str = None):
    """Shows several images and returns the image selected by the user.

    Args:
        label (str): The label shown above the images.
        images (list): The images to show. Allowed image formats are paths to local
            files, URLs, PIL images, and numpy arrays.
        key (str, optional): The key of the component. Defaults to None.

    Returns:
        (any): The image selected by the user (same object and type as passed to
            `images`).
    """

    # TODO: Check if images exist and raise exception if not.

    # Encode local images/numpy arrays/PIL images to base64.
    encoded_images = []
    for img in images:
        if isinstance(img, (np.ndarray, Image.Image)):  # numpy array or PIL image
            encoded_images.append(_encode_numpy(np.asarray(img)))
        elif os.path.exists(img):  # local file
            encoded_images.append(_encode_file(img))
        else:  # url, use directly
            encoded_images.append(img)

    component_value = _component_func(
        label=label, images=encoded_images, key=key, default=0
    )
    return images[component_value]
