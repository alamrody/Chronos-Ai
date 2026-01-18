import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. إعدادات الواجهة (بدون تعقيدات CSS)
st.set_page_config(page_title="Chronos AI Studio", page_icon="⏳", layout="centered")

# 2. الربط مع Gemini (تأكد من وضع مفتاحك هنا)
API_KEY = os.getenv("GEMINI_API_KEY") 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 3. تصميم رأس الصفحة
st.title("⏳ CHRONOS")
st.subheader("Merchant Studio: From Photo to Profit")
st.write("---")

# 4. رفع الصورة
uploaded_file = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Target Product", use_container_width=True)
    
    if st.button("🚀 Analyze & Generate Listing"):
        with st.spinner("Chronos is working its magic..."):
            try:
                # طلب التحليل من الذكاء الاصطناعي
                prompt = """
                Act as an expert e-commerce specialist. Analyze this image and provide:
                1. Professional Title (EN & AR).
                2. Persuasive Product Description (EN & AR).
                3. 5 Bullet Points (Benefits).
                4. Social Media Captions (TikTok & Instagram) with Hashtags.
                5. A JSON structure of this data.
                """
                response = model.generate_content([prompt, image])
                
                # عرض النتائج
                st.success("Analysis Complete!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error: {e}")

# 5. تذييل الصفحة
st.write("---")
st.caption("Powered by Chronos Engine | Gemini 1.5 Flash")
