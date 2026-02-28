import streamlit as st
from lecture_generator import generate_lecture
from solver import solve_problem
from plotter import plot_function
from pdf_export import export_to_pdf
from chapters import chapters
from groq import Groq

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="AI Math Assistant", layout="wide")

# ==============================
# 📌 SIDEBAR NAVIGATION
# ==============================
st.sidebar.title("📚 Navigation")
mode = st.sidebar.radio(
    "Choose an option:",
    ["📘 Generate Lecture", "🧮 Solve Problem", "💬 Chatbot"]
)

# ==============================
# 📘 LECTURE GENERATOR
# ==============================
if mode == "📘 Generate Lecture":
    st.title("📘 Lecture Generator")

    course = st.selectbox("Course", ["Calculus"])
    chapter = st.selectbox("Chapter", list(chapters.keys()))
    topic = st.selectbox("Topic", chapters[chapter])
    level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Generate Lecture"):
        with st.spinner("Generating lecture..."):
            lecture = generate_lecture(course, chapter, topic, level)

        st.subheader("📖 Lecture Output")
        st.markdown(lecture, unsafe_allow_html=True)

        # 📈 Show graph for calculus topics
        if any(word in topic.lower() for word in ["derivative", "function", "curve", "graph"]):
            st.subheader("📈 Visual Representation")
            plot_function()

        # 📄 PDF Export
        if st.button("📄 Download as PDF"):
            pdf_path = export_to_pdf(lecture)

            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download PDF",
                    data=f,
                    file_name="lecture.pdf",
                    mime="application/pdf"
                )

# ==============================
# 🧮 PROBLEM SOLVER
# ==============================
elif mode == "🧮 Solve Problem":
    st.title("🧮 Problem Solver")

    question = st.text_input("Enter your math problem:")

    if st.button("Solve"):
        with st.spinner("Solving..."):
            solution = solve_problem(question)

        st.success("✅ Solution")
        st.markdown(solution, unsafe_allow_html=True)

# ==============================
# 💬 MATH CHATBOT
# ==============================
elif mode == "💬 Chatbot":
    st.title("💬 Math Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show previous messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Ask a math question...")

    if user_input:
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # AI Response (Math-only restriction)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a mathematics tutor. Only answer math-related questions. If the question is not about math, politely refuse."
                },
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content

        # Save AI message
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)