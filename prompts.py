import google.generativeai as genai
import os

from dotenv import load_dotenv
# Set your Gemini API Key
API_key= os.getenv('API_key')
genai.configure(api_key=API_key)

def generate_tech_questions(tech_stack):
    tech_list = ', '.join(tech_stack)

    prompt = f"""
You are a technical interviewer. Generate 3-5 technical interview questions for a candidate proficient in: {tech_list}.
The questions should test core skills and understanding of these technologies. Don't include any introductory text or explanations, just the questions.
"""

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    # Gemini might return a markdown string — split lines
    return [line.strip("-• ") for line in response.text.strip().split('\n') if line.strip()]
    

  