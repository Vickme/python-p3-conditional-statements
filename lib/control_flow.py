#!/usr/bin/env python3

def admin_login(username, password):
    # Check if the username is "admin" or "ADMIN" and the password is "12345"
    if (username.lower() == "admin" or username.upper() == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

# Example usage:
username_input = input("Enter username: ")
password_input = input("Enter password: ")

result = admin_login(username_input, password_input)
print(result)



def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 65:
        return "It's a little chilly out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operator, num1, num2):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        else:
            print("Invalid operation!")
            return None
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None