import streamlit as st
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image

# Creating the title and instructions
st.header("Jewelry Caption Generator")
st.write("Hi! Im your personal jewelry caption generator: Simply upload an image and I will describe it!")

# Uploading Files
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# If users upload an image
if uploaded_file is not None:
    
    # Opening the image
    image = Image.open(uploaded_file)
    st.image(image)
    
    st.write("Analyzing image...")
    
    # Loading the model
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = AutoModelForImageTextToText.from_pretrained("Salesforce/blip-image-captioning-large")
    
    # Processing the image and generating captions
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    # Writing the captions
    st.write(f"Description: {caption}")
