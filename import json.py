import json
from datetime import datetime
import random
import sys

with open('menu.json', 'r') as f:
    data = json.load(f)

def banner():
    print("_" * 60)
    print("\nWelcome to Razer Mouse Shop")
    print("_" * 60)
    print("""\n1. Show All Products
            \n2. Sales
            \n3. Add Products
            \n4. Remove Products
            \n5. Update Products
            \n6. Exit""")
    print("_" * 60)



def display_all():
    print("SNO\tProduct\t\t\t\tIn Stock\tPrice")
    for item in items:
        print("\n{0}\t{1}\t\t{2}\t\t{3:.2f}".format(item.get('id'), item.get('name'), item.get('quantity'), item.get('price')))



def order_summary(product, price , total , q_lst):
    print("-" * 60)
    print("\t\tRazer Mouse Shop")
    print("-" * 60)
    print("Order Summary\t\tDate:{}".format(str(datetime.now())))
    print(" ")
    print("Product name\t\t\tQuantity\tPrice")
    print("-" * 60)
    for j in range(len(product)):
        print("{}\t\t  {}\t\tRM {:.2f}".format(product[j] , q_lst[j] ,price[j] ))
    print("-" * 60)
    print("Total Payment Amount:\t\t\t\tRM {:.2f}".format(total))



def generate_bill(total, lst , price , q_lst , Change , amt_received):
    print("-" * 60)
    print("\n\tRazer Mouse Shop")
    print("-" * 60)
    print("Bill:{} \t\tDate:{}".format(int(random.random()*100000), str(datetime.now())))
    print(" ")
    print("Product name\t\t\tQuantity\tPrice")
    print("-" * 60)
    for j in range(len(lst)):
        print("{}\t\t  {}\t\tRM {:.2f}".format(lst[j] , q_lst[j] ,price[j] ))
    print("-" * 60)
    print("Total Bill Amount:\t\t\t\tRM {:.2f}".format(total))
    print("  Amount Received:\t\t\t\tRM {:.2f}".format(amt_received))
    print("           Change:\t\t\t\tRM {:.2f}".format(Change))



items = data.get('items', [])
while True:
    banner()
    choice = int(input("Please enter your option: "))

    if choice == 1:
        display_all()

    elif choice == 2:
        ordered_items = {}
        order_items = 999
        item_lst = []
        amount_lst = []
        quantity_lst = []
        display_all()
        total_bill = 0
        while order_items != 0:
            order_items = list(map(int, input('What you want to buy today? ').split(',')))
            for order_item in order_items:
                for item in items:
                    if item['id'] == order_item:
                        quant = int(input("Please enter the quantity: "))
                        ordered_items[order_item] = item
                        ordered_items[order_item]['quantity'] -= 1
                        break
            for item in ordered_items:
                name = ordered_items[item]['name']
                price = ordered_items[item]['price']
                amount = price * quant
                quantity_lst.append(quant)
                item_lst.append(name)
                amount_lst.append(amount)
                total_bill += amount

        order_summary(item_lst , amount_lst , total_bill , quantity_lst) 
        conf = input('Please confirm Your Order(Y/N): ')
        if conf == "Y":
            member = input("Do you have membership(Y/N): ")
            if member == "Y":
                total_bill = total_bill * 0.9
                payment = float(input("Amount Received: "))
                change = payment - total_bill
                generate_bill(total_bill , item_lst , amount_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thank you for shopping with Us :)")
                sys.exit(0)

            else:
                payment = float(input("Amount Received: "))
                change = payment - total_bill
                generate_bill(total_bill , item_lst , amount_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thank you for shopping with Us :)")
                sys.exit(0)
        else:
            print("Continue Exploring the shop")

    elif choice == 3:
        name = input('Enter item name: ')
        item_price = int(input('Enter the price: '))
        item_quantity = int(input("Enter the quantity: "))
        items.append({
            'id': len(items) + 1, 
            'name': name,
            'price': item_price,
            'quantity': item_quantity
        })

        data['items'] = items
        with open('menu.json', 'w') as f:
            json.dump(data, f)
        print('Item is added.')

    elif choice == 4:
        

    else:
        data['items'] = items
        with open('menu.json', 'w') as f:
            json.dump(data, f)
        print('Thank you')
        break