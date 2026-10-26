# week3_ex03_functions.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def is_even(num):
    return num % 2 == 0

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(greet("Zoyi"))
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("Is 4 even?", is_even(4))
print("Grade for 85:", get_grade(85))