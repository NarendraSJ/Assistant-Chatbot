import streamlit as st
from prompts import generate_tech_questions
from storage import save_submission
import re  # <-- ADD THIS at the top

st.set_page_config(page_icon="🤖",page_title="TalentScout Hiring Assistant", layout="centered")
st.markdown('<div class="main-header"><h1>🤖 TalentScout Hiring Assistant</h1><p>Your AI-powered recruitment companion</p></div>', unsafe_allow_html=True)


# ------------------------------------------------------
# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    }
</style>
""", unsafe_allow_html=True)
# ------------------------------------------------------
# Initialize state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "step" not in st.session_state:
    st.session_state.step = "greet"
if "data" not in st.session_state:
    st.session_state.data = {}
if "questions" not in st.session_state:
    st.session_state.questions = []
if "answers" not in st.session_state:
    st.session_state.answers = []
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "greeted" not in st.session_state:
    # Show greeting immediately
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Hi there! I'm your TalentScout Hiring Assistant. Let’s begin.\n\nWhat’s your **full name**?"
    })
    st.session_state.step = "get_name"
    st.session_state.greeted = True


# Helper to display all messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# Chat Flow Logic
# def chatbot_logic(user_input):
#     step = st.session_state.step
#     data = st.session_state.data

#     def bot_says(msg):
#         with st.chat_message("assistant"):
#             st.markdown(msg)
#         st.session_state.messages.append({"role": "assistant", "content": msg})

#     if step == "get_name":
#         data["name"] = user_input
#         bot_says(f"Nice to meet you, **{user_input}**! What’s your **email address**?")
#         st.session_state.step = "get_email"

#     elif step == "get_email":
#         data["email"] = user_input
#         bot_says("Got it! What’s your **phone number**?")
#         st.session_state.step = "get_phone"

#     elif step == "get_phone":
#         data["phone"] = user_input
#         bot_says("Thanks. How many **years of experience** do you have?")
#         st.session_state.step = "get_experience"

#     elif step == "get_experience":
#         data["experience"] = user_input
#         bot_says("Great. What’s the **position you're applying for**?")
#         st.session_state.step = "get_position"

#     elif step == "get_position":
#         data["position"] = user_input
#         bot_says("What’s your **current location**?")
#         st.session_state.step = "get_location"

#     elif step == "get_location":
#         data["location"] = user_input
#         bot_says("Awesome! Now list your **tech stack** (comma-separated):")
#         st.session_state.step = "get_tech_stack"

#     elif step == "get_tech_stack":
#         tech_stack = [t.strip() for t in user_input.split(",")]
#         data["tech_stack"] = tech_stack
#         bot_says("Thanks! Generating questions for: " + ", ".join(tech_stack))
#         st.session_state.questions = generate_tech_questions(tech_stack)
#         st.session_state.step = "ask_questions"
#         st.session_state.q_index = 0
#         bot_says("Q1: " + st.session_state.questions[0])

#     elif step == "ask_questions":
#         st.session_state.answers.append(user_input)
#         st.session_state.q_index += 1

#         if st.session_state.q_index < len(st.session_state.questions):
#             next_q = st.session_state.questions[st.session_state.q_index]
#             bot_says(f"Q{st.session_state.q_index + 1}: {next_q}")
#         else:
#             data["questions"] = st.session_state.questions
#             data["answers"] = st.session_state.answers
#             save_submission(data)
#             bot_says("✅ Thanks! Your interview has been submitted.")
#             st.session_state.step = "done"

#     elif step == "done":
#         bot_says("Want to try again? Just refresh the page 🙂")

# --------------------------------------------


def chatbot_logic(user_input):
    step = st.session_state.step
    data = st.session_state.data

    def bot_says(msg):
        with st.chat_message("assistant"):
            st.markdown(msg)
        st.session_state.messages.append({"role": "assistant", "content": msg})

    if step == "get_name":
        data["name"] = user_input
        bot_says(f"Nice to meet you, **{user_input}**! What’s your **email address**?")
        st.session_state.step = "get_email"

    elif step == "get_email":
        # ✅ Validate email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_input):
            bot_says("❌ That doesn't look like a valid email. Please enter a valid email address.")
            return
        data["email"] = user_input
        bot_says("Got it! What’s your **phone number**?")
        st.session_state.step = "get_phone"

    elif step == "get_phone":
        # ✅ Validate phone number (10 digits)
        cleaned = re.sub(r'\D', '', user_input)  # remove non-digits
        if len(cleaned) != 10:
            bot_says("❌ That doesn't look like a valid phone number. Please enter a 10-digit number.")
            return
        data["phone"] = cleaned
        bot_says("Thanks. How many **years of experience** do you have?")
        st.session_state.step = "get_experience"

    elif step == "get_experience":
        data["experience"] = user_input
        bot_says("Great. What’s the **position you're applying for**?")
        st.session_state.step = "get_position"

    elif step == "get_position":
        data["position"] = user_input
        bot_says("What’s your **current location**?")
        st.session_state.step = "get_location"

    elif step == "get_location":
        data["location"] = user_input
        bot_says("Awesome! Now list your **tech stack** (comma-separated):")
        st.session_state.step = "get_tech_stack"

    elif step == "get_tech_stack":
        tech_stack = [t.strip() for t in user_input.split(",")]
        data["tech_stack"] = tech_stack
        bot_says("Thanks! Generating questions for: " + ", ".join(tech_stack))
        st.session_state.questions = generate_tech_questions(tech_stack)
        st.session_state.step = "ask_questions"
        st.session_state.q_index = 0
        bot_says("Q1: " + st.session_state.questions[0])

    elif step == "ask_questions":
        st.session_state.answers.append(user_input)
        st.session_state.q_index += 1

        if st.session_state.q_index < len(st.session_state.questions):
            next_q = st.session_state.questions[st.session_state.q_index]
            bot_says(f"Q{st.session_state.q_index + 1}: {next_q}")
        else:
            data["questions"] = st.session_state.questions
            data["answers"] = st.session_state.answers
            save_submission(data)
            bot_says("✅ Thanks! Your interview has been submitted.")
            st.session_state.step = "done"

    elif step == "done":
        bot_says("Want to try again? Just refresh the page 🙂")

# --------------------------------------------
# Chat Input (always shown)
if prompt := st.chat_input("Type your response..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    chatbot_logic(prompt)
