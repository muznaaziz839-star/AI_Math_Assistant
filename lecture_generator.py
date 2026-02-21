def generate_lecture(topic, course, semester, difficulty):
    lectures = {
        "Derivatives": f"""
# 📘 Lecture: Derivatives

## 🎓 Course: {course} | Semester: {semester} | Level: {difficulty}

### 🔹 What is a Derivative?
A derivative measures how a function changes as its input changes.

### 🔹 Formula
f'(x) = lim(h→0) [f(x+h) - f(x)] / h

### 🔹 Example
If f(x) = x²  
f'(x) = 2x

### 🔹 Step-by-Step
1. Start with function: x²  
2. Apply power rule  
3. Multiply by exponent → 2x  

### 🔹 Practice Problem
Find derivative of f(x) = 3x²

### ✅ Solution
f'(x) = 6x
""",
        "Integration": f"""
# 📘 Lecture: Integration

## 🎓 Course: {course} | Semester: {semester} | Level: {difficulty}

### 🔹 What is Integration?
Integration finds the area under a curve.

### 🔹 Formula
∫ xⁿ dx = xⁿ⁺¹ / (n+1)

### 🔹 Example
∫ x² dx = x³/3

### 🔹 Practice Problem
Find ∫ 2x dx

### ✅ Solution
x² + C
"""
    }

    return lectures.get(topic, "Lecture not available for this topic yet.")