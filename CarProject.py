Japanese = {"Honda": 0, "Nissan": 0}
JapaneseMods = {'suspension': 0, 'engine': 0}
American = {"Corvette": 0}
AmericanMods = {'Suspension':0, 'engine':0}
print('\nMain Menu')
menu = '     \n Press 1 to start '
carmenu = ("Honda, Corevette")
money = 100
print("Welcome to Need for Speed!!! \n " 'You have ', money, 'dollars left')
choice = None
print(menu)
while choice != "0":
    choice = input()
    if choice == "1":
        print("Welcome! \nCostumize what car?")
        carselection = input()
    if carselection in Japanese:
        print('Select what attribute to upgrade to that car: ')
        modselection = input()
    if modselection in JapaneseMods:
        print('how much money would you like to spend on', modselection)
        carupgradevalue = int(input())
        if carupgradevalue <= money:
            JapaneseMods[modselection] += carupgradevalue
            money -= carupgradevalue
        print('You have ', money, ' dollars left')
        print(carselection, JapaneseMods)
    elif carselection in American:
        print('What car would you like to mod in the American Manufacturer', carselection)

    else:
        print("Incorrect value")
