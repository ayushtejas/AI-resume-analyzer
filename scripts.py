import pdfplumber
import spacy

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() + "\n"
    return text.strip()

print(extract_text_from_pdf('Ayush_Kumar_SDE1.pdf'))