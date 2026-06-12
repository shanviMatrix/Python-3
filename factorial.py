n=int(input("Enter a number whose factorial you want to print: "))
fact=1
i=1

while i<=n:
    fact=fact*i
    i=i+1

print("factorial =", fact)