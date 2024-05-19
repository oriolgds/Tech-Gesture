import whisper

model = whisper.load_model("base")
result = model.transcribe("whisper/cs.mp3")
print(result["text"])