# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "banana", "orange", "mango"]

# TODO: Add a fruit to the end of the list
fruits.append("pineapple")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "strawberry")

# TODO: Remove a fruit from the list
fruits.remove("banana")  # removes banana

# TODO: Print the modified list
print("Question 1 - Modified fruits list:", fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# TODO: Create a new list with each number squared
squared_numbers = [num ** 2 for num in numbers]

# TODO: Find the sum and average of the original numbers
total = sum(numbers)
average = total / len(numbers)

# TODO: Print the results
print("\nQuestion 2:")
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Sum:", total)
print("Average:", average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals = {
    "South Africa": "Pretoria",
    "USA": "Washington",
    "France": "Paris"
}

# TODO: Add a new country-capital pair
countries_capitals["Japan"] = "Tokyo"

# TODO: Update the capital of an existing country
countries_capitals["South Africa"] = "Cape Town"

# TODO: Remove a country-capital pair
countries_capitals.pop("USA")

# TODO: Print the modified dictionary
print("\nQuestion 3 - Modified countries_capitals:", countries_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grape": "purple"
}

# TODO: Print all the fruits (keys)
print("\nQuestion 4:")
print("Fruits (keys):", list(fruit_colors.keys()))

# TODO: Print all the colors (values)
print("Colors (values):", list(fruit_colors.values()))

# TODO: Print each fruit and its color
print("Fruit and color pairs:")
for fruit, color in fruit_colors.items():
    print(f"  {fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color
check_fruit = "apple"
if check_fruit in fruit_colors:
    print(f"\n{check_fruit} is in dictionary, its color is {fruit_colors[check_fruit]}")
else:
    print(f"{check_fruit} not found")
