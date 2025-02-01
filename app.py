import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load the model
model = load_model('cnn_model.h5')

# Function to process the uploaded image
def process_image(img):
    img = img.convert("RGB")  # Convert to RGB
    img = img.resize((64, 64))  # Resize to match model input
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Expand dimensions for batch processing
    return img

# Streamlit App
st.set_page_config(page_title="Pneumonia Detector", page_icon="🩺", layout="centered")

# Apply custom styling
st.markdown(
    """
    <style>
        .main {background-color: #e3f2fd;}  /* Light blue background */
        h1 {color: #008080; text-align: center;}  /* Teal color title */
        .stButton button {background-color: #008080; color: white; font-size: 18px;} /* Stylish button */
        .result-box {padding: 10px; border-radius: 10px; font-size: 20px; text-align: center; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🩺 Pneumonia Detection System")
st.write("Upload a chest X-ray image to check if it indicates Pneumonia or is Normal.")

# File uploader
file = st.file_uploader("📷 Upload an Image", type=["jpg", "jpeg", "png"])

if file is not None:
    # Display uploaded image
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("🔍 Predict"):
        with st.spinner("Analyzing... ⏳"):
            image = process_image(img)
            predictions = model.predict(image)
            predicted_class = np.argmax(predictions)

            # Class names
            class_names = ["NORMAL", "PNEUMONIA"]
            result_text = class_names[predicted_class]

            # Dynamic coloring for results
            color = "green" if predicted_class == 0 else "red"

            # Display result
            st.markdown(
                f'<div class="result-box" style="background-color: {color}; color: white;">{result_text}</div>',
                unsafe_allow_html=True,
            )
