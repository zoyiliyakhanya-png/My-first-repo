# Question 1: Using a for loop with a list
fruits = ["apple", "banana", "orange", "mango", "grapes"]
print("Question 1:")
for fruit in fruits:
    print(fruit)

print("\n" + "-"*50 + "\n")

# Question 2: Using a while loop for countdown
print("Question 2: Countdown from 5 to 1")
count = 5
while count >= 1:
    print(count)
    count -= 1

print("\n" + "-"*50 + "\n")

# Question 3: Using a for loop with range()
print("Question 3: First 10 square numbers")
for i in range(1, 11):
    print(f"{i} squared is {i*i}")

print("\n" + "-"*50 + "\n")

# Question 4: Using the random module
import random
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
print("Question 4: 3 random colors")
for _ in range(3):
    print(random.choice(colors))

print("\n" + "-"*50 + "\n")

# Question 5: Creating and using a custom module
import math_operations
print("Question 5: Custom module functions")
print(f"Add 10 + 5 = {math_operations.add(10, 5)}")
print(f"Subtract 10 - 5 = {math_operations.subtract(10, 5)}")
print(f"Multiply 10 * 5 = {math_operations.multiply(10, 5)}")
print(f"Divide 10 / 5 = {math_operations.divide(10, 5)}")