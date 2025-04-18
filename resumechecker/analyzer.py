import pdfplumber
import spacy
import os
from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() + "\n"
    return text.strip()

extract_text_from_pdf('Ayush_Kumar_SDE1.pdf')


def analyse_resume_with_llm(resume_text, job_description):
    prompt = f"""
        You are  AI assistant that analyzes resumes for a software engineering job application.
        Given a resume and a job description, extract the following details.

        1. Identify all skills mentioned in the resume
        2. Calculate the total years of experience
        3. Categorize the projects based on domain(e.g. Web Development, Cloud, etc.)
        4. Rank the resume relevance to the job description n a scale of 0 to 100.

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        provide the output in valid JSON format with this structure:
        {{
            "rank": "<percentage>",
            "skills" : ["skill1", "skill2", ....],
            "total_experience": "<number of years>",
            "project_category": ["category1", "category2", ....]
        }}
"""
    try:
        client = Groq(api_key=API_KEY)
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages =[{'role':'user', 'content': prompt}],
            temperature=0.7,
            response_format = {'type': "json_object"}
        )
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        print(e)


def process_resume(pdf_path, job_description):
    try:
        resume_text = extract_text_from_pdf(pdf_path)
        data = analyse_resume_with_llm(resume_text, job_description)
        print(data)
        return data
    except Exception as e:
        print(e)
        return None
