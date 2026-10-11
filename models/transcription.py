import os
import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    transcript = result["text"]

    os.makedirs("output/transcripts", exist_ok=True)

    filename = os.path.splitext(os.path.basename(audio_path))[0]
    transcript_path = os.path.join(
        "output/transcripts",
        f"{filename}.txt"
    )

    with open(transcript_path, "w", encoding="utf-8") as file:
        file.write(transcript)

    return transcript, transcript_path