a = int(input("Enter your first number: \n"))
b = int(input("Enter your second number: \n"))
if ((a%2==0) and (b%2==0)) or ((a%3==0) and (b%3==0)):
    print(a*b)
else:
    print(a+b)