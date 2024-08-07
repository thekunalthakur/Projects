menu= {
    'Pizza':80,
    'Burger':60,
    'Pasta':60,
    'Cold Coffee':50,
    'Tea':20
}


print("Welcome to Restauresnt")
print("Pizza: 80\nBurger: 60\nPasta: 60\nCold Coffee: 50\nTea: 20")

Order_Total=0

while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        Order_Total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {Order_Total} Rs")

