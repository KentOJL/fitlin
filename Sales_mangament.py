from datetime import datetime
import random
import sys

all_products = [
    [1, "Razer Deathadder V2 Pro" , 100, 349.00], 
    [2, "Razer Viper Ultimate",  105, 419.00], 
    [3, "Razer Basilink Ultimate" , 35, 599.00], 
    [4, "Razer Viper mini", 295, 139.00], 
    [5, "Razer Deathadder X", 592, 76.90]
]

def banner():
    print("_" * 60)
    print("\nWelcome to Razer Mouse Shop")
    print("_" * 60)
    print("""\n1. Show All Products
            \n2. Sales
            \n3. Add Products
            \n4. Remove Products
            \n5. Exit""")
    print("_" * 60)



def display_all():
    print("SNO\tProduct\t\t\t\tIn Stock\tPrice")
    for item in all_products:
        print("\n{0}\t{1}\t\t{2}\t\t{3:.2f}".format(item[0], item[1], item[2], item[3]))



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



def generate_bill(product, total, lst , price , q_lst , Change , amt_received):
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




while(True):
    banner()
    choice = int(input("Please enter your option: "))
    if choice == 1:
        display_all()
    elif choice == 2:
        display_all()
        print("Press 0 for payment")
        item_lst = []
        price_lst = []
        quantity_lst = []
        total_price = 0
        prod_id = 999
        while prod_id != 0:
            prod_id = int(input("Enter the Product ID: "))
            for item in all_products:
                if item[0] == prod_id:
                    quantity = int(input("Please enter the quantity: "))
                    item_lst.append(item[1])
                    quantity_lst.append(quantity)
                    price_q = item[3] * quantity
                    price_lst.append(price_q)
                    total_price = total_price + price_q
                    if item[2] == 0:
                        print("Sorry we are out of stock")
                    else:
                        item[2] -= 1
        order_summary(item_lst , price_lst , total_price , quantity_lst)
        print(" ")
        conf = input("Please confirm your order(Y/N): ")
        if conf == "Y":
            member = input("Do you have membership(Y/N): ")
            if member == "Y":
                total_price = total_price * 0.9
                payment = float(input("Amount received: "))
                change = payment - total_price
                generate_bill(item, total_price, item_lst , price_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thanks For shopping with Us :)")
                sys.exit(0)
            else:
                payment = float(input("Amount received: "))
                change = payment - total_price
                generate_bill(item, total_price, item_lst , price_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thanks For shopping with Us :)")
                sys.exit(0)
        else:
            print("Continue Exploring the shop")
    
    elif choice == 3:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            prod = []
            prod.append(len(all_products)+1)
            prod.append(input("Enter the Product Name: "))
            prod.append(int(input("Quantity: ")))
            prod.append(float(input("Price: ")))
            all_products.append(prod)
        else:
            print("Incorrect username and password")
    elif choice == 4:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            del_prod = int(input("Enter the product id which you want to delete: "))
            del(all_products[del_prod - 1])
        else:
            print("Incorrect username and password")
    else:
        print("GoodBye!!")
        break
