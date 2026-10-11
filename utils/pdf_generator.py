from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def create_pdf(title, content, filename):

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))

    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    paragraphs = content.split("\n")

    for p in paragraphs:
        story.append(Paragraph(p, styles["BodyText"]))

    pdf.build(story)
    