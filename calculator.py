"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a): 
    try:
        math.sqrt(a)
    except:
        raise ValueError("Invalid Input")   

def hypotenuse(a, b): 
    return math.hypot(a, b) # can have negative nums

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

>>>>>>> 799110f7afcee380f30f7a87e067c0bf969677a4




