import streamlit as st
from prompts import generate_tech_questions
from storage import save_submission

st.set_page_config(page_title="TalentScout Chatbot")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.questions = []
    st.session_state.answers = []

st.title("🤖 TalentScout Hiring Assistant")

# Step 0: Greeting
if st.session_state.step == 0:
    st.write("👋 Welcome! Type `start` to begin your interview.")
    if st.text_input("You:", key="greet").lower() == "start":
        st.session_state.step = 1
        st.rerun()

# Step 1: Candidate Info
elif st.session_state.step == 1:
    st.subheader("📋 Candidate Information")
    st.session_state.data["name"] = st.text_input("Full Name")
    st.session_state.data["email"] = st.text_input("Email")
    st.session_state.data["phone"] = st.text_input("Phone Number")
    st.session_state.data["experience"] = st.text_input("Years of Experience")
    st.session_state.data["position"] = st.text_input("Desired Position")
    st.session_state.data["location"] = st.text_input("Current Location")

    if all(st.session_state.data.values()):
        if st.button("Next"):
            st.session_state.step = 2
            st.rerun()

# Step 2: Tech Stack
elif st.session_state.step == 2:
    st.subheader("💻 Tech Stack")
    tech_input = st.text_input("List your tech stack (comma-separated)")
    if tech_input:
        tech_stack = [t.strip() for t in tech_input.split(",")]
        st.session_state.data["tech_stack"] = tech_stack
        st.session_state.questions = generate_tech_questions(tech_stack)
        st.session_state.step = 3
        st.rerun()

# Step 3: Q&A
elif st.session_state.step == 3:
    st.subheader("🧪 Answer Technical Questions")
    for i, question in enumerate(st.session_state.questions):
        answer = st.text_area(f"{i+1}. {question}", key=f"q{i}")
        if len(st.session_state.answers) <= i:
            st.session_state.answers.append(answer)
        else:
            st.session_state.answers[i] = answer

    if st.button("Submit Interview"):
        st.session_state.data["questions"] = st.session_state.questions
        st.session_state.data["answers"] = st.session_state.answers
        save_submission(st.session_state.data)
        st.success("✅ Your responses have been recorded.")
        st.session_state.step = 4

# Step 4: Thank You
elif st.session_state.step == 4:
    st.write("🎉 Thank you for completing the interview!")
    if st.button("Start Over"):
        st.session_state.clear()
        st.rerun()
