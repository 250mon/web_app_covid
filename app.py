# Core pkgs
import streamlit as st
st.set_page_config(
        page_title="Covid19 Detection Tool",
        page_icon="covid19.jpeg",
        layout='centered',
        initial_sidebar_state='auto'
)

import os
import time

# Viz pkgs
import cv2
from PIL import Image, ImageEnhance
import numpy as np

# AI pkgs
import tensorflow as tf


def main():
    """Simple Tool for Covid-19 Detection from Chest X-Ray"""
    html_templ = """
    <div style="background-color:blue;padding:10px;">
    <h1 style="color:yellow">Covid-19 Detection Tool</h1>
    </div>
    """

    st.markdown(html_templ, unsafe_allow_html=True)
    st.write("A simple proposal for Covid-19 Diagnosis powered by Deep Learning and Streamlit")

    st.sidebar.image("covid19.jpeg", width=300)

    image_file = st.sidebar.file_uploader(
            "Upload an X-Ray Image (jpg, png or jpeg)",
            type=['jpg', 'png', 'jpeg']
    )
    
    if image_file is not None:
        our_image = Image.open(image_file)

        if st.sidebar.button("Image Preview"):
            st.sidebar.image(our_image, width=300)

        activities = ["Image Enhancement", "Diagnosis", "Disclaimer and Info"]
        choice = st.sidebar.selectbox("Select Activity", activities)

        if choice == 'Image Enhancement':
            st.subheader("Image Enhancement")
            enhance_type = st.sidebar.radio(
                    "Enhance Type",
                    ["Original", "Contrast", "Brightness"]
            )
            
            if enhance_type == "Contrast":
                c_rate = st.slider("Contrast", 0.5, 5.0)
                enhancer = ImageEnhance.Contrast(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output, width=600, use_column_width=True)

            elif enhance_type == "Brightness":
                c_rate = st.slider("Brightness", 0.5, 5.0)
                enhancer = ImageEnhance.Brightness(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output, width=600, use_column_width=True)

            else:
                st.text("Original Image")
                st.image(our_image, width=600, use_column_width=True)


        elif choice == "Diagnosis":
            if st.sidebar.button("Diagnosis"):
                new_img = np.array(our_image.convert('RGB'))
                new_img = cv2.cvtColor(new_img, 1) # 0 is original, 1 is grayscale
                gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)



        else:
            st.subheader("Disclaimer and Info")


if __name__ == '__main__':
    main()


