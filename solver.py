import sympy as sp

# Define symbol
x = sp.symbols('x')

def solve_expression(expr):
    """
    Solves or processes a math expression.
    Supports:
    - Solving equations
    - Simplifying expressions
    - Derivatives
    - Integrals
    """

    try:
        # Convert string to sympy expression
        expression = sp.sympify(expr)

        # If expression contains '=' → solve equation
        if "=" in expr:
            left, right = expr.split("=")
            equation = sp.sympify(left) - sp.sympify(right)
            solution = sp.solve(equation, x)
            return f"Solutions: {solution}"

        # Detect derivative request
        elif "diff" in expr.lower():
            derivative = sp.diff(expression, x)
            return f"Derivative: {derivative}"

        # Detect integral request
        elif "integrate" in expr.lower() or "int" in expr.lower():
            integral = sp.integrate(expression, x)
            return f"Integral: {integral} + C"

        # Otherwise simplify
        else:
            simplified = sp.simplify(expression)
            return f"Simplified: {simplified}"

    except Exception as e:
        return f"⚠️ Error: {str(e)}"