import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_tech_questions(tech_stack):
    prompt = f"""
You are a technical interviewer. Generate 3-5 technical interview questions for a candidate proficient in: {tech_stack}.
The questions should test core skills and understanding of these technologies. Don't include any introductory text or explanations, just the questions.
"""

    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content(prompt)
        return [line.strip("-• ") for line in response.text.strip().split('\n') if line.strip()]

    except Exception as e:
        return [f"❌ Error generating questions: {str(e)}"]

