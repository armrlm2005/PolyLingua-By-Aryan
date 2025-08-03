# PolyLingua by Aryan 🎧🌍

PolyLingua is a powerful, user-friendly Streamlit-based application that enables fast and accurate transcription and translation of audio from YouTube URLs, uploaded audio files, or live microphone input using OpenAI's Whisper model.

---

## 🔥 Demo

[Watch demo video](https://youtu.be/weofTmTcQAM?si=cX__u4LO5Ep0E6x_)

---

## 🚀 Features

- 🎙️ Transcribe audio from:
  - Uploaded audio files
  - YouTube URLs
  - Live microphone input
- 🌍 Translate transcriptions to any target language
- 📄 Export full transcript as a downloadable PDF
- ⚡ Fast, lightweight, and Streamlit-powered UI

---

## 🧰 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Model:** OpenAI Whisper
- **Translation:** Google Translate / DeepL API *(customizable)*
- **Exporting:** FPDF / ReportLab

---

## 📦 Installation

Clone the project:

```bash
git clone https://github.com/armrlm2005/polylingua.git
cd polylingua
```

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🧪 Usage

1. Launch the app with `streamlit run app.py`
2. Select your input method (YouTube URL, mic, or file)
3. Click **Transcribe**
4. Choose a target language for translation (optional)
5. Download the transcript in PDF format

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

### To contribute:

1. Fork the project
2. Create a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a pull request

---

## 🪪 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Aryan Mehta**

- GitHub: [@armrlm2005](https://github.com/armrlm2005)
- LinkedIn: [Aryan Mehta](https://linkedin.com/in/your-link) <!-- Optional -->
- Email: armrlm200518@gmail.com <!-- Optional -->

---

## 💡 Future Plans

- Add subtitle (SRT/VTT) export
- Batch processing of files
- Custom speaker diarization
- Translation quality settings

---

## 🌐 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Streamlit](https://streamlit.io/)
- [Google Translate](https://pypi.org/project/googletrans/)
