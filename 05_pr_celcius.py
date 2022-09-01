list = [1, 2, 3]
print("options are :", list)
choice = int(input("Enter your choice :"))
if choice is 1:
    num = int(input("Enter the temperature :"))
    f = (9*num + 160)/5
    print(f"{num} Celcius is equivalent to {f} Farenheit")
elif choice is 2:
    num = int(input("Enter the temperature :"))
    c = (5*num - 160)/9
    print(f"{num} Farenheit is equivalent to {c} Celcius ")
elif choice is 3:
    print("Quit")