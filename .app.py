import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

st.set_page_config(page_title="Chronos AI Studio", page_icon="⏳")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Missing API Key! Please add it to Streamlit Secrets.")
else:
    genai.configure(api_key=api_key)
    
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    except:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

    st.title("⏳ CHRONOS AI")
    st.write("Merchant Studio: From Photo to Profit")
    
    uploaded_file = st.file_uploader("Upload or Take a Photo", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Target Product", use_container_width=True)
        
        if st.button("🚀 Analyze & Generate Listing"):
            with st.spinner("Chronos is analyzing the image..."):
                try:
                    prompt = "Analyze this product image. Provide a catchy title, a professional description in both Arabic and English, and suggest 5 hashtags."
                    
                    response = model.generate_content([prompt, img])
                    
                    st.success("Success!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
