import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, send_file

from utils.video_utils import extract_audio
from models.transcription import transcribe_audio
from models.summarizer import summarize_text
from models.quiz_generator import generate_quiz
from utils.pdf_generator import create_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
AUDIO_FOLDER = "static/audio"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["AUDIO_FOLDER"] = AUDIO_FOLDER

# Create folders
folders = [
    "static/uploads",
    "static/audio",
    "output/transcripts",
    "output/summaries",
    "output/quizzes",
    "output/pdfs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/upload", methods=["POST"])
def upload():
    stage = "starting upload"

    try:
        if "video" not in request.files:
            return render_template(
                "index.html",
                error="Please select a video."
            )

        file = request.files["video"]

        if not file or not file.filename:
            return render_template(
                "index.html",
                error="Please select a video."
            )

        # Use a safe filename
        filename = secure_filename(file.filename)

        if not filename:
            return render_template(
                "index.html",
                error="Invalid video filename."
            )

        video_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        stage = "saving video"
        print(f"[PROCESS] {stage}", flush=True)
        file.save(video_path)

        stage = "extracting audio"
        print(f"[PROCESS] {stage}", flush=True)
        audio_path = extract_audio(video_path)
        print("[SUCCESS] Audio extracted", flush=True)

        stage = "transcribing audio with Whisper"
        print(f"[PROCESS] {stage}", flush=True)
        transcript, transcript_path = transcribe_audio(audio_path)
        print("[SUCCESS] Transcript generated", flush=True)

        stage = "generating summary"
        print(f"[PROCESS] {stage}", flush=True)
        summary = summarize_text(transcript)

        summary_path = os.path.join(
            "output/summaries",
            os.path.splitext(filename)[0] + "_summary.txt"
        )
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)

        stage = "generating quiz"
        print(f"[PROCESS] {stage}", flush=True)
        quiz = generate_quiz(summary)

        quiz_path = os.path.join(
            "output/quizzes",
            os.path.splitext(filename)[0] + "_quiz.txt"
        )
        with open(quiz_path, "w", encoding="utf-8") as f:
            f.write(quiz)

        stage = "generating PDFs"
        print(f"[PROCESS] {stage}", flush=True)

        create_pdf(
            "Video Summary",
            summary,
            "output/pdfs/latest_summary.pdf"
        )
        create_pdf(
            "Video Quiz",
            quiz,
            "output/pdfs/latest_quiz.pdf"
        )

        print("[SUCCESS] All processing completed", flush=True)

        return render_template(
            "index.html",
            video=filename,
            transcript=transcript,
            summary=summary,
            quiz=quiz,
            success=True
        )

    except Exception:
        app.logger.exception(
            "Video processing failed at stage: %s",
            stage
        )
        return render_template(
            "index.html",
            error=f"Processing failed during: {stage}. Check server logs."
        ), 500
