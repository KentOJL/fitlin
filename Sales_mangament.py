from datetime import datetime
import random
import sys


#To store all products into a double list
all_products = [line.strip().split(',') for line in open('razershop.txt','r').readlines()]


#banner for the customer to know what they want
def banner():
    print("_" * 80)
    print("\nWelcome to Razer Mouse Shop")
    print("_" * 80)
    print("""\n1. Show All Products
            \n2. Sales
            \n3. Add Products
            \n4. Remove Products
            \n5. Exit""")
    print("_" * 80)


#Display all the products on the screen
def display_all():
    print("SNO\t Product \t\t\t\t  Price\t\t\tIn Stock")
    for item in all_products:
        print("\n{0}\t{1} \t\t\t {2}\t\t{3}".format(item[0], item[1], item[2], item[3]))


#Display the order summary to the customer
def order_summary(product, price , total , q_lst):
    print("-" * 80)
    title = "Razer Mouse Shop"
    x = title.center(80)
    print(x)
    print("-" * 80)
    print("Order Summary\t\t\t\t\tDate:{}".format(str(datetime.now())))
    print(" ")
    print("Product name\t\t\tQuantity\tPrice")
    print("-" * 80)
    for j in range(len(product)):
        print("{}\t\t  {}\t\tRM {:.2f}".format(product[j] , q_lst[j] ,price[j] ))
    print("-" * 80)
    print("Total Payment Amount:\t\t\t\tRM {:.2f}".format(total))


#Display the order summary after the member discount
def member_summary(product, price , total , q_lst):
    print("-" * 80)
    title = "Razer Mouse Shop"
    x = title.center(80)
    print(x)
    print("-" * 80)
    print("Order Summary\t\tDate:{}".format(str(datetime.now())))
    print(" ")
    print("Product name\t\t\tQuantity\tPrice")
    print("-" * 80)
    for j in range(len(product)):
        print("{}\t\t  {}\t\tRM {:.2f}".format(product[j] , q_lst[j] ,price[j] ))
    print("-" * 80)
    print("Total Payment Amount:\t\t\t\tRM {:.2f}".format(total))


#Generate the bill for the customer
def generate_bill(product, total, lst , price , q_lst , Change , amt_received):
    print("-" * 80)
    title = "Razer Mouse Shop"
    x = title.center(80)
    print(x)
    print("-" * 80)
    print("Bill:{} \t\tDate:{}".format(int(random.random()*100000), str(datetime.now())))
    print(" ")
    print("Product name\t\t\tQuantity\tPrice")
    print("-" * 80)
    for j in range(len(lst)):
        print("{}\t\t  {}\t\tRM {:.2f}".format(lst[j] , q_lst[j] ,price[j] ))
    print("-" * 80)
    print("Total Bill Amount:\t\t\t\tRM {:.2f}".format(total))
    print("  Amount Received:\t\t\t\tRM {:.2f}".format(amt_received))
    print("           Change:\t\t\t\tRM {:.2f}".format(Change))


#Decrease the item from the text file after customer buy it
def decrement_item(item_id, quantity):
    new_all_products = [line.strip().split(',') for line in open('razershop.txt','r').readlines()]

    quant = quantity
    ids = str(item_id)
    for line in new_all_products:
        if line[0] == ids:
            if int(line[3]) >= quant:
                line[3] = int(line[3])-quant

            else:
                print("Sorry insufficient stock, you can only buy" , line[3] , 'of this stock.')

    with open('razershop.txt' , 'w') as f:        
        for line in new_all_products:
            f.write("%s,%s, %s   ,   %s\n" %(line[0].strip() , line[1].strip() , line[2].strip() , line[3].strip()))






