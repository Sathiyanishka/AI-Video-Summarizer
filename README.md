# 🎥 AI Video Summarization & Quiz Generator

## 📌 Project Overview

AI Video Summarization & Quiz Generator is a Flask-based web application that allows users to upload a video, automatically extract its audio, convert speech into text using OpenAI Whisper, generate a concise summary, create multiple-choice quiz questions, and download the results as PDF files.

---

## 🚀 Features

- Upload video files
- Extract audio using MoviePy
- Convert speech to text using OpenAI Whisper
- Generate AI-based summaries
- Generate 10 quiz questions
- Download Summary PDF
- Download Quiz PDF
- Responsive Bootstrap UI
- Loading animation during processing

---

## 🛠️ Technologies Used

- Python
- Flask
- OpenAI Whisper
- MoviePy
- Transformers
- ReportLab
- HTML
- CSS
- Bootstrap

---

## 📂 Project Structure

AI-Video-Summarizer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── transcription.py
│   ├── summarizer.py
│   └── quiz_generator.py
│
├── utils/
│   ├── video_utils.py
│   └── pdf_generator.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── uploads/
│   └── audio/
│
└── output/
    ├── transcripts/
    ├── summaries/
    ├── quizzes/
    └── pdfs/

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd AI-Video-Summarizer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📸 Output

- Transcript (.txt)
- Summary (.txt)
- Quiz (.txt)
- Summary PDF
- Quiz PDF

---

## 🔮 Future Enhancements

- Multi-language support
- Interactive quiz with scoring
- User authentication
- Cloud deployment
- Database integration

---

## 👩‍💻 Author

**Sathiyanishka S**

B.Tech – Artificial Intelligence & Data Science

