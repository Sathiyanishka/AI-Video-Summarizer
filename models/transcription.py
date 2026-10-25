import os
import whisper

_model = None


def transcribe_audio(audio_path):
    global _model

    if _model is None:
        _model = whisper.load_model("tiny", device="cpu")

    result = _model.transcribe(audio_path, fp16=False)
    transcript = result["text"].strip()

    output_dir = "output/transcripts"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(os.path.basename(audio_path))[0]
    transcript_path = os.path.join(output_dir, f"{filename}.txt")

    with open(transcript_path, "w", encoding="utf-8") as file:
        file.write(transcript)

    return transcript, transcript_path