while(True):
    banner()
    choice = int(input("Please enter your option: "))

    #if customer choice is see all the products in the shop
    if choice == 1:
        display_all()

    #if customer choice is buy things    
    elif choice == 2:
        display_all()
        print("Press 0 for payment")
        item_lst = []
        price_lst = []
        quantity_lst = []
        total_price = 0
        prod_id = 999 #make it a number so it can continue until 0 is enter
        while prod_id != 0:
            prod_id = int(input("Enter the Product ID: "))
            for item in all_products:
                if int(item[0]) == prod_id:
                    quantity = int(input("Please enter the quantity: "))
                    #add all the item, quantity, and price of the item to the list for the use of printing bill
                    item_lst.append(item[1])
                    quantity_lst.append(quantity)
                    price_q = float(item[2]) * quantity
                    price_lst.append(price_q)
                    total_price = total_price + price_q
                    decrement_item(prod_id , quantity)

        #make a order summary for the customer, to confirm their order before generate bill
        order_summary(item_lst , price_lst , total_price , quantity_lst)
        print(" ")
        conf = input("Please confirm your order(Y/N): ").upper()
        if conf == "Y":
            member = input("Do you have membership(Y/N): ").upper()
            if member == "Y":
                total_price = total_price * 0.9
                member_summary(item_lst , price_lst , total_price , quantity_lst)#member summary for the customer to know their total amount after the discount
                payment = float(input("Amount received: "))
                change = payment - total_price
                generate_bill(item, total_price, item_lst , price_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thanks For shopping with Us :)")
                sys.exit(0)#exit the program after generate bill
            elif member == "N":
                payment = float(input("Amount received: RM"))
                change = payment - total_price
                generate_bill(item, total_price, item_lst , price_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thanks For shopping with Us :)")
                sys.exit(0)
            else:
                print("Invalid Typing Error")
        #if confirmation is no let the customer continue to shopping
        elif conf == "N":
            print("Continue Exploring the shop")
        else:
            print("Invalid Typing Error")
    
    #if the choice is to add item into inventory text file
    elif choice == 3:
        #let the user to key in the correct id and password
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":#both id and password are correct then can add item into the system
            print(" ")
            print("ADD INVENTORY ITEM")
            print("---------------------")
            print()
            prod = []
            prod.append(len(all_products)+1)#add a new id for the item
            prod.append(input("Enter the Product Name: "))#add a name for the item
            pri = "{:.2f}".format(float(input("Price: ")))#add a price for the item
            quant = int(input("Quantity: "))#add quantity for the item in the store
            prod.append(str(pri))
            prod.append(str(quant))
            all_products.append(prod)
            while True:
                confirmation = input("CONFIRMATION: Are You Sure You Want To Add This Item(yes/no): ").lower()#confirmation to add the new product
                if confirmation in ['yes', 'no']:
                    break    
            if confirmation == 'yes':
                with open("razershop.txt" , 'a') as newline:
                    newline.write("{0},{1}, {2}   ,   {3}\n".format(prod[0] , prod[1] , prod[2] , prod[3]))
                print("Item Had Been Added")   
            else:
                sys.exit(0)
        else:#wrong id and password to ensure the inventory file not change by others
            print("Incorrect username and password")

    elif choice == 4:
        #let the user to key in the correct id and password
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":#both id and password are correct then can add item into the system
            print(" ")
            print("DELETE INVENTORY ITEM")
            print("---------------------")
            print()
            while True:
                del_prod = int(input("Enter the product id which you want to delete: "))#let the user enter the id which item they want delete
                if del_prod <= len(all_products):#ensure the id is in the list
                    break
                else:
                    print("That Item Does Not Exist")
                    print()

            while True:
                confirmation = input("CONFIRMATION: Are You Sure You Want To Delete This Item(yes/no): ").lower()#confirmation to delete the new product
                if confirmation in ['yes', 'no']:
                    break    
            if confirmation == 'yes':
                del(all_products[del_prod - 1])#delete the item
                for j in all_products:
                    if int(j[0]) > del_prod:#to make the id below the deleted item is move upwards
                        j[0] = int(j[0]) - 1
                f = open('razershop.txt' , 'w')#clear the file
                f.close()
                with open("razershop.txt" , 'a') as newline:#rewrite the new content into the file
                    for item in all_products:
                        newline.write("{0},{1}, {2}   ,   {3}\n".format(item[0].strip() , item[1].strip() , item[2].strip() , item[3].strip()))
                print("Item Had Been Deleted.")   
                sys.exit(0)

            #confirmation is no then quit the system
            else:
                sys.exit(0)
        else:
            print("Incorrect username and password")
 
    #if user coice is quit
    elif choice == 5:
        print("GoodBye!!")
        break

    #user enter the wrong option
    else:
        print("Sorry No This Option!!!")
        break
