def add_drink_type():
    description=input("Enter description of drink:")
    price=input("Enter price:$")
    check=price.replace('.','')
    while check.isdigit()==False:
        print("Please enter a suitable price!")
        price=input("Enter price:$")
        check=price.replace('.','')
    else:
        price=float(price)
    quantity=input("Enter quantity:")
    while quantity.isdigit()==False:
        print("Please enter a suitable quantity!")
        quantity=input("Enter quantity:")
    else:
        quantity=int(quantity)
    new_drink={'description':description,'price':price,'quantity':quantity}
    return new_drink

def replenish_drink(drink_id,drinks):
    replenish=drinks.get(drink_id)
    current=replenish.get('quantity')
    if current<5:
        replenish_quantity=int(input("Enter quantity:"))
        replenish['quantity']=current+replenish_quantity
        print(replenish.get('description')," has been top up!")
    else:
        print("No need to replenish. Quantity is greater than 5.")
    return replenish




