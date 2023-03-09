import streamlit as st
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="Breast and Blood Analysis", page_icon=":microscope:")

# Define color scheme
COLOR_SCHEME = {
    "primary": "#0087c9",
    "secondary": "#1f2d3d",
    "text": "#444444",
    "background": "#f9f9f9",
}

# Set custom CSS
CUSTOM_CSS = f"""
    <style>
        body {{
            color: {COLOR_SCHEME['text']};
            background-color: {COLOR_SCHEME['background']};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {COLOR_SCHEME['primary']};
        }}
        .streamlit-expanderHeader {{
            color: {COLOR_SCHEME['primary']};
        }}
        .streamlit-expanderContent {{
            background-color: {COLOR_SCHEME['background']};
        }}
        .streamlit-widget stDropdown {{
            background-color: {COLOR_SCHEME['secondary']};
            color: {COLOR_SCHEME['text']};
        }}
        .css-1aumxhk {{
            color: {COLOR_SCHEME['primary']} !important;
        }}
        .css-ewgfru {{
            color: {COLOR_SCHEME['primary']} !important;
        }}
        .css-1mlaifk {{
            color: {COLOR_SCHEME['primary']} !important;
        }}
    </style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Define layout
st.title("Breast and Blood Analysis")
st.subheader("Upload Image")
image_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
if image_file is not None:
    st.image(image_file, caption="Uploaded image", use_column_width=True)

st.sidebar.title("Navigation")
sidebar_options = ["Home", "Analysis", "About"]
selected_sidebar = st.sidebar.radio("", sidebar_options)

# Display selected page
if selected_sidebar == "Home":
    st.write("This is the home page")
elif selected_sidebar == "Analysis":
    st.write("This is the analysis page")
elif selected_sidebar == "About":
    st.write("This is the about page") 