
import os
import logging
from google import genai

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_api_key = os.getenv("GEMINI_API_KEY")
_client = genai.Client(api_key=_api_key) if _api_key else None


def summarize_text(text):
    if not text or not text.strip():
        return "No text available to summarize."

    if _client is None:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it in Render Environment Variables."
        )

    # Limit transcript length to control processing time and token usage.
    text = text.strip()[:12000]

    try:
        logger.info("Starting Gemini summarization")

        response = _client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "Summarize this video transcript clearly. "
                "Include the main ideas and important details. "
                "Use concise, easy-to-understand language.\n\n"
                + text
            ),
        )

        if not response.text or not response.text.strip():
            raise RuntimeError("Gemini returned an empty summary.")

        logger.info("Summary generated successfully")
        return response.text.strip()

    except Exception:
        logger.exception("Gemini summarization failed")
        raise
