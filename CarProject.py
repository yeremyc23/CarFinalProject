#I got this part of the code from https://www.geeksforgeeks.org/python-dictionary-values/ which I learned how to create a dictionary with number values to allow me to add everything up.
Japanese = {"civic": 0, "gtr": 0, "supra":0}
civicmods = {'turbo':40, 'engine':90, 'transmission':35, 'suspension':15,'exhuast':20}
gtrmods = {'turbo':90, 'engine':140, 'transmission':90, 'suspension':50,'exhuast':40}
supramods = {'turbo':110, 'engine':170, 'transmission':80, 'suspension':40,'exhuast':50}
American = {"corvette": 0, "fiesta rs":0, "Hennessey":0}
corvettemods = {'turbo':80, 'engine':120, 'transmission':70, 'suspension':20,'exhuast':30}
fiestamods = {'turbo':40, 'engine':100, 'transmission':70, 'suspension':30,'exhuast':25}
hennesseymods = {'turbo':185, 'engine':250, 'transmission':120, 'suspension':50,'exhuast':100}

print('\n       Main Menu')
menu =('     \n Press 1 to start upgrading ' \
       '     \n Press 2 to downgrade a car '\
       '     \n Press 3 to Finish and View Horsepower ')
menu2 = (
    "\n \n Manufacturers:   Japanese          American\n "
                    "                   Civic           Corvette"
                    "\n                    GTR             Fiesta rs"
                    "\n                    Supra           Hennesey"
           )
attributes = (
              "\nTurbo"
              "\nEngine"
              "\nTransmission"
              "\nSuspension"
              "\nExhuast"
               )
money = 300
print(" Welcome to Need for Speed!!! \n " 'You have ', money, 'dollars left')
choice = None
print(menu)
while choice != "3":
    choice = input('Choice:')
    if choice == "3":
        print("Adding up horsepower---> \n")
