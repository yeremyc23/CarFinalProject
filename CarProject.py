Car = {"Honda": 0}
print("Welcome to Need for Speed!!!")
horsepower = 0
money = 100
choice = None
print('     \nMain Menu\n Press 1 to start ')
while choice != "0":
    choice = input()
    if choice =="1":
        print("Welcome! Add horsepower to what car?")
    elif choice in Car:
        Adding = int(input("How much?"))
        if Adding <= money:
            horsepower += Adding
            money -= Adding
        print(horsepower)
    else:
        print("Incorrect")

    print('Your car has', horsepower, 'and your have ', money, 'left')

