import streamlit as st
import tensorflow as tf
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="Breast and Blood Analysis", page_icon=":microscope:")

#loading the model
model_1 = tf.keras.models.load_model('Resnet50_model_100_bloodMNIST_jpg100x100.h5')
model_2 = tf.keras.models.load_model('Blood_MNIST_CNN_own_model_best.h5')
model_3 = tf.keras.models.load_model('Blood_npz_without_aug.h5')
model_4 = tf.keras.models.load_model('vgg16_model_450_breastMNIST_jpg224x224.h5')
model_5 = tf.keras.models.load_model('Breast_MNIST_CNN_own_model_with_data_aug.h5')
model_6 = tf.keras.models.load_model('Breast_MNIST_CNN_own_model_no_data_aug.h5')



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
st.markdown("<h1 style='text-align: center;'>Breast and Blood Analysis</h1>", unsafe_allow_html=True)

st.subheader("Upload Image")

model_selection = st.selectbox("Select a model",("model 1", "model 2", "model 3", "model 4", "model 5", "model 6"))

image_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
if image_file is not None:
    st.image(image_file, caption="Uploaded image", use_column_width=True)
    
    img = Image.open(image_file)
    if model_selection == "model 1":
        img = img.resize((100, 100))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)
    elif model_selection == "model 2":
        img = img.resize((28, 28))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)
    elif model_selection == "model 3":
        img = img.resize((28, 28))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)
    elif model_selection == "model 4":
        img = img.resize((224, 224))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)
    elif model_selection == "model 5":
        img = img.convert('L')
        img = img.resize((28, 28))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)
    elif model_selection == "model 6":
        img = img.convert('L')
        img = img.resize((28, 28))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)
    

    if st.button("Predict"):
        if model_selection == "model 1":
            predictions = model_1.predict(img)
        elif model_selection == "model 2":
            predictions = model_2.predict(img)
        elif model_selection == "model 3":
            predictions = model_3.predict(img)
        elif model_selection == "model 4":
            predictions = model_4.predict(img)
        elif model_selection == "model 5":
            predictions = model_5.predict(img)
        elif model_selection == "model 6":
            predictions = model_6.predict(img)
        st.write('Predictions:')
        st.write(predictions)

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