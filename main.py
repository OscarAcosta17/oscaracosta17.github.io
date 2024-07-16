import whisper

model = whisper.load_model("medium")
result = model.transcribe("a.mp3")
print(result["text"])

from whisper.utils import write_txt
