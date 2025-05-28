import os
import random
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

question_styles = [
    "Generate 5 advanced technical interview questions for technology: {}.Don't include any explanations or introductory text ,just the questions",
    "Create 5 challenging and real-world scenario-based questions covering: {}.Don't include any explanations or introductory text ,just the questions",
    "Write 5 practical questions to evaluate a candidate's skills in: {}.Don't include any explanations or introductory text ,just the questions",
    "You are a tech lead hiring for a senior position. Ask 5 deep-dive questions on: {}.Don't include any explanations or introductory text ,just the questions",
    "Formulate 5 unique, thoughtful, and non-repetitive interview questions about: {}.Don't include any explanations or introductory text ,just the questions",
]

def generate_tech_questions(tech_stack):
    tech_list = ', '.join(tech_stack)
    template = random.choice(question_styles)
    prompt = template.format(tech_list)

    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content(prompt)
        return [line.strip("-• ") for line in response.text.strip().split('\n') if line.strip()]

    except Exception as e:
        return [f"❌ Error generating questions: {str(e)}"]



