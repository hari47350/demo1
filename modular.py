# Modular code means writing a program in independent, reusable pieces (modules) instead of one big block of code.
# uses ->maintainability,reuseablility 

# # All logic mixed together
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# choice = input("Add or Multiply? ")

# if choice == "Add":
#     print("Result:", num1 + num2)
# elif choice == "Multiply":
#     print("Result:", num1 * num2)

# main.py
from calc import add, multiply

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("add or multiply? ")

if choice == "add":
    print("Result:", add(num1, num2))
elif choice == "multiply":
    print("Result:", multiply(num1, num2))

