def is_eq(product,num):
    if num > product[3]:
        return "notEQ"
def make_purchase():
    while True:
        is_false_input = True
        print("=======================================\n\t\tAVAILABLE PRODUCTS\n=======================================",'\n')

        for i in range(len(products_lst)):
            print(products_lst[i][0], '.', products_lst[i][1], '-'.center(10, '-'), f"quantity : [{products_lst[i][3]}]" , '-'.center(10,'-') , f"price : [${products_lst[i][2]}]")
        print(len(products_lst) + 1, '.', '(exit)\n')

        customer_input = input("\nEnter the product number to continue:")
        if customer_input == str(len(products_lst) + 1):
            break
        else:
            for element in products_lst:
                if element[0] == customer_input:
                    is_false_input = False
                    process_lst = element

            if is_false_input == True:
                print("\n[ERROR] Invalid input : Vendi can only process valid requests. Please try again.")

            elif is_false_input == False:

                quantity = int(input("Enter the quantity you would like to purchase:"))
                result = is_eq(process_lst, quantity)
                if result == "notEQ":
                    print("\nThe requested quantity is not currently available.")
                else:
                    final_price = process_lst[2] * quantity
                    is_used_credit = False
                    while True:
                            if is_used_credit == True:
                                break
                            else:
                                print(f"\nProduct name : {process_lst[1]}\nQuantity : {quantity}\nYour final price is: {final_price}$")
                                print("\n-------------------------------------")
                                print("\nHow would you like to pay?\n[1] Cash\n[2] Credit Card\n[3] exit")
                                pay_method = input("\nPlease select your payment method:")
                                print("\n-------------------------------------")

                                if pay_method == '1':
                                    insert_cash = input("\nPlease insert your cash(idid) or (0 to exit):")
                                    if insert_cash == 'idid':
                                        for i in range(len(products_lst)):
                                            if products_lst[i][0] == process_lst[0]:
                                                products_lst[i][3] -= quantity
                                                break
                                        print("\nThank you for your purchase!\nWe hope you enjoy your product.")
                                        break
                                    elif insert_cash == '0':
                                        break
                                    else:
                                        print(
                                            "\n[ERROR] Invalid input : Vendi can only process valid requests. Please try again.")
                                elif pay_method == '2':
                                    while True:
                                        is_credit_card_valid = False
                                        credit_num = input("\nEnter your credit card number (enter 0 to exit):")
                                        if credit_num == '0':
                                            break
                                        credit_pass = input("\nEnter your credit card password:")
                                        for credit_card in bank_ac:
                                            if credit_num == credit_card[0] and credit_pass == credit_card[1]:
                                                is_credit_card_valid = True
                                                credit_info = credit_card
                                        if is_credit_card_valid == False:
                                            print("Invalid card number or password. Please try again.")
                                        else:
                                            if final_price > credit_info[2]:
                                                print("\n-------------------------------------")
                                                print("\nThere is not enough money on your credit card.")
                                                is_used_credit = True
                                                break
                                            else:
                                                for i in range(len(bank_ac)):
                                                    if bank_ac[i][0] == credit_info[0]:
                                                        bank_ac[i][2] -= final_price
                                                for i in range(len(products_lst)):
                                                    if products_lst[i][0] == process_lst[0]:
                                                        products_lst[i][3] -= quantity
                                                        break
                                                print("\n-------------------------------------")
                                                print("\nThank you for your purchase!\nWe hope you enjoy your product.")
                                                is_used_credit = True
                                                break
                                elif pay_method == '3':
                                    break
                                else:
                                    print("\n[ERROR] Invalid input : Vendi can only process valid requests. Please try again.")
def atm_mode():
    while True:
        is_credit_card_valid = False
        credit_num = input("\nEnter your credit card number (enter 0 to exit):")
        if credit_num == '0':
            break
        credit_pass = input("\nEnter your credit card password:")
        for credit_card in bank_ac:
            if credit_num == credit_card[0] and credit_pass == credit_card[1]:
                is_credit_card_valid = True
                credit_info = credit_card
        if is_credit_card_valid == False:
            print("\nInvalid card number or password. Please try again.")
        else:
            add_money = int(input("\nHow much money would you like to add to your account?"))
            for i in range(len(bank_ac)):
                if credit_info[0] == bank_ac[i][0]:
                    bank_ac[i][2] += add_money
                    print("\n-------------------------------------")
                    print(f"\nMoney added successfully!\nAdded: ${add_money}\nNew balance: ${bank_ac[i][2]}")
                    break
            break


bank_ac = [['3251232' , '1234' , 200],['6241232' , '1234' , 5]]
admin_info = ['amir2mp' , '1234']
products_lst = [['1' , 'chips' , 2 , 10],
                ['2' , 'chocolate' , 2.3 , 8],
                ['3' , 'candy' , 5 , 5],
                ['4' , 'cookies' , 1.2 , 4],
                ['5', 'gum', 2.1, 10],
                ['6', 'popcorn', 2.4, 3],
                ['7', 'nuts', 8, 5],
                ['8', 'sandwiches', 12, 4],
                ['9', 'soda', 2.50, 6],
                ['10', 'juice', 1.70, 8],
                ['11', 'coffee', 3, 7],
                ['12', 'tea', 2, 4],
                ]




while True:
    print("Hello and welcome to Vendi!".center(50,'-'))

    print("\nHow would you like to enter?\n\n0. ATM mode\n1. Customer\n2. Admin \n3. exit\n")

    first_input = input("\nEnter your choice:")
    if first_input == '3':
        exit()
    elif first_input == '2':

        username = input("\nEnter your username:")
        password = input("\nEnter your password:")

        if username == admin_info[0] and password == admin_info[1]:
            while True:
                admin_input = input("\nWhat would you like to do?\n\n1. Add a Product\n2. Remove a Product\n3. Edit Product Quantity\n4. Exit\nEnter your choice:")
                if admin_input == '4':
                    break
                elif admin_input == '2':
                    for i in range(len(products_lst)):
                        print(f"{products_lst[i][0]} . {products_lst[i][1]}")
                    product_code = input("\n\n""Enter the product code:")
                    for i in range(len(products_lst)):
                        if products_lst[i][0] == product_code:
                            print(f"\nYou have removed {products_lst[i][1]} from the products.")
                            products_lst.pop(i)
                            break
                    else:
                        print("\n[ERROR] Invalid input : Vendi can only process valid requests. Please try again.")
                        break
                elif admin_input == '1':
                    products_name = input("\nEnter the product name: ")
                    products_quantity = int(input("\nEnter the product quantity: "))
                    products_price = float(input("\nEnter the product price: "))
                    products_code = str(len(products_lst) + 1)
                    products_lst.append([products_code , products_name , products_price , products_quantity])
                    print(f"\nNew product added  name : {products_name} , price : ${products_price} , quantity : {products_quantity}")
                elif admin_input == '3':
                    for i in range(len(products_lst)):
                        print(f"{products_lst[i][0]} . {products_lst[i][1]}")
                    product_code = input("\n\n""Enter the product code:")
                    for i in range(len(products_lst)):
                        if products_lst[i][0] == product_code:
                            products_quantity_add = int(input("\nEnter the amount to add:"))
                            products_lst[i][3] += products_quantity_add
                            print(f"\nProduct name: {products_lst[i][1]}  New quantity: {products_lst[i][3]}")
                            break
                    else:
                        print("\nProduct code not found!!")
                        break
        else:
            print("\nInvalid username or password. Please try again.")
    elif first_input == '1':
        make_purchase()
    elif first_input == '0':
        atm_mode()



