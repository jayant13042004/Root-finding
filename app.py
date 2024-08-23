import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from functions import create_function_from_string, newton_raphson, secant_method, bisection_method, false_position_method, df

# Title of the app
st.title('Root Finder')

# Text box for the user to input the equation
equation = st.text_input('Enter your equation f(x) = 0 in terms of x. Example: x**2 - 4*x + 4')

# Dropdown menu to select the method
method = st.selectbox('Select the root-finding method', ('Newton-Raphson', 'Secant', 'Bisection', 'False Position'))

# Input fields based on the selected method
if method in ['Newton-Raphson']:
    guess = st.number_input('Enter initial guess for the root')
elif method in ['Secant']:
    first_guess = st.number_input('Enter first guess for the root')
    second_guess = st.number_input('Enter second guess for the root')
else:
    lower_limit = st.number_input('Enter the lower limit of the interval')
    upper_limit = st.number_input('Enter the upper limit of the interval')

# Button to trigger the root finding process
if st.button('Find Root'):
    try:
        # Create the function from the equation string
        f = create_function_from_string(equation)

        if method == 'Newton-Raphson':
            # Convert initial guess to float
            x0 = float(guess)
            # Find the root using Newton-Raphson method
            root, steps = newton_raphson(f,df, x0)
        
        elif method == 'Secant':
            # Convert initial guesses to float
            x0, x1 = float(first_guess), float(second_guess)
            # Find the root using Secant method
            root, steps = secant_method(f, x0, x1)
        
        elif method == 'Bisection':
            # Convert limits to float
            a, b = float(lower_limit), float(upper_limit)
            # Find the root using Bisection method
            root, steps = bisection_method(f, a, b)
        
        elif method == 'False Position':
            # Convert limits to float
            a, b = float(lower_limit), float(upper_limit)
            # Find the root using False Position method
            root, steps = false_position_method(f, a, b)
        
        # Display the root
        st.write(f"Root found: x = {root:.6f}")
        
        # Plot the function and the root
        x_vals = np.linspace(root - 10, root + 10, 400)
        y_vals = f(x_vals)
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='f(x)')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(root, color='red', linestyle='--', label=f'Root at x = {root:.6f}')
        ax.set_title('Graph of the function and its root')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid(True)
        
        # Display the plot
        st.pyplot(fig)
        
        # Save the plot to a buffer
        buf = BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        
        # Provide option to download the plot
        st.download_button('Download Plot', data=buf, file_name='function_plot.png', mime='image/png')
        
    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
