from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def solve_problem(question):
    prompt = f"Solve this math problem step by step:\n{question}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a math problem solver."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content