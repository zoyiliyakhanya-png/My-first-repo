# week3_ex02_operators.py
print("=== WEEK 3 EXERCISE 02 - OPERATORS ===")
num1 = 20
num2 = 6
print(f"\n1. Arithmetic Operators (num1={num1}, num2={num2})")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponent: {num1} ** 2 = {num1 ** 2}")
print(f"\n2. Comparison Operators")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
a = True
b = False
print(f"\n3. Logical Operators (a=True, b=False)")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"\n4. Conditional Logic - Grade System")
score = 75
if score >= 90:
    grade = "A - Excellent"
elif score >= 75:
    grade = "B - Good"
elif score >= 50:
    grade = "C - Pass"
else:
    grade = "F - Fail"
print(f"Score: {score} -> Grade: {grade}")
print(f"\n5. Even/Odd Checker")
number = 15
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
print(f"\n6. Assignment Operators")
x = 10
print(f"Start x = {x}")
x += 5
print(f"After x += 5: {x}")
x *= 2
print(f"After x *= 2: {x}")
print("\n=== Exercise Complete ===")
