from transformers import pipeline

# Load summarization model (downloads once)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):

    # BART has an input length limit
    text = text[:3000]

    summary = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]