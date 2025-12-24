# If/Else:
# a. Write a program that asks the user for an integer and prints whether it is even or odd.
# b. Write a program that asks the user for their age and then prints whether they are a child, teenager, adult, or senior.
# (e.g., child: <13, teenager: 13-19, adult: 20-64, senior: 65+)
# c. Write a program that asks the user for two numbers and prints the larger one. If they are equal, print that they are equal.
# d. Write a program that asks the user for a year and prints whether it is a leap year or not.
# e. Write a program that asks the user for a temperature and then asks whether it is in Celsius or Fahrenheit.
# Convert the temperature to the other unit and print the result.

# #a.
# a = int(input("enter an integer:"))
# if a%2==0:
#     print(a,"is even")
# else:
#     print(a,"is odd")


# #b.
# age = int(input("Enter your age: "))

# if age < 13:
#     print("You are a child.")
# elif 13 <= age <= 19:
#     print("You are a teenager.")
# elif 20 <= age <= 64:
#     print("You are an adult.")
# else:
#     print("You are a senior.")


# #c.
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# if a > b:
#     print("The first number is larger.")
# elif b > a:
#     print("The second number is larger.")
# else:
#     print("Both numbers are equal.")

# #d.
# year = int(input("Enter a year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("It is a leap year.")
# else:
#     print("It is not a leap year.")

# #e.
# temp = float(input("Enter the temperature: "))
# unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

# if unit == "C":
#     f = (temp * 9/5) + 32
#     print(f"{temp}°C = {f}°F")
# elif unit == "F":
#     c = (temp - 32) * 5/9
#     print(f"{temp}°F = {c}°C")
# else:
#     print("Invalid unit. Please enter C or F.")

# For loops and range:
# a. Write a program that prints the first 10 natural numbers using a for loop and range.
# b. Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.
# c. Write a program that prints the multiplication table (from 1 to 10) for a given number.
# d. Write a program that prints all the even numbers between 1 and 50 using a for loop and range.
# e. Write a program that asks the user for a string and prints each character of the string on a new line.


# #a.
# for i in range(1, 11):
#     print(i)

# #b.
# n = int(input("Enter n: "))
# s = 0
# for i in range(1, n+1):
#     s = s + i
# print(s)

# #c.
# n = int(input("Enter number: "))
# for i in range(1, 11):
#     print(n, "*", i, "=", n*i)

# #d.
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# #e.
# text = input("Enter text: ")
# for ch in text:
#     print(ch)

# While loops:
# a. Write a program that asks the user for a number and then counts down from that number to 1 using a while loop.
# b. Write a program that asks the user for a number and then keeps asking until the user enters a positive number.
# c. Write a program that simulates a simple guessing game. The program should generate a random number between 1 and 10 and then let the user guess until they get it right.
# d. Write a program that calculates the factorial of a given number using a while loop.
# e. Write a program that asks the user for a series of numbers until they enter 0, and then prints the sum of all the numbers.

# #a.
# n = int(input("Enter a number: "))
# while n >= 1:
#     print(n)
#     n = n - 1

# #b.
# n = int(input("Enter a positive number: "))
# while n <= 0:
#     n = int(input("Please enter a POSITIVE number: "))
# print("Thank you! You entered:", n)

# #c.
# import random

# secret = random.randint(1, 10)

# guess = int(input("Guess the number (1-10): "))
# while guess != secret:
#     guess = int(input("Wrong! Try again: "))

# print("Correct! The number was", secret)

# #d.
# n = int(input("Enter a number: "))
# fact = 1

# while n > 0:
#     fact = fact * n
#     n = n - 1

# print("Factorial is:", fact)

# #e.
# total = 0
# n = int(input("Enter a number (0 to stop): "))

# while n != 0:
#     total = total + n
#     n = int(input("Enter another number (0 to stop): "))

# print("Sum is:", total)
