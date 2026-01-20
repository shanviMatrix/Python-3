#loops

#for loops
print("How many times you want to execute the loop? : ")
number=int(input())
for i in range (0,number):
    print(i)
   
list1=[[1,2,3], [4,5,6], [7,8,9]]   
#nested for loop
for item in list1:
    for i in item:
        print(i)
        
        
#while loops
print("Enter a number: ")
number=int(input())
while(number>4):
    if(number==9):
        break
    if(number==8):
        continue
    print("Number is greater than 4.")
    number=int(input())
    print("loop ended")