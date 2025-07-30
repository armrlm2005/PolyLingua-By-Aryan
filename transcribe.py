import whisper
from utils import translate_text

model = whisper.load_model("medium", device = "cpu")

def transcribe_audio(audio_path):
    return model.transcribe(audio_path)


