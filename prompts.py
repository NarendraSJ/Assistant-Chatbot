import os
import google.generativeai as genai
import re
import random

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

question_styles = (
    "Generate exactly 3 to 5 technical interview questions for a candidate with skills in: {}.\n"
    "Only output the questions. No headings, no explanations, no code, no greetings.\n"
    "Format strictly as:\n"
    "1. Question one?\n"
    "2. Question two?\n"
    "...",

    "Create 5 challenging and real-world scenario-based questions covering: {}.The questions should test core skills and understanding of these technologies. "
    "Only output the questions. No headings, no explanations, no code, no greetings.\n"
    "Format strictly as:\n"
    "1. Question one?\n"
    "2. Question two?\n"
    "...",

    "Write 5 practical questions to evaluate a candidate's skills in: {}.The questions should test core skills and understanding of these technologies."
    "Only output the questions. No headings, no explanations, no code, no greetings.\n"
    "Format strictly as:\n"
    "1. Question one?\n"
    "2. Question two?\n"
    "...",

    "You are a tech lead hiring for a senior position. Ask 5 deep-dive questions on: {}.The questions should test core skills and understanding of these technologies."
    "Only output the questions. No headings, no explanations, no code, no greetings.\n"
    "Format strictly as:\n"
    "1. Question one?\n"
    "2. Question two?\n"
    "...",

    "Formulate 5 unique, thoughtful, and non-repetitive interview questions about: {}.The questions should test core skills and understanding of these technologies." 
    "Only output the questions. No headings, no explanations, no code, no greetings.\n"
    "Format strictly as:\n"
    "1. Question one?\n"
    "2. Question two?\n"
    "..."


)

def generate_tech_questions(tech_stack):
    tech_str = ', '.join(tech_stack)
    prompt = random.choice(question_styles).format(tech_str)

    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
        response = model.generate_content(prompt)
        raw_output = response.text

        # Extract only "1. ..." lines
        questions = re.findall(r'\d+\.\s+(.*)', raw_output)

        cleaned = [q.strip() for q in questions if len(q.strip()) > 5]
        return cleaned[:5]

    except Exception as e:
        return [f"❌ Error generating questions: {str(e)}"]
    