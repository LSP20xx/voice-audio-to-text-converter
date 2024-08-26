import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_dir = "audios"
transcriptions = {}
audio_extensions = [".ogg", ".mp3", ".wav", ".m4a", ".flac", ".aac"]

for filename in os.listdir(audio_dir):
    if any(filename.endswith(ext) for ext in audio_extensions):
        audio_file_path = os.path.join(audio_dir, filename)

        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file,
            )

            transcriptions[filename] = response["text"]
            print(f"Transcription of {filename}:")
            print(response["text"])
            print()

with open("transcriptions.txt", "w") as file:
    for filename, transcription in transcriptions.items():
        file.write(f"{filename}:\n{transcription}\n\n")
