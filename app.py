import streamlit as st
from lecture_generator import generate_lecture
from solver import solve_problem

st.title("AI Mathematics Assistant")

menu = st.sidebar.selectbox("Choose", ["Lecture", "Solve Problem"])

if menu == "Lecture":
    course = st.text_input("Course Name")
    topic = st.text_input("Topic")
    semester = st.selectbox("Semester", ["1", "2", "3", "4" , "5" , "6", "7","8"])
    difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Generate Lecture"):
        output = generate_lecture(course, topic, semester, difficulty)
        st.write(output)

elif menu == "Solve Problem":
    question = st.text_area("Enter math problem")

    if st.button("Solve"):
        solution = solve_problem(question)
        st.write(solution)