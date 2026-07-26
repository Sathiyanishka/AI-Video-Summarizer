import os
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

    try:

        if "video" not in request.files:
            return render_template(
                "index.html",
                error="Please select a video."
            )

        file = request.files["video"]

        if file.filename == "":
            return render_template(
                "index.html",
                error="Please select a video."
            )

        # Save video
        video_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(video_path)

        print("✅ Video Saved")

        # Extract Audio
        audio_path = extract_audio(video_path)

        print("✅ Audio Extracted")

        # Speech To Text
        transcript, transcript_path = transcribe_audio(audio_path)

        print("✅ Transcript Generated")

        # Summary
        summary = summarize_text(transcript)

        summary_path = os.path.join(
            "output/summaries",
            os.path.splitext(file.filename)[0] + "_summary.txt"
        )

        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)

        print("✅ Summary Saved")

        # Quiz
        quiz = generate_quiz(summary)

        quiz_path = os.path.join(
            "output/quizzes",
            os.path.splitext(file.filename)[0] + "_quiz.txt"
        )

        with open(quiz_path, "w", encoding="utf-8") as f:
            f.write(quiz)

        print("✅ Quiz Saved")

        # PDF
        summary_pdf = "output/pdfs/latest_summary.pdf"
        quiz_pdf = "output/pdfs/latest_quiz.pdf"

        create_pdf(
            "Video Summary",
            summary,
            summary_pdf
        )

        create_pdf(
            "Video Quiz",
            quiz,
            quiz_pdf
        )

        print("✅ PDF Generated")

        return render_template(
            "index.html",
            video=file.filename,
            transcript=transcript,
            summary=summary,
            quiz=quiz,
            success=True
        )

    except Exception as e:

        print("ERROR:", e)

        return render_template(
            "index.html",
            error=str(e)
        )


@app.route("/download/summary")
def download_summary():

    return send_file(
        "output/pdfs/latest_summary.pdf",
        as_attachment=True
    )


@app.route("/download/quiz")
def download_quiz():

    return send_file(
        "output/pdfs/latest_quiz.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    print("🚀 Starting Flask Server...")
    app.run(debug=True)