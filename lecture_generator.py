from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_lecture(topic, course, semester, difficulty):
    prompt = f"""
    Create a {difficulty} level math lecture on {topic}.
    Course: {course}
    Semester: {semester}

    Include:
    - Explanation
    - Examples
    - Key formulas
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content