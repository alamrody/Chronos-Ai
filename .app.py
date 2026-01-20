import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Chronos AI: Future Edition", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; }
    .stHeader { color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# المفتاح الخاص بك تم دمجه هنا
API_KEY = "AIzaSyBB6El9QdiDxXSHvgyJSXUBbZg9bDwJ4hQ"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("⚡ CHRONOS: The Future of Commerce")
st.write("Professional Merchant Analysis | From Photo to Profit")

col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("📸 Scan Your Product (Live or Gallery)", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Product Ready for Analysis", use_container_width=True)

with col2:
    if uploaded_file and st.button("🔥 Generate Market Strategy"):
        with st.spinner("AI is analyzing pixels, brand, and market value..."):
            try:
                prompt = """
                You are a professional e-commerce strategist. Analyze this product image and provide:
                1. PRODUCT IDENTITY: Exactly what is this? (Brand and Model).
                2. MAGIC TITLE: A catchy, SEO-friendly title in Arabic and English.
                3. SALES DESCRIPTION: A persuasive description focusing on features and benefits (Arabic and English).
                4. PRICING STRATEGY: Estimated market price in USD and why.
                5. SEO & VIRAL TAGS: 10 viral hashtags for Instagram and Facebook.
                6. TARGET AUDIENCE: Who is the ideal buyer for this?
                Format the output beautifully with bold headers and emojis.
                """
                response = model.generate_content([prompt, img])
                st.success("Analysis Complete!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Powered by Chronos Engine | Developed for 2026 Merchant Standards")
