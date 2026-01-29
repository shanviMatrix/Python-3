#functions
"""A function is a block of statements that perform a specific task."""

""" import math

def average(num1,num2):
    return (num1+num2)/2

print(int(average(8,10))) """

# Functions for calculating areas
""" def area_of_square(side):
    return side * side

def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_circle(radius):
    return math.pi * radius * radius """

# Testing all functions
""" print("Area of square (side=5):", area_of_square(5))
print("Area of rectangle (length=10, breadth=6):", area_of_rectangle(10, 6))
print("Area of circle (radius=7):", int(area_of_circle(7)))
 """

#Calculate basic sum. 
""" def calc_sum(a,b):
    return a+b

sum=calc_sum(5,1)  
print(sum)
 """

#Greet.
""" def greet():
    print("Hello")
    
greet() """

#Avg of 3 nums.
""" def avg(a,b,c):
    sum=a+b+c
    average=sum/3
    print(average)
    return average

avg(2,4,6)
avg(10,20,30) """

# func to print length of list (List is the parameter). Also, print the items in the list with their index number.
""" juice=["tropicana","maaza","real","frooti","appy"]
beverage=["coffee","macchiato","tea","green tea","kaadha"]

def printLen(list):
    print(len(list))
 
def printList(list):
    for items in list:
        print(items,end=" ")
        
printList(juice)
printList(beverage)
printLen(juice)
printLen(beverage) """

#function to calculte the factorial of n (n is parameter).
""" def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

factorial(6) """

#function to convert USD to INR.
""" def usd_inr(n):
    inr=n*90
    print(n,"dollars =",inr, "rupees")
    
usd_inr(10) """

#function to take input n and print if it is odd or even.
def even_odd(n):
    if n%2==0:
        print("Even!")
    else:
        print("Odd!")
    
even_odd(82)
