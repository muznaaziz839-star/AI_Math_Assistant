import streamlit as st
import solver
from lecture_generator import generate_lecture

# Page title
st.title("📘 AI Math Assistant")

# ---------- Lecture Generator ----------
st.header("📖 Generate Math Lecture")
course = st.text_input("Course Name")
topic = st.selectbox("Select Topic", ["Derivatives", "Integration"])
semester = st.selectbox("Semester", ["1", "2", "3", "4"])
difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Lecture"):
    lecture = generate_lecture(topic, course, semester, difficulty)
    st.markdown(lecture)

# ---------- Divider ----------
st.divider()

# ---------- Solver ----------
st.header("🧮 Solve Equation")

expression = st.text_input("Enter equation (example: x**2 - 4)")

if st.button("Solve"):
    if expression:
        result = solver.solve_expression(expression)
        st.success(f"Solution: {result}")
    else:
        st.warning("Please enter an equation.")