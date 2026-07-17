import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool", layout="centered")
st.title("🌍 Language Translation Tool")
st.write("Translate text between 100+ languages instantly")

# List of languages
LANGUAGES = {
    'English': 'en', 'Hindi': 'hi', 'Marathi': 'mr', 'Gujarati': 'gu',
    'Bengali': 'bn', 'Tamil': 'ta', 'Telugu': 'te', 'Kannada': 'kn',
    'French': 'fr', 'Spanish': 'es', 'German': 'de', 'Japanese': 'ja', 
    'Korean': 'ko', 'Arabic': 'ar', 'Chinese': 'zh-CN'
}

# 1. Input Text
text_input = st.text_area("Enter text to translate:", height=150, placeholder="Type here...")

col1, col2 = st.columns(2)
# 2. Source and Target Language
with col1:
    src_lang = st.selectbox("From:", list(LANGUAGES.keys()), index=0)
with col2:
    dest_lang = st.selectbox("To:", list(LANGUAGES.keys()), index=1)

# 3. Translate Button
if st.button("Translate 🚀", use_container_width=True, type="primary"):
    if text_input.strip() != "":
        with st.spinner("Translating..."):
            try:
                translated = GoogleTranslator(source=LANGUAGES[src_lang], target=LANGUAGES[dest_lang]).translate(text_input)
                
                st.success("Translated Text:")
                st.text_area("", translated, height=150)
            except Exception as e:
                st.error("Translation failed. Please check internet connection.")
    else:
        st.warning("⚠️ Please enter some text to translate")

st.caption("Powered by Google Translate API")