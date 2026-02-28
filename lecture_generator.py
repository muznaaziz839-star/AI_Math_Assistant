from groq import Groq
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ✅ Create Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


# ==============================
# 📈 Graph Function (ADD AT TOP)
# ==============================
def plot_function():
    x = np.linspace(-10, 10, 200)
    y = x**2  # example curve

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Example Function Graph")
    st.pyplot(fig)


# ==============================
# 📚 Lecture Generator
# ==============================
def generate_lecture(course, chapter, topic, level):
    prompt = f"""
You are a Mathematics tutor.

Course: {course}
Chapter: {chapter}
Topic: {topic}
Level: {level}

Follow level rules:
Beginner → definition + simple explanation + easy example
Intermediate → detailed explanation + worked examples
Advanced → rigorous explanation + applications

IMPORTANT:
• Use LaTeX formatting for all mathematical expressions.
• Wrap equations using $...$ for inline math and $$...$$ for block equations.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful math tutor."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content