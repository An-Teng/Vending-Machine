vendor = input("Are you a vendor (Y/N)?")
drinks = ["IM", "HM", "IC", "HC", "1p", "CC"]
count=0
cost=0
vendor = vendor.upper()
repay=True
cont=True
while cont==True:
    if vendor == 'N':
        print("Welcome to ABC Vending Machine.")
        print("Select from following choices to continue:")
        print("IM. Iced Milo (S$1.5)", "HM. Hot Milo (S$1.2)", "IC. Iced Coffee (S$1.5)", "HC. Hot Coffee (S$1.2)",
              "1P. 100 Plus (S$1.1)", "CC. Coca Cola (S$1.3)", "0. Exit / Payment", sep="\n")
        choice = 1
        while choice !='0':
            choice = input("Enter choice:")
            choice=choice.upper()
            if choice in drinks:
                if choice=='IM' or choice=='IC':
                    cost+=1.50
                    count+=1
                elif choice=='HM' or choice=='HC':
                    cost+=1.20
                    count+=1
                elif choice=='1P':
                    cost+=1.10
                    count+=1
                else:
                    cost+=1.30
                    count+=1
            elif choice=='0':
                break
            else:
                print("Invalid option")
            print("No. of drinks selected =",count)
        print("please pay:%.2f" %(cost))
        while repay==True:
            if count!=0:
                money=0
                change=0
                print("Indicate your payment:")
                ten=int(input("Enter no. of $10 notes:"))
                money+=ten*10
                if money<cost:
                    five=int(input("Enter no. of $5 notes:"))
                    money+=five*5
                    if money<cost:
                        two=int(input("Enter no. of $2 notes:"))
                        money+=two*2
                        if money<cost:
                            print("Not enough to pay for drinks","Take back your cash!",sep="\n")
                            pay=input("Do you want to cancel the Purchases? Y/N:")
                            if pay=='Y':
                                repay=False
                                carry_on = input("Do you want to continue? Y/N")
                                if carry_on == 'Y':
                                    cont=True
                                    vendor = input("Are you a vendor (Y/N)?")
                                else:
                                    cont=False
                            else:
                                repay=True
                if money>cost:
                    change=money-cost
                    print("please collect your change:$%.2f" %(change))
                    print("Drinks paid. Thank you.")
                    carry_on = input("Do you want to continue? Y/N")
                    if carry_on == 'Y':
                        cont=True
                        vendor = input("Are you a vendor (Y/N)?")
                        break
                    else:
                        cont=False
                        break
    if vendor=='Y':
        print("Welcome to ABC Vending Machine.")
        print("Select from following choices to continue:")
        print("1. Add Drink Type","2. Replenish Drink","0. Exit", sep="\n")
        choice=input("Enter choice:")
        if choice=='0':
            cont=False











