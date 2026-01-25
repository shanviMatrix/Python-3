#loops

#for loops
""" print("How many times you want to execute the loop? : ")
number=int(input())
for i in range (0,number):
    print(i) """
   
""" list1=[[1,2,3], [4,5,6], [7,8,9]]   
#nested for loop
for item in list1:
    for i in item:
        print(i) """
     
#while loops
""" print("Enter a number: ")
number=int(input())
while(number>4):
    if(number==9):
        break
    if(number==8):
        continue
    print("Number is greater than 4.")
    number=int(input())
    print("loop ended") """
    
""" count=1
while count<=10:
    print("WTF!", count)
    count=count+1
print("Loop ended...") """

""" count=5
while count>=1:
    print("Reverse", count)
    count=count-1
print("Loop ended!") """

#Print numbers from 1 to 100.
""" i=1
while i<=100:
    print(i)
    i+=1 """

#Print numbers from 100 to 1.
""" i=100
while i>=1:
    print(i)
    i-=1
 """
 
#Print the multiplication table of any number called n.
""" i=1
n=int(input("Enter a number: "))
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1 """
    
#Print all elements in the list using a while loop.
""" nums=[1,4,9,16,25,36,49,64,81,100]
i=1
while i<=10:
    print(i,"x",i,"=", i*i)
    i+=1 """
    
""" i=0
while i<len(nums):
    print(i,"x",i,"=",nums[i])
    i+=1
     """

#Search for an elements x in the tuple using a loop.
""" nums=(1,4,9,16,25,36,49,64,81,100)
x=81
i=0
while i<len(nums):
    if(nums[i]==x):
        print("Item found at idex", i)
        break
    else:
        print("Finding...")
    i+=1
 """
 
#Continue.
""" i =0 
while i<=10:
    if(i%2==0):
        i+=1
        continue #skip
    print(i)
    i+=1
 """

#For-loop

""" list=[1,2,3,4,5]
tuple=("Google","Microsoft","Accenture","Nvidia")
for value in list:
    print(value)
for company in tuple:
    print(company)
 """
 
""" str="Placementnahihorahi"
for char in str:
    print(char) """
    
""" list=[1,4,9,16,25,36,49,64,81,100]
for num in list:
    print(num) """
    
#Search for an elements x in the tuple using a for loop.
""" tuple=(1,4,9,16,25,36,49,64,81,100)
x=49
index=0
for nums in tuple:
    if (nums==x):
        print("Item found at index", index)
        break
    index+=1
     """
     
#Range(start,stop,step)

""" for i in range(10):
    print(i) """
    
""" for i in range(2,10,2):
    print(i) """
    
""" for i in range(1,101):
    print(i) """
    
""" for i in range(1,11):
    print(i,"x",i,"=",i*i) """
    
""" n=int(input("Enter a number"))
for i in range(1,11):
    print(n,"x",i,"=",n*i) """
    
""" for i in range(5):
    pass
print("Hello") """

#wap to find sum of first n numbers using while loop.
""" n=int(input("Enter the number : "))
i=0
sum=0
while i<=n:
   sum+=i
   i+=1
print("Sum =", sum) """

#wap to find the factorial of first n numbers using for loop.
""" n=int(input("Enter a number: "))
i=1
factorial=1
for i in range(1,n+1):
    factorial*=i
    i+=1
print("Factorial of",n,"is =",factorial)
 """