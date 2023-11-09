"Menu"

order=[]

menu_items={"Pizza":"20.65",
            "Spaghetti":"15.49",
            "Risotto":"8.56",
            "Polenta":"11.85",
            "Canederli":"14.88",
            "Arancini":"5.34",
            "Gnocchi":"22.22"
}

menu_list=[]

def menu():
    i=1
    spacer=50*"-"
    spacer1=32*"-"+"|"+"-"*17
    spacer2=28*"-"+"|"+"-"*9+"|"+"-"*11
    print(spacer)
    print(f"Items{' '*27}| Price")
    print(spacer1)
    for item,price in menu_items.items():
        menu_list.append(item)
        numspace=(30-len(item))*" "
        print(f"{i}.{item}{numspace}| ${price}")
        i+=1
    print(spacer)
    i-=1
    place_order=True
    while place_order:
        quantity=0
        menu_selection=input(f"What would you like to add to your order? ")
        if menu_selection.isdigit():
            menu_selection=int(menu_selection)
            if menu_selection<=0 or menu_selection>i:
                print("Please choose the number of an item on the menu. ")
            else:
                item_name=menu_list[menu_selection-1]
                item_price=menu_items[f"{item_name}"]
                quantity=input(f"How many {item_name}s would you like? ")
                if quantity.isdigit():
                    quantity=int(quantity)
                else:
                    quantity=1
                order.append({"Item":f"{item_name}","Price":f"{item_price}","Quantity":quantity})
                keep_ordering=input("Do you want to order something else? (Y) or (N): ")
                while True:
                    match keep_ordering.lower():
                        case "y":
                            place_order=True
                            break
                        case "n":
                            print("Thank you for your order! ")
                            place_order=False
                            break
                        case _:
                            keep_ordering=input("Please enter a valid input. (Y) or (N): ")
        else:
            print("Please choose the number of an item on the menu. ")
    print(spacer)
    print(f"Item{' '*24}| Price   | Quantity")
    print(spacer2)
    for item in order:
        item_name=item["Item"]
        price=item["Price"]
        quantity=f"{item['Quantity']}"
        numspace1=" "*(28-len(item_name))
        numspace2=" "*(7-len(price))
        print(f"{item_name}{numspace1}| ${price}{numspace2}| {quantity}")
    print(spacer)
    item_price_by_quantity_list=[]
    for item in order:
        item_price_by_quantity_list.append(float(item["Price"])*item["Quantity"])
    total_order_price=sum(item_price_by_quantity_list)
    print(f"Your total bill is ${total_order_price:.2f}. ")
    print(spacer)


        




if __name__ == "__main__":
    menu()