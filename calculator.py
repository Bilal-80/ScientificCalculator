import streamlit as st
import math

# Set the title for the calculator
st.title("Scientific Calculator")

# Display input fields for numbers and operators
st.write("### Enter the values and select the operation")

# Input numbers
num1 = st.number_input("Enter the first number:", format="%.10f")
num2 = st.number_input("Enter the second number (if needed):", format="%.10f")

# Select operation
operation = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division",
                                                  "Exponentiation", "Square Root", "Sine", "Cosine", "Tangent",
                                                  "Logarithm"])

# Display the result
result = None

try:
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    elif operation == "Exponentiation":
        result = num1 ** num2
    elif operation == "Square Root":
        result = math.sqrt(num1) if num1 >= 0 else "Square root of negative number is undefined"
    elif operation == "Sine":
        result = math.sin(math.radians(num1))
    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
    elif operation == "Logarithm":
        result = math.log(num1) if num1 > 0 else "Logarithm of non-positive number is undefined"

    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"Result: {result}")
except Exception as e:
    st.error(f"Error: {e}")
