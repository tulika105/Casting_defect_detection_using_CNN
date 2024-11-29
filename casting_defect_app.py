import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('cast_defect_model.h5')  # Ensure this is the correct path to your trained model

# Image preprocessing function
def preprocess_image(image):
    """Preprocess the uploaded image to match the model's input format."""
    image = image.resize((64, 64))  # Resize image to match the model's expected input size
    img_array = img_to_array(image) / 255.0  # Normalize pixel values to [0, 1]
    img_array = img_array[np.newaxis, ...]  # Add batch dimension
    return img_array

# Streamlit interface
st.title('Casting defect detection')
st.markdown("Upload any image")

# Upload image section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # Preprocess the image
    image = load_img(uploaded_file)
    img_array = preprocess_image(image)

    # Make predictions
    y_pred_prob = model.predict(img_array)
    y_pred = (y_pred_prob > 0.5).astype(int)

    # Show the prediction result
    predicted_class = 'def_front' if y_pred == 0 else 'ok_front'
    st.write(f"Predicted Class: {predicted_class}")
    
   
