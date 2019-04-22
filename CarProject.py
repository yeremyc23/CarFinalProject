#I got this part of the code from https://www.geeksforgeeks.org/python-dictionary-values/ which I learned how to create a dictionary with number values to allow me to add everything up.
Japanese = {"civic": 0, "gtr": 0, "supra":0}
civicmods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}
gtrmods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}
supramods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}
American = {"corvette": 0, "fiesta rs":0, "Hennessey":0}
corvettemods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}
fiestamods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}
hennesseymods = {'turbo':0, 'engine':0, 'transmission':0, 'suspension':0,'exhuast':0}

print('\nMain Menu')
menu =('     \n Press 1 to start upgrading ' \
       '     \n Press 2 to downgrade a car '\
       '     \n Press 3 to Finish and View Horsepower ')
carmenu = (
    "\n \n Manufacturers :Japanese   American   German\n "
                    "               Civic      Corvette"
                    "\n                GTR        Fiesta rs"
                    "\n                Supra      Hennesey"
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
while choice != "3":
    choice = input()
    if choice == "3":
        print("Adding up horsepower \n")

    elif choice == "1":
        print("What car would you like to select? \n",carmenu)
        carselection = input()
        if carselection in Japanese:
            print('Select what attribute to upgrade to:',carselection, attributes)
            modselection = input()
            if modselection in civicmods:
                print('how much money would you like to spend on the', modselection)
                carupgradevalue = int(input())
                if carupgradevalue <= money:
                    civicmods[modselection] += carupgradevalue
                    money -= carupgradevalue
                    print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print('You Selected:', carselection,'\nYoure specs are:', civicmods)
                    print('\nSelect another car or the same one', carmenu)
            elif modselection in gtrmods:
                print('how much money would you like to spend on the', modselection)
                carupgradevalue = int(input())
                if carupgradevalue <= money:
                    gtrmods[modselection] += carupgradevalue
                    money -= carupgradevalue
                    print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, gtrmods)
                    print('Select another car or the same one', carmenu)
            elif modselection in supramods:
                print('how much money would you like to spend on the', modselection)
                carupgradevalue = int(input())
                if carupgradevalue <= money:
                    supramods[modselection] += carupgradevalue
                    money -= carupgradevalue
                    print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                    print(carselection, supramods)
                    print('Select another car or the same one', carmenu)

        elif carselection in American:
                print('Select what attribute to upgrade to:',carselection, attributes)
                modselection = input()
                if modselection in corvettemods:
                    print('how much money would you like to spend on the', modselection)
                    carupgradevalue = int(input())
                    if carupgradevalue <= money:
                        corvettemods[modselection] += carupgradevalue
                        money -= carupgradevalue
                        print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                        print(carselection, corvettemods)
                        print('Select another car or the same one', carmenu)
                elif modselection in fiestamods:
                    print('how much money would you like to spend on the', modselection)
                    carupgradevalue = int(input())
                    if carupgradevalue <= money:
                        fiestamods[modselection] += carupgradevalue
                        money -= carupgradevalue
                        print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                        print(carselection, fiestamods)
                        print('Select another car or the same one', carmenu)
                elif modselection in hennesseymods:
                    print('how much money would you like to spend on the', modselection)
                    carupgradevalue = int(input())
                    if carupgradevalue <= money:
                        hennesseymods[modselection] += carupgradevalue
                        money -= carupgradevalue
                        print('-----------------------------' "\n"'You have ', money, ' dollars left''\n''-----------------------------')
                        print(carselection, hennesseymods)
                        print('Select another car or the same one', carmenu)
                else:
                    print("Incorrect value, try again")
else:
            input("Are you sure?")
if input()=="":
    print('civic mods----------------------GTR Mods----------------------------Supra Mods\n')
    for i in civicmods and gtrmods and supramods:
        print(i.title(),'|', civicmods[i],'|','                   ',i.title(),'|', gtrmods[i],'|','                  ',
              i.title(),'|', supramods[i],'|',)

    print('\n \nCorvette mods----------------------Fiesta Mods----------------------------Hennesey Mods\n')
    for e in corvettemods and fiestamods and hennesseymods:
        print(e.title(),'|', corvettemods[e],'|','                   ',e.title(),'|', fiestamods[e],'|','                  ',
              e.title(),'|', hennesseymods[e],'|',)

#I learned this code from StackOverflow(link is at the end), Since I was using dictionary lists which were dfined with values https://stackoverflow.com/questions/3019049/how-do-i-get-the-key-of-an-item-when-doing-a-for-loop-through-a-dictionary-or-li
#I found that the best way to display a manu was with a foor loop which will put everything in order. I found out hoow to print the list and values
#Also I got something else from stackoverflow that allowed me to sum up all the values in the dictionary from https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary
