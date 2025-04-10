"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a == 0 or a == 1 or b == 0:
        ValueError("Invalid Input")
    return math.log(b, a)

def exponent(a, b):
    return a ** b





