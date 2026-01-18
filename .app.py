import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Chronos AI Studio", page_icon="⏳")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Missing API Key! Please check your Streamlit Secrets.")
else:
    genai.configure(api_key=api_key)
    
    st.title("⏳ CHRONOS AI")
    st.write("Merchant Studio: From Photo to Profit")
    
    uploaded_file = st.file_uploader("Upload or Take a Photo", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Product Preview", use_container_width=True)
        
        if st.button("🚀 Analyze & Generate Listing"):
            with st.spinner("Searching for best AI model..."):
                # محاولة تجربة الموديلات بالترتيب حسب المتاح في حسابك
                working_model = None
                for model_name in ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro-vision']:
                    try:
                        temp_model = genai.GenerativeModel(model_name)
                        # فحص سريع للموديل
                        temp_model.generate_content("test")
                        working_model = temp_model
                        break
                    except:
                        continue
                
                if working_model:
                    try:
                        prompt = "Identify this product. Provide a catchy title, a detailed description in Arabic and English, and 5 hashtags."
                        response = working_model.generate_content([prompt, img])
                        st.success(f"Success! (Model: {working_model.model_name})")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"Analysis failed: {e}")
                else:
                    st.error("Your API Key is not allowing any Gemini model. Please create a NEW key at aistudio.google.com")
