# 🤖 TalentScout Hiring Assistant Chatbot

A conversational AI assistant built with Streamlit and Gemini API to simulate a hiring experience. It collects candidate details, dynamically generates technical questions based on tech stack, stores the results, and presents a modern chat-style UI. Includes an admin dashboard for viewing all submissions.

---

## 📌 Project Overview

It is an interactive AI-powered **Hiring Assistant Chatbot** designed to:

- Engage users through a dynamic, chat-like interface.
- Collect candidate information (name, email, phone, experience, location, etc.).
- Validate inputs like email and phone formats.
- Generate **3–5 customized technical interview questions** using **Gemini (Google AI) API** based on the tech stack provided.
- Collect candidate responses and **store them locally in JSON**.

---

## ⚙️ Installation Instructions

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/NarendraSJ/Assistant-Chatbot.git
cd Assistant-chatbot
```

### ✅ Step 2: Create a virtual environment

```bash
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### ✅ Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Step 4: Set up Gemini API Key

1. Go to [https://makersuite.google.com/app](https://makersuite.google.com/app)
2. Generate an API key.
3. Option A: Set the environment variable in your terminal:

```bash
export GEMINI_API_KEY=your-api-key-here
```

4. Option B: Replace `api_key=os.getenv("GEMINI_API_KEY")` in `prompts.py` with your actual key (not recommended for production).

---

## ▶️ Usage Guide

To run the chatbot:

```bash
streamlit run app.py
```

- It will launch at `http://localhost:8501`

---

## 🧠 Technical Details

### 🔧 Libraries Used

- `streamlit` – for UI
- `google-generativeai` – to access Gemini
- `re` – for input validation
- `json` – for storing user data
- `os` – for file operations

### 🤖 Model Used

- **Model:** `models/gemini-1.5-pro-latest`
- **Provider:** Google AI (via Gemini API)
- **Access:** Prompt-based generation using the Gemini SDK

### 🧱 Architecture

- `app.py` – Handles the UI, flow, and routing
- `prompts.py` – Handles prompt crafting and Gemini interaction
- `storage.py` – Stores all submissions to `submissions.json`
- `submissions.json` – Stores user responses in structured format

---

## ✨ Prompt Design

Prompts are dynamically created using:

```txt
Generate 3-5 concise and relevant technical interview questions for a candidate skilled in: Python, Django, MySQL.
```

Multiple templates are randomized to avoid repetition, making each interaction feel unique.Like :
```txt
    "Generate 5 advanced technical interview questions for technology: {}.Don't include any explanations or introductory text ,just the questions",
    "Create 5 challenging and real-world scenario-based questions covering: {}.Don't include any explanations or introductory text ,just the questions",
    "Write 5 practical questions to evaluate a candidate's skills in: {}.Don't include any explanations or introductory text ,just the questions",
```
---

## 🧗 Challenges & Solutions

- **Repetitive Questions:** Solved by prompt randomization and varied instruction styles.
- **Large Model Size:** Initially used Hugging Face models locally, but shifted to cloud-based Gemini API.
- **Validation Issues:** Added regex validation for email and phone inputs.
- **Lack of Interactivity:** Switched from form-based UI to chat-style using `st.chat_message()`.

---


## 👨‍💻 Author

Built by Narendra Jadhav  
For AI/ML Internship Assignment 

---
