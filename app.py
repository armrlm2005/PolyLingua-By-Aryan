import streamlit as st
from transcribe import transcribe_audio, translate_text
from utils import (
    save_uploaded_file,
    download_youtube_audio,
    start_recording,
    stop_recording,
    create_transcript_txt
)
import os

st.set_page_config(page_title="Transcript Generator", layout="wide")
st.markdown("""
<style>
body {
    background-color: #9BC09C;
    font-family: 'Segoe UI', sans-serif;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    padding: 0.5rem 1.5rem;
    font-size: 16px;
    border-radius: 8px;
    border: none;
    margin-top: 1rem;
}
.stSelectbox, .stTextInput, .stFileUploader {
    padding: 0.5rem;
    font-size: 16px;
}
.stRadio > div {
    font-size: 16px;
}
.stMarkdown h1 {
    color: #333333;
    font-weight: 700;
}
.stMarkdown h2 {
    color: #4CAF50;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.title("🎧 PolyLingua By Aryan 🎧")
st.markdown("##### Generate Transcripts from any YouTube Video, Your Own Audio or Record Live Using Microphone — One Click Only!")
st.markdown("---")

lang_map = {
    "English": "en", "Hindi": "hi", "Spanish": "es", "French": "fr",
    "German": "de", "Chinese": "zh", "Japanese": "ja", "Russian": "ru", "Arabic": "ar", 
    "Gujarati": "gu", "Punjabi": "pa"
}

target_lang_name = st.selectbox("🌍 Translate transcription to:", list(lang_map.keys()))
target_lang = lang_map[target_lang_name]

input_type = st.radio("📥 Select Input Type:", ("Audio File", "YouTube URL", "Microphone"))

if "result" not in st.session_state:
    st.session_state.result = None
if "txt_path" not in st.session_state:
    st.session_state.txt_path = None
if "translated_txt_path" not in st.session_state:
    st.session_state.translated_txt_path = None

if input_type == "Audio File":
    uploaded_file = st.file_uploader("🎵 Upload an audio file", type=["mp3", "wav"])
    if uploaded_file:
        path = save_uploaded_file(uploaded_file)
        st.session_state.result = transcribe_audio(path)

elif input_type == "YouTube URL":
    url = st.text_input("🔗 Enter a YouTube URL")
    if st.button("🎬 Transcribe YouTube Video", key="yt_button"):
        try:
            path = download_youtube_audio(url)
            st.session_state.result = transcribe_audio(path)
        except Exception as e:
            st.error(f"Error processing YouTube video: {e}")
            st.session_state.result = None

elif input_type == "Microphone":
    st.markdown("🎙️ Use the buttons below to record manually.")
    col1, col2 = st.columns(2)
    if col1.button("▶️ Start Recording"):
        start_recording()
    if col2.button("⏹️ Stop Recording and Transcribe"):
        path = stop_recording()
        st.session_state.result = transcribe_audio(path)

if st.session_state.result and "text" in st.session_state.result:
    original_text = st.session_state.result["text"]

    st.markdown("## 📝 Original Transcription")
    st.text_area("Original", original_text, height=200)

    translated = translate_text(original_text, target_lang)
    st.markdown(f"## 🌐 Translated to {target_lang_name}")
    st.text_area("Translated", translated, height=200)

    if not st.session_state.txt_path and original_text.strip():
        st.session_state.txt_path = create_transcript_txt(
            original_text,
            filename="original_transcript.txt"
        )

    if not st.session_state.translated_txt_path and translated.strip():
        st.session_state.translated_txt_path = create_transcript_txt(
            translated,
            filename="translated_transcript.txt"
        )

    st.success("✅ TXT transcripts generated!")

    col1, col2 = st.columns(2)

    with col1:
        with open(st.session_state.txt_path, "r", encoding="utf-8") as f:
            st.download_button(
                "📄 Download Original Transcript (.txt)",
                data=f,
                file_name="original_transcript.txt",
                mime="text/plain"
            )

    with col2:
        with open(st.session_state.translated_txt_path, "r", encoding="utf-8") as f:
            st.download_button(
                f"🌐 Download Translated Transcript ({target_lang_name}) (.txt)",
                data=f,
                file_name="translated_transcript.txt",
                mime="text/plain"
            )

else:
    if (
        (input_type == "Audio File" and uploaded_file)
        or (input_type == "YouTube URL" and url)
        or (input_type == "Microphone")
    ):
        if not (st.session_state.result and "text" in st.session_state.result):
            st.error("Failed to generate transcript. Please check your input and try again.")
