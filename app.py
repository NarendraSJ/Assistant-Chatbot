import streamlit as st
from prompts import generate_tech_questions
import time

st.set_page_config(page_title="TalentScout Hiring Assistant")
st.title("🤖 TalentScout Hiring Assistant")

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.questions = []

# Greet
if st.session_state.step == 0:
    st.write("Hi, I'm your assistant for initial screening! Type `start` to begin.")
    user_input = st.text_input("You:", key="greet")
    if user_input.lower() == "start":
        st.session_state.step = 1
        st.rerun()

# Collect Info
elif st.session_state.step == 1:
    st.write("Let's gather your details.")
    st.session_state.data['name'] = st.text_input("Full Name")
    st.session_state.data['email'] = st.text_input("Email")
    st.session_state.data['phone'] = st.text_input("Phone Number")
    st.session_state.data['experience'] = st.text_input("Years of Experience")
    st.session_state.data['position'] = st.text_input("Desired Position")
    st.session_state.data['location'] = st.text_input("Current Location")

    if all(st.session_state.data.values()):
        if st.button("Next"):
            st.session_state.step = 2
            st.rerun()

# Collect Tech Stack
elif st.session_state.step == 2:
    tech_stack = st.text_input("Enter your tech stack (comma separated):")
    if tech_stack:
        st.session_state.data['tech_stack'] = [tech.strip() for tech in tech_stack.split(',')]
        st.session_state.step = 3
        st.rerun()

# Generate Questions
elif st.session_state.step == 3:
    st.write(f"Tech Stack: {', '.join(st.session_state.data['tech_stack'])}")
    st.write("Generating questions based on your tech stack...")
    with st.spinner("Generating..."):
        questions = generate_tech_questions(st.session_state.data['tech_stack'])
        st.session_state.questions = questions
        time.sleep(2)
        st.session_state.step = 4
        st.rerun()

# Show Questions
elif st.session_state.step == 4:
    st.write("Please answer the questions below:")  
    answers = []
    for idx, question in enumerate(st.session_state.questions, 1):
        answer = st.text_input(f"Q{idx}: {question}", key=f"answer_{idx}")
        answers.append(answer)

    all_answered = all(ans.strip() for ans in answers)
    if st.button("Submit Answers", disabled=not all_answered):
        for idx, ans in enumerate(answers, 1):
            st.session_state.data[f"answer_{idx}"] = ans
        st.write("Thank you for your answers! We will review them and get back to you.")
        st.session_state.step = 5
        st.rerun()

# Final Step
elif st.session_state.step == 5:
    st.write("You have completed the initial screening!")
    if st.button("End Chat"):
        st.write("Thank you! Our team will reach out to you soon.")
        st.session_state.step = 0



    # # for idx, q in enumerate(st.session_state.questions, 1):
    # #     st.write(f"{idx}. {q}")
    # if st.button("End Chat"):
    #     st.write("Thank you! Our team will reach out to you soon.")
    #     st.session_state.step = 0
