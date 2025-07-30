import os
import tempfile
import shutil
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from yt_dlp import YoutubeDL
from deep_translator import GoogleTranslator

recording_data = []
stream = None

def create_transcript_txt(text, filename="transcript.txt"):
    output_path = os.path.join(tempfile.gettempdir(), filename)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        raise RuntimeError(f"Failed to write text file: {e}")
    return output_path


def start_recording(fs=44100):
    global stream, recording_data
    recording_data = []

    def callback(indata, frames, time, status):
        if status:
            print(f"{status}")
        recording_data.append(indata.copy())

    stream = sd.InputStream(callback=callback, channels=1, samplerate=fs)
    stream.start()
    print("Recording started...")

def stop_recording(fs=44100):
    global stream, recording_data
    if stream:
        stream.stop()
        stream.close()
        stream = None

    if not recording_data:
        raise RuntimeError("No audio was recorded.")

    audio = np.concatenate(recording_data, axis=0)
    output_path = os.path.join(tempfile.gettempdir(), "mic_input.wav")
    write(output_path, fs, audio)
    print(f"Recording saved to {output_path}")
    return output_path

def save_uploaded_file(uploaded_file):
    try:
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(uploaded_file, f)
        return file_path
    except Exception as e:
        raise RuntimeError(f"Failed to save uploaded file: {e}")

def download_youtube_audio(url):
    temp_dir = tempfile.gettempdir()
    output_template = os.path.join(temp_dir, "yt_audio.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)

    final_path = os.path.join(temp_dir, "yt_audio.mp3")
    if not os.path.exists(final_path):
        raise FileNotFoundError(f"Audio not found at {final_path}")

    return final_path

def translate_text(text, target_lang='fr'):

    def chunk_text(text, max_length=3000):
        chunks = []
        current_chunk = ""

        for sentence in text.split('. '):
            if len(current_chunk) + len(sentence) < max_length:
                current_chunk += sentence + ". "
            else:
                chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def actual_translate(chunk):
        return GoogleTranslator(source="auto", target=target_lang).translate(chunk)

    chunks = chunk_text(text)
    translated_chunks = [actual_translate(chunk) for chunk in chunks]
    return " ".join(translated_chunks)
