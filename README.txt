🎧 PolyLingua by Aryan

--> A powerful, user-friendly tool to generate transcripts from YouTube videos, uploaded audio files, or live microphone input — and translate them into your chosen language in just one click.

---

🚀 About the Project

PolyLingua by Aryan is a Streamlit-based web app built to simplify the process of audio transcription and translation. It combines the power of OpenAI's Whisper model with modern translation tools to generate highly accurate transcripts in multiple languages. Whether you're a student, journalist, content creator, or language enthusiast — PolyLingua is your all-in-one transcription and translation assistant.

---

🧠 Features

✅ Transcribe from:
- 🎧 Uploaded audio files (`.mp3`, `.wav`)
- 📺 YouTube video URLs
- 🎙️ Live microphone recording

✅ Translate the transcription into:
- English, Hindi, Gujarati, French, Spanish, German, Japanese, Chinese, Arabic, Punjabi, and more!

✅ Downloadable PDF of:
- The original transcript
- The translated version

✅ Clean UI built with Streamlit

---

🛠️ Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/) – for UI
- [OpenAI Whisper](https://github.com/openai/whisper) – for transcription
- `yt-dlp` – for downloading YouTube audio
- `sounddevice` & `scipy` – for microphone recording
- `deep-translator` – for translation
- `reportlab` – for PDF generation

---

📁 Folder Structure
PolyLingua-By-Aryan/
│
├── app.py # Main Streamlit app
├── transcribe.py # Transcription and translation logic
├── utils.py # Helper utilities: file handling, PDF generation
├── requirements.txt # All required packages
├── /venv # Virtual environment (not tracked in git)
└── /output # Generated transcript files

---

🔧 Installation

1. Clone the Repository
git clone https://github.com/armrlm2005/PolyLingua-By-Aryan.git
cd PolyLingua-By-Aryan

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

If requirements.txt is not present, install manually:
pip install streamlit openai-whisper yt-dlp sounddevice scipy deep-translator reportlab

4.Run the App
streamlit run app.py

---

📦 Example Use Cases
   🎓 Transcribe lecture audio and translate into your native language

   🧳 Travel vloggers: convert your voiceovers into different languages

   👩‍🏫 Teachers: record and share translated lessons

   📰 Journalists: turn interviews into clean transcripts and reports

---

🌍 Supported Languages (for translation) 

English (en)

Hindi (hi)

Spanish (es)

French (fr)

German (de)

Chinese (zh)

Japanese (ja)

Russian (ru)

Arabic (ar)

Gujarati (gu)

Punjabi (pa)






