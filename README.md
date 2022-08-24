# streamlit-image-select 🖼️

[![Badge](https://img.shields.io/badge/add%20one-badge-blue)](https://shields.io/)

**An image select component for Streamlit.**

This custom component works just like `st.selectbox` but with images. It's a great option
if you want to let the user select an example image, e.g. for a computer vision app!

---

<h3 align="center">
  🏃 <a href="https://image-select.streamlitapp.com/">Try out the demo app</a> 🏃
</h3>

---
<!--
<p align="center">
    <a href="https://image-select.streamlitapp.com/"><img src="demo.gif" width=600></a>
</p>
-->


## Installation

```bash
pip install streamlit-image-select
```

## Usage

```python
from streamlit_image_select import image_select
img = image_select("Label", ["image1.png", "image2.png", "image3.png"])
st.write(img)
```

See [the demo app](https://image-select.streamlitapp.com/) for a detailed guide!


## Development

Note: you only need to run these steps if you want to change this component or 
contribute to its development!

### Setup

First, clone the repository:

```bash
git clone https://github.com/jrieke/streamlit-image-select.git
cd streamlit-image-select
```

Install the Python dependencies:

```bash
poetry install --dev
```

And install the frontend dependencies:

```bash
cd streamlit_image_select/frontend
npm install
```

### Making changes

To make changes, first go to `streamlit_image_select/__init__.py` and make sure the 
variable `_RELEASE` is set to `False`. This will make the component use the local 
version of the frontend code, and not the built project. 

Then, start one terminal and run:

```bash
cd streamlit_image_select/frontend
npm start
```

This starts the frontend code on port 3001.

Open another terminal and run:

```bash
poetry shell
streamlit run demo.py
```

This starts the demo app. Now you can make changes to the Python or Javascript code in 
`streamlit_image_select` and the demo app should update automatically!


### Publishing on PyPI

Switch the variable `_RELEASE` in `streamlit_image_select/__init__.py` to `True`. 
Increment the version number in `pyproject.toml`. 

Build the frontend code with:

```bash
cd streamlit_image_select/frontend
npm run build
```

After this has finished, build and upload the package to PyPI:

```bash
cd ..
poetry build
poetry publish
```
