import streamlit as st
import cv2
import numpy as np
from PIL import Image

def main():
    st.title("Grayscale Image Converter")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        
        st.image(image, caption='Original Image', use_column_width=True)
        st.image(grayscale_image, caption='Grayscale Image', use_column_width=True)

if __name__ == "__main__":
    main()
