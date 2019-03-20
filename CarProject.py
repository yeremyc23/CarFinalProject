def race():
    print("Welcome to Need for Speed!!!")
    print('\n      Main Menu')
    i = 0
    while i != 99:
        i = int(input('\nStart Game press "1" \n Quit press "0"'))
        if i == 0:
            print("Goodbye")
        elif i == 1:
            choice = int(input('\nSelect a Manufacturer'));
        else:
            print("\nThat's not a value")
race()
