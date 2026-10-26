# Question 1: Basic Function Definition and Calling
# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    print("Hello, World!")

# TODO: Call the 'greet' function
greet()

# Question 2: Function with Parameters
# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):
    print(f"Hello, {name}!")

# TODO: Call the 'personalized_greeting' function with your name
personalized_greeting("Zoyi")

# Question 3: Function with Return Value
# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
def square(number):
    return number * number

# TODO: Call the 'square' function with the number 5 and print the result
print(square(5))

# Question 4: Function with Multiple Parameters and Return Value
# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length, width):
    return length * width

# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
print(rectangle_area(4, 5))

# Question 5: Using a Function as an Argument
# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(func, number):
    return func(number)

print(apply_operation(square, 6))