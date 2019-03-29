Car = {"Honda": 0}
print("Welcome to Need for Speed!!!")
horsepower = 0
money = 100
choice = None
print('Main Menu')
while choice != "0":
    choice = input("Add horsepower to what car?")
    if choice == "0":
        print("Quitted Game")
    elif choice in Car:
        inputs = int(input("How much?"))
    else:
        print("Incorrect input")

    print(horsepower)

