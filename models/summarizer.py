
import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def summarize_text(text):
    if not text or not text.strip():
        return "No text available to summarize."

    if client is None:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    text = text[:12000]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            "Summarize the following video transcript clearly. "
            "Include the main ideas and important details.\n\n"
            + text
        ),
    )

    if not response.text:
        raise RuntimeError("The summarization API returned an empty response.")

    return response.text.strip()
