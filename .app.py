import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Chronos AI Studio", page_icon="⏳")

# جلب المفتاح
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Missing API Key!")
else:
    genai.configure(api_key=api_key)
    
    st.title("⏳ CHRONOS AI")
    st.write("Merchant Studio: From Photo to Profit")
    
    uploaded_file = st.file_uploader("Upload or Take a Photo", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Target Product", use_container_width=True)
        
        if st.button("🚀 Analyze & Generate Listing"):
            with st.spinner("Processing..."):
                try:
                    # استخدام اسم الموديل بدون بادئة models/ كحل أخير
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = "Describe this product professionally in Arabic and English for a merchant listing."
                    response = model.generate_content([prompt, img])
                    st.success("Done!")
                    st.markdown(response.text)
                except Exception as e:
                    # إذا فشل، جرب الموديل القديم المستقر جداً
                    try:
                        model = genai.GenerativeModel('gemini-pro-vision')
                        response = model.generate_content([prompt, img])
                        st.markdown(response.text)
                    except:
                        st.error(f"Please check your API Key permissions. Error: {e}")
