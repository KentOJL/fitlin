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
    print("_" * 40)
    print("Welcome to Razer Mouse Shop")
    print("_" * 40)
    print("""\n1. Show All Products
            \n2. Sales
            \n3. Add Products
            \n4. Remove Products
            \n5. Exit""")
    print("_" * 40)



def display_all():
    print("SNO\tProduct\t\t\t\tIn Stock\tPrice")
    for item in all_products:
        print("{0}\t{1}\t\t{2}\t\t{3}".format(item[0], item[1], item[2], item[3]))



def order_summary(product, price):
    print("-" * 40)
    print("\t\tRazer Mouse Shop")
    print("-" * 40)
    print("Order Summary\tDate:{}".format(str(datetime.now())))
    for i in range(len(product)):
        print("Product Name: {}".format(i))
    print("Price: {}".format(price))
    print("-" * 40)
    print("\t\tTotal Payment Amount: {}".format(item[-1]))



def generate_bill(product, price, lst):
    print("-" * 40)
    print("\t\tRazer Mouse Shop")
    print("-" * 40)
    print("Bill:{} \tDate:{}".format(int(random.random()*100000), str(datetime.now())))
    print("Product name\t\tprice")
    print("-" * 40)
    for j in range(len(lst)):
        print("{}\t\tRM{}".format(j , item[-1]))
    print("-" * 40)
    print("\t\tTotal Bill Amount: {}".format(price))



while(True):
    banner()
    choice = int(input("Please enter your option: "))
    if choice == 1:
        display_all()
    elif choice == 2:
        display_all()
        print("Press 0 for payment")
        item_lst = []
        total_price = 0
        prod_id = int(input("Enter the Product ID: "))
        while prod_id != 0:
            prod_id = int(input("Enter the Product ID: "))
            for item in all_products:
                if item[0] == prod_id:
                    item_lst.append(item[0])
                    total_price = total_price + item[2]
                    if item[1] == 0:
                        print("Sorry we are out of stock")
                    else:
                        item[1] -= 1
                    
                member = input("Do you have membership(Y/N): ")
                if member == "Y":
                    total_price * 0.9
                    generate_bill(item, total_price, item_lst)
                    print("Thanks For shopping with Us")
                    sys.exit(0)
                else:
                    print("Continue Shopping")
    elif choice == 3:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            prod = []
            prod.append(len(all_products)+1)
            prod.append(input("Enter the Product Name: "))
            prod.append(int(input("Quantity: ")))
            prod.append(int(input("Price: ")))
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