#Adding for Japanese cars
    elif choice == "1":
        print("What car would you like to select? \n",menu2)
        carselection = input('Choice:')
        if carselection in Japanese:
            print('Select what attribute to upgrade to:',carselection, attributes)
            modselection = input('Choice:')
            if modselection in civicmods:
                print('how much money would you like to spend on the', modselection)
                carupgradevalue = int(input('Choice:'))
                if carupgradevalue <= money:
                    civicmods[modselection] += carupgradevalue
                    money -= carupgradevalue
                    print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print('You Selected:', carselection,'\nYoure specs are:', civicmods)
                    print('\nSelect another car or the same one', menu)
            elif modselection in gtrmods:
                print('how much money would you like to spend on the', modselection)
                carupgradevalue = int(input('Choice:'))
                if carupgradevalue <= money:
                    gtrmods[modselection] += carupgradevalue
                    money -= carupgradevalue
                    print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, gtrmods)
                    print('Select another car or the same one', menu)
            elif modselection in supramods:
                print('how much money would you like to spend on the', modselection)
                carupgradevalue = int(input('Choice:'))
                if carupgradevalue <= money:
                    supramods[modselection] += carupgradevalue
                    money -= carupgradevalue
                    print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, supramods)
                    print('Select another car or the same one', menu)
            else:
                print("Incorrect value, try again", menu)
        elif carselection in American: #Adding for American cars
                print('Select what attribute to upgrade to:',carselection, attributes)
                modselection = input('Choice:')
                if modselection in corvettemods:
                    print('how much money would you like to spend on the', modselection)
                    carupgradevalue = int(input('Choice:'))
                    if carupgradevalue <= money:
                        corvettemods[modselection] += carupgradevalue
                        money -= carupgradevalue
                        print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                        print(carselection, corvettemods)
                        print('Select another car or the same one', menu)
                elif modselection in fiestamods:
                    print('how much money would you like to spend on the', modselection)
                    carupgradevalue = int(input('Choice:'))
                    if carupgradevalue <= money:
                        fiestamods[modselection] += carupgradevalue
                        money -= carupgradevalue
                        print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                        print(carselection, fiestamods)
                        print('Select another car or the same one', menu)
                elif modselection in hennesseymods:
                    print('how much money would you like to spend on the', modselection)
                    carupgradevalue = int(input('Choice:'))
                    if carupgradevalue <= money:
                        hennesseymods[modselection] += carupgradevalue
                        money -= carupgradevalue
                        print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                        print(carselection, hennesseymods)
                        print('Select another car or the same one', menu)
        else:
            print("Incorrect value, try again", menu)
    elif choice == "2":  #Removing for japanese cars
        print("Which cars mod would you like to downgrade?",menu)
        carselection = input('Choice:')
        if carselection in Japanese:
            print('Select what attribute to remove from',carselection, attributes)
            modselection = input('Choice:')
            if modselection in civicmods:
                print('how much money would you like to remove on the', modselection)
                cardowngradevalue = int(input('Choice:'))
                if cardowngradevalue <= money:
                    civicmods[modselection] -= cardowngradevalue
                    money += cardowngradevalue
                    print('------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, civicmods)
                    print('Select another car or the same one', menu)
            elif modselection in gtrmods:
                print('how much money would you like to remove on the', modselection)
                cardowngradevalue = int(input('Choice:'))
                if cardowngradevalue <= money:
                    gtrmods[modselection] -= cardowngradevalue
                    money += cardowngradevalue
                    print('------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, gtrmods)
                    print('Select another car or the same one', menu)
            elif modselection in supramods:
                print('how much money would you like to remove on the', modselection)
                cardowngradevalue = int(input('Choice:'))
                if cardowngradevalue <= money:
                    supramods[modselection] -= cardowngradevalue
                    money += cardowngradevalue
                    print('------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, supramods)
                    print('Select another car or the same one', menu)
#Removing for American cars
        elif carselection in American:
            print('Select what attribute to remove from',carselection, attributes)
            modselection = input('Choice:')
            if modselection in corvettemods:
                print('how much money would you like to remove on the', modselection)
                cardowngradevalue = int(input('Choice:'))
                if cardowngradevalue <= money:
                    corvettemods[modselection] -= cardowngradevalue
                    money += cardowngradevalue
                    print('------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, corvettemods)
                    print('Select another car or the same one', menu)
            elif modselection in fiestamods:
                print('how much money would you like to remove on the', modselection)
                cardowngradevalue = int(input('Choice:'))
                if cardowngradevalue <= money:
                    fiestamods[modselection] -= cardowngradevalue
                    money += cardowngradevalue
                    print('------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, fiestamods)
                    print('Select another car or the same one', menu)
            elif modselection in hennesseymods:
                print('how much money would you like to remove on the', modselection)
                cardowngradevalue = int(input('Choice:'))
                if cardowngradevalue <= money:
                    hennesseymods[modselection] -= cardowngradevalue
                    money += cardowngradevalue
                    print('------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, hennesseymods)
                    print('Select another car or the same one', menu)
else:
    input("Press enter twice to confirm")
    print("You have", money, "left!")
    if input()=="":
        print('Civic:',sum(civicmods.values()),'---------------------  GTR', sum(gtrmods.values()),'----------------------------  Supra',sum(supramods.values()),'\n')
    for i in civicmods and gtrmods and supramods:
        print(i.title(),'|', civicmods[i],'|','                   ',i.title(),'|', gtrmods[i],'|','                  ',
              i.title(),'|', supramods[i],'|',)

    print('\n \nCorvette',sum(corvettemods.values()),'--------------------  Ford Fiesta',sum(fiestamods.values()),'-----------------  Hennesey',sum(hennesseymods.values()),'\n')
    for e in corvettemods and fiestamods and hennesseymods:
        print(e.title(),'|', corvettemods[e],'|','                   ',e.title(),'|', fiestamods[e],'|','                  ',
              e.title(),'|', hennesseymods[e],'|',)

#I learned this code from StackOverflow(link is at the end), Since I was using dictionary lists which were dfined with values https://stackoverflow.com/questions/3019049/how-do-i-get-the-key-of-an-item-when-doing-a-for-loop-through-a-dictionary-or-li
#I found that the best way to display a manu was with a foor loop which will put everything in order. I found out hoow to print the list and values
