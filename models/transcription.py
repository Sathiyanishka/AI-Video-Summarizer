import os
import logging
import whisper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_model = None


def transcribe_audio(audio_path):
    global _model

    try:
        if _model is None:
            logger.info("Loading Whisper tiny model...")
            _model = whisper.load_model("tiny", device="cpu")
            logger.info("Whisper model loaded successfully.")

        logger.info("Starting transcription: %s", audio_path)
        result = _model.transcribe(audio_path, fp16=False)
        transcript = result["text"].strip()

        output_dir = "output/transcripts"
        os.makedirs(output_dir, exist_ok=True)

        filename = os.path.splitext(os.path.basename(audio_path))[0]
        transcript_path = os.path.join(output_dir, f"{filename}.txt")

        with open(transcript_path, "w", encoding="utf-8") as file:
            file.write(transcript)

        logger.info("Transcript saved: %s", transcript_path)
        return transcript, transcript_path

    except Exception:
        logger.exception("Whisper transcription failed")
        raise
