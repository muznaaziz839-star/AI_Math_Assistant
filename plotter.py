import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_function():
    x = np.linspace(-10, 10, 100)
    y = x**2  # example parabola

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Example Graph: y = x²")
    ax.grid(True)

    st.pyplot(fig)