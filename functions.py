import numpy as np

# Define the function creation from string
def create_function_from_string(equation):
    allowed_functions = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'log': np.log,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'power': np.power,
        'pi': np.pi,
        'e': np.e
    }
    equation = equation.replace('^', '**')  # Replace ^ with ** for power operation

    def fx_equal_0(x):
        try:
            return eval(equation, {"__builtins__": None}, {**allowed_functions, 'x': x})
        except Exception as e:
            print(f"Error in evaluating the equation: {e}")
            return None

    return fx_equal_0

# Secant method
def secant_method(f, x0, x1, tol=1e-8, max_iter=1000):
    steps = [(x0, f(x0)), (x1, f(x1))]
    for _ in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1) < tol:
            return x1, steps
        if fx1 == fx0:
            raise ValueError("Division by zero in Secant method")
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        steps.append((x_new, f(x_new)))
        x0, x1 = x1, x_new
    raise ValueError("Maximum iterations exceeded. No solution found.")

# Bisection method
def bisection_method(f, a, b, tol=1e-8, max_iter=1000):
    if f(a) * f(b) > 0:
        raise ValueError("Function does not change sign on the interval try different limits or method")
    steps = [(a, f(a)), (b, f(b))]
    for _ in range(max_iter):
        c = (a + b) / 2
        steps.append((c, f(c)))
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, steps
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum iterations exceeded. No solution found.")

# False position method
def false_position_method(f, a, b, tol=1e-8, max_iter=1000):
    if f(a) * f(b) > 0:
        raise ValueError("Function does not change sign on the interval")
    steps = [(a, f(a)), (b, f(b))]
    for _ in range(max_iter):
        fa, fb = f(a), f(b)
        c = a - fa * (b - a) / (fb - fa)
        steps.append((c, f(c)))
        if abs(f(c)) < tol:
            return c, steps
        if f(c) * fa < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum iterations exceeded. No solution found.")

# Numerical derivative
def df(f, x):
    h = 1e-6  # Small step size
    return (f(x + h) - f(x)) / h

# Newton-Raphson method
def newton_raphson(f, df, x0, tol=1e-8, max_iter=1000):
    x = x0
    steps = [(x, f(x))]
    errors = []
    for i in range(max_iter):
        fx = f(x)
        dfx = df(f, x)
        if abs(fx) < tol:
            return x, steps
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / dfx
        steps.append((x_new, f(x_new)))
        errors.append(abs(x_new - x))
        x = x_new
    raise ValueError("Maximum iterations exceeded. No solution found.")
