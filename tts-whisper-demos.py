# Author: Niko Lorantos
# https://platform.openai.com/docs/overview for more information

import os
from pathlib import Path
from openai import OpenAI # make sure to 'pip install openai' if you haven't already
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI client
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

# First, let's generate speech using OpenAI's text-to-speech model
speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Here is OpenAI's text to speech model in action. Pretty cool, right?"
)

response.stream_to_file(speech_file_path)

# Then, you can transcribe the audio file using Whisper!
# Transcribing generated speech back to text is fairly useless, but this is the basic code needed to do any TTS or speech transcription tasks.
audio_file= open(speech_file_path, "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)