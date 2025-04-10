#https://github.com/DanielAPerez20/lab10-DP-WC
# will crotty
# daniel perez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError("Invalid Input")

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    return math.log(b, a)

def exponent(a, b):
    return a ** b


def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return b / a   # raise ZeroDivisionError if a == 0


def log(a, b):
    return math.log(b, a)


def exp(a, b): return a ** b





