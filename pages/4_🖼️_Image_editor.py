import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

st.set_page_config(
    page_title="Image editor",
    page_icon=":frame_with_picture:",
    layout="wide",
)

st.title("Image editor")

st.write("This is an image editor built with Streamlit.")

st.write("Upload an image to get started.")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg','png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns( [0.5, 0.5] )
    with col1:
        st.markdown("<p style=\"text-align: center;\">Before</style>", unsafe_allow_html=True)
        st.image(image, use_column_width=True)

    with col2:
        st.markdown("<p style=\"text-align: center;\">After</style>", unsafe_allow_html=True)
        #in the sidebar we will have the options to edit the image, and some pre-made filters
        st.sidebar.header("Edit image")
        st.sidebar.subheader("Pre-Made filters")
        st.sidebar.write("Apply a pre-made filter to your image.")
        filter = st.sidebar.selectbox(
            label="Choose a filter",
            options=["None", "Grayscale", "Blur", "Pencil Sketch", "Edge Detection"],
        )

        if filter == "Grayscale":
            conv_image = np.array(image.convert("RGB"))
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_RGB2GRAY)
            conv_image = Image.fromarray(conv_image)
        elif filter == "Blur":
            conv_image = np.array(image.convert("RGB"))
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_RGB2BGR)
            conv_image = cv2.GaussianBlur(conv_image, (55,55), 0)
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_BGR2RGB)
            conv_image = Image.fromarray(conv_image)
        elif filter == "Pencil Sketch":
            converted_img = np.array(image.convert('RGB')) 
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            inv_gray = 255 - gray_scale
            slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
            blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
            conv_image = cv2.divide(gray_scale, 255 - blur_image, scale=256)
            conv_image = Image.fromarray(conv_image)
        elif filter == "Edge Detection":
            conv_image = np.array(image.convert("RGB"))
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_RGB2BGR)
            conv_image = cv2.Canny(conv_image, 100, 200)
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_BGR2RGB)
            conv_image = Image.fromarray(conv_image)
        else:
            conv_image = image
        
        #options to edit the image directly
        st.sidebar.subheader("Edit image")
        st.sidebar.write("Edit your image directly.")
        brightness = st.sidebar.slider("Brightness", 0.0, 3.0, 1.0)
        contrast = st.sidebar.slider("Contrast", 0.0, 3.0, 1.0)
        saturation = st.sidebar.slider("Saturation", 0.0, 3.0, 1.0)
        hue = st.sidebar.slider("Hue", 0.0, 3.0, 1.0)
        enhancer = ImageEnhance.Brightness(conv_image)
        conv_image = enhancer.enhance(brightness)
        enhancer = ImageEnhance.Contrast(conv_image)
        conv_image = enhancer.enhance(contrast)
        enhancer = ImageEnhance.Color(conv_image)
        conv_image = enhancer.enhance(saturation)
        enhancer = ImageEnhance.Sharpness(conv_image)
        conv_image = enhancer.enhance(hue)

        #radio button to extract the different RGB channels
        st.sidebar.subheader("Extract RGB channels")
        st.sidebar.write("Extract the different RGB channels of your image.")
        channel = st.sidebar.radio(
            label="Choose a channel",
            options=["None", "Red", "Green", "Blue"],
        )

        if channel == "Red":
            conv_image = np.array(conv_image.convert("RGB"))
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_RGB2BGR)
            conv_image = cv2.split(conv_image)[2]
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_BGR2RGB)
            conv_image = Image.fromarray(conv_image)
        elif channel == "Green":
            conv_image = np.array(conv_image.convert("RGB"))
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_RGB2BGR)
            conv_image = cv2.split(conv_image)[1]
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_BGR2RGB)
            conv_image = Image.fromarray(conv_image)
        elif channel == "Blue":
            conv_image = np.array(conv_image.convert("RGB"))
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_RGB2BGR)
            conv_image = cv2.split(conv_image)[0]
            conv_image = cv2.cvtColor(conv_image, cv2.COLOR_BGR2RGB)
            conv_image = Image.fromarray(conv_image)
        
        #show image
        st.image(conv_image, use_column_width=True)
    