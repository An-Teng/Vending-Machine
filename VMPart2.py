vendor = input("Are you a vendor (Y/N)?")
drinks = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 20},
          'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 20},
          'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 2},
          'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0},
          '1p': {'description': '100 Plus', 'price': 1.1, 'quantity': 50},
          'CC': {'description': 'Coca cola', 'price': 1.3, 'quantity': 50},
          'JT': {'description': 'Jasmine Tea', 'price': 1.2, 'quantity': 50}}
back_up=drinks
vendor = vendor.upper()
repay = True
cont=True
while cont==True:
    if vendor == 'N':
        choice = 1
        cost=0
        count=0
        while choice != '0':
            print("Welcome to ABC Vending Machine.")
            print("Select from following choices to continue:")
            for key, value in drinks.items():
                description = value.get('description')
                price = value.get('price')
                quantity = value.get('quantity')
                if quantity == 0:
                    print("%s. %s (S$%s) *** Out of Stock ***" % (key, description, price))
                else:
                    print("%s. %s (S$%s) Qty:%s" % (key, description, price, quantity))
            print("0. Exit/Payment")
            choice = input("Enter choice:")
            choice=choice.upper()
            if choice in drinks:
                drink = drinks.get(choice)
                if drink['quantity'] == 0:
                    print(drink['description'], " is out of stock")
                    continue
                drink['quantity'] += -1
                cost += drink['price']
                drinks[choice] = drink
                count += 1
            elif choice == '0':
                break
            else:
                print("Invalid option")
            print("No. of drinks selected =", count)
        print("please pay:$%.2f" % (cost))
        while repay == True:
            if count != 0:
                money = 0
                change = 0
                print("Indicate your payment")
                ten = int(input("Enter no. of $10 notes:"))
                money += ten * 10
                if money < cost:
                    five = int(input("Enter no. of $5 notes:"))
                    money += five * 5
                    if money < cost:
                        two = int(input("Enter no. of $2 notes:"))
                        money += two * 2
                        if money < cost:
                            print("Not enough to pay for drinks", "Take back your cash!", sep="\n")
                            pay = input("Do you want to cancel the Purchases? Y/N:")
                            if pay == 'Y':
                                repay = False
                                drinks=back_up
                                carry_on = input("Do you want to continue? Y/N")
                                if carry_on == 'Y':
                                    cont=True
                                    vendor = input("Are you a vendor (Y/N)?")
                                else:
                                    cont=False
                            else:
                                repay = True
                if money > cost:
                    change = money - cost
                    print("please collect your change:$%.2f" % (change))
                    print("Drinks paid. Thank you.")
                    carry_on = input("Do you want to continue? Y/N")
                    if carry_on == 'Y':
                        vendor = input("Are you a vendor (Y/N)?")
                        cont=True
                        break
                    else:
                        cont=False
                        break
    if vendor=='Y':
        import vendor
        print("Welcome to ABC Vending Machine.")
        print("Select from following choices to continue:")
        print("1. Add Drink Type", "2. Replenish Drink", "0. Exit", sep="\n")
        option = int(input("Enter choice:"))
        while option == 1:
            drink_id = input("Enter drink id:")
            while drink_id in drinks:
                print("drink id exists!.")
                drink_id = input("Enter drink id:")
            else:
                new_drink = vendor.add_drink_type()
                drinks[drink_id] = new_drink
                print("drink have been added")
            option = int(input("Enter choice:"))
        while option == 2:
            for key, value in drinks.items():
                description = value.get('description')
                price = value.get('price')
                quantity = value.get('quantity')
                if quantity == 0:
                    print("%s. %s (S$%s) *** Out of Stock ***" % (key, description, price))
                else:
                    print("%s. %s (S$%s) Qty:%s" % (key, description, price, quantity))
            replenish_drink = input("Enter drink id:")
            while replenish_drink not in drinks:
                print("No drink with this drink id. Try again.")
                replenish_drink = input("Enter drink id:")
            replenish = vendor.replenish_drink(replenish_drink, drinks)
            drinks[replenish_drink] = replenish
            option = int(input("Enter Choice:"))
        if option==0:
            carry_on = input("Do you want to continue? Y/N")
            if carry_on == 'Y':
                cont=True
                vendor = input("Are you a vendor (Y/N)?")
            else:
                cont=False
