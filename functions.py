#functions

import math

def average(num1,num2):
    return (num1+num2)/2

print(int(average(8,10)))

# Functions for calculating areas
def area_of_square(side):
    return side * side

def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_circle(radius):
    return math.pi * radius * radius

# Testing all functions
print("Area of square (side=5):", area_of_square(5))
print("Area of rectangle (length=10, breadth=6):", area_of_rectangle(10, 6))
print("Area of circle (radius=7):", int(area_of_circle(7)))


