#if-else statements

'''traditionally, input takes string values. but to typecast it to only integer we use this method:'''

print("Enter your marks: ")
marks=int(input()) 

if(marks>90 and marks<100):
    grade='A'
elif(marks>70 and marks<90):
    grade='B'
elif(marks<70):
    grade='Fail'
else:
    grade="Wrong input! Place enter valid marks!"
    

print("Your grade is:",grade)
