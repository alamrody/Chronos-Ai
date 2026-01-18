import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. إعداد الصفحة
st.set_page_config(page_title="Chronos AI Studio", page_icon="⏳")

# 2. الربط مع المفتاح السري
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Missing API Key! Please add it to Streamlit Secrets.")
else:
    genai.configure(api_key=api_key)
    
    # محاولة تشغيل الموديل بأكثر من تسمية لضمان العمل
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        model = genai.GenerativeModel('gemini-pro-vision') # نسخة احتياطية

    st.title("⏳ CHRONOS AI")
    st.write("Professional Merchant Studio")
    
    # 3. رفع الصورة
    uploaded_file = st.file_uploader("Upload Product Photo", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Product Preview", use_container_width=True)
        
        if st.button("🚀 Analyze & Generate Listing"):
            with st.spinner("Chronos is thinking..."):
                try:
                    # البرومبت الاحترافي
                    prompt = "Analyze this product image. Provide a professional title, a detailed description in Arabic and English, and social media tags."
                    
                    # طلب النتيجة
                    response = model.generate_content([prompt, img])
                    
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Technical Error: {e}")
