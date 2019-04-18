Japanese = {"Civic": 0, "gtr": 0, "Supra":0}
JapaneseMods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}
American = {"corvette": 0, "ford":0, "Hennessey":0}
AmericanMods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}
German = {"golf r": 0, "audi r8": 0, "keonigsegg one":0}
print('\nMain Menu')
menu = '     \n Press 1 to start '
carmenu = ("Costumize what car? "
    "\n \n Manufacturers :Japanese   American   German\n "
                    "               Civic      Corvette       Golf R"
                    "\n                GTR        Firsta rs       Audi R8"
                    "\n                Supra      Hennesey       Keonigsegg One"
           )
attributes = (
              "\nTurbo"
              "\nEngine"
              "\nTransmission"
              "\nSuspension"
              "\nExhuast"
             )
money = 100
print("Welcome to Need for Speed!!! \n " 'You have ', money, 'dollars left')
choice = None
print(menu)
while choice != "0":
    choice = input()
    if choice == "1":
        print(carmenu)
        carselection = input()
    if carselection in Japanese or American:
        print('Select what attribute to upgrade to:',carselection, attributes)
        modselection = input()
    if modselection in JapaneseMods:
        print('how much money would you like to spend on the', modselection)
        carupgradevalue = int(input())
        if carupgradevalue <= money:
            JapaneseMods[modselection] += carupgradevalue
            money -= carupgradevalue
        print('You have ', money, ' dollars left')
        print(carselection, JapaneseMods)
        print('Select another car or the same one', carmenu)
    else:
        print("Incorrect value")
