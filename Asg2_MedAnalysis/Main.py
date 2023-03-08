import streamlit as st
from PIL import Image


header = st.container()
dataset = st.container()
features = st.container()
model_Training = st.container()

with header:
    st.title('Medical image analysis for breast and blood')
    st.text('In this project with are going to perform medical image analysis for breast and blood')

with dataset:
    st.header('Medical image dataset for breast and blood')


with features:
    st.header('Upload here')

    uploaded_file = st.file_uploader("Upload an image to analyze", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded image')


with model_Training:
    st.header('Time to train the model')