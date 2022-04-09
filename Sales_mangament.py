from datetime import datetime
import random
import sys



all_products = [line.strip().split(',') for line in open('razershop.txt','r').readlines()]



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



def display_all():
    print("SNO\t Product \t\t\t\t  Price\t\t\tIn Stock")
    for item in all_products:
        print("\n{0}\t{1} \t\t\t {2}\t\t{3}".format(item[0], item[1], item[2], item[3]))



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



def decrement_item(item_id, quantity):
    with open('razershop.txt', 'r') as fin:
        # indexes for id and quantity
        index_id = 0
        index_quantity = 3
        
        # output buffer
        output = []
        
        # Add headaer to output buffer
        header = fin.readline().rstrip()
        output.append(header)  # header without '\n' at end of line
        
        bfound_item = False
        for line in fin:
            # Check each line for item_id then upadte quantity
            line = line.rstrip()
            if not bfound_item:
                # Only process if item_id has not been found yet
                # Break line into separate fields
                row = line.split()
                current_id = row[index_id]
                if current_id == item_id:
                    # Found item
                    # Check if sufficiente quantity
                    current_quantity = int(row[index_quantity])
                    if current_quantity >= quantity:
                        # Decrement quantity
                        current_quantity -= quantity
                        row[index_quantity] = str(current_quantity)
                        line = ' '.join(row)
                        bfound_item = True
                    else:
                        # Insufficient quantity for update
                        s = f"Sorry, available quantity is only {int(row[index_quantity])}"
                        raise Exception(s)
                    
            # Add line to output
            output.append(line)  # add copy since row changes with loop
            
    # Update inventory file
    with open('razershop.txt', 'w') as fout:
        for line in output:
            fout.write(line + '\n')



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
                if int(item[0]) == prod_id:
                    quantity = int(input("Please enter the quantity: "))
                    item_lst.append(item[1])
                    quantity_lst.append(quantity)
                    price_q = float(item[2]) * quantity
                    price_lst.append(price_q)
                    total_price = total_price + price_q
                    decrement_item(prod_id , quantity)

        order_summary(item_lst , price_lst , total_price , quantity_lst)
        print(" ")
        conf = input("Please confirm your order(Y/N): ").upper()
        if conf == "Y":
            member = input("Do you have membership(Y/N): ").upper()
            if member == "Y":
                total_price = total_price * 0.9
                member_summary(item_lst , price_lst , total_price , quantity_lst)
                payment = float(input("Amount received: "))
                change = payment - total_price
                generate_bill(item, total_price, item_lst , price_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thanks For shopping with Us :)")
                sys.exit(0)
            elif conf == "N":
                payment = float(input("Amount received: RM"))
                change = payment - total_price
                generate_bill(item, total_price, item_lst , price_lst , quantity_lst ,change , payment)
                print(" ")
                print("Thanks For shopping with Us :)")
                sys.exit(0)
            else:
                print("Invalid Typing Error")

        elif conf == "N":
            print("Continue Exploring the shop")
        else:
            print("Invalid Typing Error")
    
    elif choice == 3:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            print(" ")
            print("ADD INVENTORY ITEM")
            print("---------------------")
            print()
            prod = []
            prod.append(len(all_products)+1)
            prod.append(input("Enter the Product Name: "))
            pri = "{:.2f}".format(float(input("Price: ")))
            quant = int(input("Quantity: "))
            prod.append(str(pri))
            prod.append(str(quant))
            all_products.append(prod)
            while True:
                confirmation = input("CONFIRMATION: Are You Sure You Want To Add This Item(yes/no): ").lower()
                if confirmation in ['yes', 'no']:
                    break    
            if confirmation == 'yes':
                with open("razershop.txt" , 'a') as newline:
                    newline.write("\n{0} , {1}, {2} , {3}".format(prod[0] , prod[1] , prod[2] , prod[3]))
                print("Item Had Been Added")   
            else:
                sys.exit(0)
        else:
            print("Incorrect username and password")

    elif choice == 4:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            print(" ")
            print("DELETE INVENTORY ITEM")
            print("---------------------")
            print()
            while True:
                del_prod = int(input("Enter the product id which you want to delete: "))
                if del_prod <= len(all_products):
                    break
                else:
                    print("That Item Does Not Exist")
                    print()

            while True:
                confirmation = input("CONFIRMATION: Are You Sure You Want To Delete This Item(yes/no): ").lower()
                if confirmation in ['yes', 'no']:
                    break    
            if confirmation == 'yes':
                del(all_products[del_prod - 1])
                for j in all_products:
                    if int(j[0]) > del_prod:
                        j[0] = int(j[0]) - 1
                f = open('razershop.txt' , 'w')
                f.close()
                with open("razershop.txt" , 'a') as newline:
                    for item in all_products:
                        newline.write("{0} , {1}, {2} , {3}\n".format(item[0] , item[1] , item[2] , item[3]))
                print("Item Had Been Deleted.")   
                sys.exit(0)
            else:
                sys.exit(0)
        else:
            print("Incorrect username and password")
 
    elif choice == 5:
        print("GoodBye!!")
        break

    else:
        print("Sorry No This Option!!!")
        break
