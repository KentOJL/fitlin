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
    print("SNO\t Product \t\t\t\t In Stock\t\t\tPrice")
    for item in all_products:
        print("\n{0}\t{1} \t\t\t {2}\t\t\t{3}".format(item[0], item[1], item[2], item[3]))



def order_summary(product, price , total , q_lst):
    print("-" * 80)
    print("\t\tRazer Mouse Shop")
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
    print("\n\tRazer Mouse Shop")
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
            pri = float(input("Price: "))
            quant = int(input("Quantity: "))
            prod.append(str(pri))
            prod.append(str(quant))
            all_products.append(prod)
            for i in prod:
                with open("razershop.txt" , 'a') as newline:
                    newline.write("{0} , {1}, {2} , {3}\n".format(prod[0] , prod[1] , prod[2] , prod[3]))
        else:
            print("Incorrect username and password")

    elif choice == 4:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            del_prod = int(input("Enter the product id which you want to delete: "))
            del(all_products[del_prod - 1])
            
            with open("razershop.txt" , 'w') as newline:
                 newline.write(all_products)
        else:
            print("Incorrect username and password")
    else:
        print("GoodBye!!")
        break
