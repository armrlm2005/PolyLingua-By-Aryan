# 🎧 PolyLingua by Aryan

> **A powerful, user-friendly tool to generate transcripts from YouTube videos, uploaded audio files, or live microphone input — and translate them into your chosen language in just one click.**

---

## 🚀 About the Project

**PolyLingua by Aryan** is a **Streamlit-based web app** built to simplify the process of **audio transcription and translation**.  
It combines the power of **OpenAI's Whisper** model with modern translation tools to generate **highly accurate transcripts in multiple languages**.

Whether you're a **student, journalist, content creator, or language enthusiast** — PolyLingua is your all-in-one **transcription and translation assistant**.

---

## 🧠 Features

### ✅ Transcribe From:
- 🎧 **Uploaded audio files** (`.mp3`, `.wav`)
- 📺 **YouTube video URLs**
- 🎙️ **Live microphone recording**

### ✅ Translate Into:
- English, Hindi, Gujarati, French, Spanish, German, Japanese, Chinese, Arabic, Punjabi, and more!

### ✅ Output:
- 📄 **Downloadable PDF** of:
  - Original transcript
  - Translated version

### ✅ Interface:
- 🚀 **Clean UI built with Streamlit**

---

## 🛠️ Tech Stack

| Tool               | Purpose                            |
|--------------------|-------------------------------------|
| `Python 3.10+`     | Programming language                |
| `Streamlit`        | Web interface framework             |
| `openai-whisper`   | Transcription engine                |
| `yt-dlp`           | YouTube audio downloader            |
| `sounddevice` & `scipy` | Microphone input                |
| `deep-translator`  | Language translation                |
| `reportlab`        | PDF generation                      |

---

## 📁 Folder Structure

PolyLingua-By-Aryan/
│
├── app.py # Main Streamlit app
├── transcribe.py # Transcription and translation logic
├── utils.py # Helper utilities: file handling, PDF generation
├── requirements.txt # Required packages list
├── /venv # Virtual environment (not committed)
└── /output # Transcript and PDF files

---

## 🔧 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/armrlm2005/PolyLingua-By-Aryan.git
cd PolyLingua-By-Aryan
