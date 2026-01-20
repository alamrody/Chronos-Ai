import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة وتغيير الاسم
st.set_page_config(page_title="Chronos AI", page_icon="⏳", layout="wide")

# تصميم واجهة بأسلوب Neon و Dark Mode
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #00FFC8; /* لون نيون مائل للتركواز */
    }
    h1 {
        color: #FF00FF; /* لون نيون زهري */
        text-shadow: 0 0 10px #FF00FF, 0 0 20px #FF00FF;
        text-align: center;
    }
    .stwrite, p {
        color: #00FFC8;
        text-shadow: 0 0 5px #00FFC8;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF00FF, #00FFC8);
        color: white;
        border: none;
        border-radius: 15px;
        height: 3.5em;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
        box-shadow: 0 0 15px #FF00FF;
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px #00FFC8;
        transform: scale(1.02);
    }
    .stFileUploader {
        border: 2px dashed #00FFC8;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# الـ API Key الجديد مدمج هنا
API_KEY = "AIzaSyAEdd4IOsB_i7Dd6E-lOaCqHykKvD5BkHw"

# إعداد الموديل
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("⏳ CHRONOS AI")
st.markdown("<p style='text-align: center; font-size: 1.2em;'>THE FUTURE OF NEON COMMERCE</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📸 Scan Product")
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Detected by Chronos", use_container_width=True)

with col2:
    st.markdown("### ⚡ AI Intelligence")
    if uploaded_file and st.button("🚀 UNLEASH NEON ANALYSIS"):
        with st.spinner("Chronos is penetrating the market data..."):
            try:
                prompt = """
                You are a premium e-commerce AI. Analyze this image:
                1. What is this? (Brand & Model).
                2. Professional Title in Arabic & English.
                3. High-converting sales description in Arabic & English.
                4. Estimated Market Price in USD.
                5. 10 Viral hashtags.
                Format the response clearly.
                """
                response = model.generate_content([prompt, img])
                st.success("Analysis Ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.markdown("<p style='text-align: center; color: #555;'>Chronos Engine v2.0 | Neon Edition 2026</p>", unsafe_allow_html=True)
