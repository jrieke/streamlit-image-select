import io
import os

import numpy as np
import requests
import streamlit as st
from PIL import Image

from streamlit_image_select import image_select


def add_sunglasses(img, position):
    sunglasses = Image.open("images/red_sunglasses.png")
    # sunglasses.thumbnail((120, 120))
    # sunglasses.thumbnail((150, 150))
    if isinstance(img, np.ndarray):
        pil_img = Image.fromarray(img)
    elif isinstance(img, Image.Image):
        pil_img = img
    elif os.path.exists(img):
        pil_img = Image.open(img)
    else:
        response = requests.get(img)
        pil_img = Image.open(io.BytesIO(response.content))

    pil_img = pil_img.copy()
    pil_img.paste(sunglasses, position, sunglasses)
    return pil_img


st.set_page_config("Demo for streamlit-image-select", "🖼️")


st.write(
    f'<span style="font-size: 78px; line-height: 1">🖼️</span>',
    unsafe_allow_html=True,
)
"""
# Demo for [streamlit-image-select](https://github.com/jrieke/streamlit-image-select)
## Step 1: Create the component
You can pass in different image formats: local files, URLs, PIL images, and numpy 
arrays. Captions are optional!
"""

with st.expander("API reference"):
    st.help(image_select)

with st.echo():
    from streamlit_image_select import image_select

    img = image_select(
        label="Select a cat",
        images=[
            "images/cat1.jpeg",
            "https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg",
            Image.open("images/cat3.jpeg"),
            np.array(Image.open("images/cat4.jpeg")),
        ],
        captions=["A cat", "Another cat", "Oh look, a cat!", "Guess what, a cat..."],
    )

# st.file_uploader("Or upload your own cat!", type=["jpg", "jpeg", "png"])
# "https://bagongkia.github.io/react-image-picker/6c800cccebf18c24f51d5fd411818ac8.jpg",
# "https://bagongkia.github.io/react-image-picker/0e1abaf656c3367fc89f628f0d52ad11.jpg",
# "https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg",

if isinstance(img, np.ndarray):
    position = (55, 15)
elif isinstance(img, Image.Image):
    position = (30, 90)
elif img == "images/cat1.jpeg":
    position = (65, 70)
elif (
    img
    == "https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg"
):
    position = (15, 70)
else:
    position = (100, 100)

# if isinstance(img, np.ndarray):
#     position = (60, -15)
# elif isinstance(img, Image.Image):
#     position = (40, 60)
# elif img == "images/cat1.jpeg":
#     position = (65, 35)
# elif img == "https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg":
#     position = (20, 40)
# else:
#     position = (100, 100)

"""
## Step 2: Use the return value
It's just the same value you passed into the list of images above. Note that you can 
pipe it directly into `st.image` (or add some cool 😎).
"""
with st.echo():
    st.write(img)
    st.image(add_sunglasses(img, position))
