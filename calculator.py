# 5 function calculator
# river

# add ur import statements
import random
import math

# global variables
A = 5
B = 7

# function/procedure definition statements
def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def mult(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    result = num1 / num2
    return result

def pyth(num1, num2):
    result = math.sqrt((num1**2 + num2**2))
    return result

def quad(num1, num2, num3):
    disc = num2**2 - 4*num1*num3
    if disc < 0:
        return "no real solutions"
    else:
        root1 = (-num2 + math.sqrt(disc)) / (2 * num1)
        root2 = (-num2 - math.sqrt(disc)) / (2 * num1)
        result = f"{root1} and {root2}"
        return result


# body of the program
input1 = int(input("first number: "))
input2 = int(input("second number: "))
input3 = input("third number (write skip to skip): ")
if input3 != "skip":
    input3 = int(input3)

# call statement
print("add: ", add(input1, input2))
print("subtract: ", subtract(input1, input2))
print("mult: ", mult(input1, input2))
print("div: ", div(input1, input2))
print("pyth: ", pyth(input1, input2))
if input3 != "skip":
    print("quad: ", quad(input1, input2, input3))