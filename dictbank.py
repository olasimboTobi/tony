
def print_menu():
    print ("1. List Account(s)")
    print ("2. Open an Account")
    print ("3. Close an Account")
    print ("4. Withdraw money")
    print ("5. Deposit Money")
    print ("6. Quit")
    print

accounts = {}
menu_choice = 0
print_menu()
#balance = {}
balance = 0
while True:
    menu_choice = int(input("Type in a number (1-6): "))
    print
    if menu_choice == 1:
        print ("Accounts")
        for x in accounts.keys():
            print ("Accountnumber:", x, "with balance #", balance)
        print
    elif menu_choice == 2:
        print ("Enter a new Accountnumber")
        number = input("New accountnumber: ")
        #phone = input("Number: ")
        accounts[number]=balance
        print ("Accountnumber", number, "opened.")
    elif menu_choice == 3:
        print ("Close an Accountnumber")
        number = input("Accountnumber: ")
        if number in accounts:
            #accounts[number]=balance
            del accounts[number]
            print ("Accountnumber", number, "is closed.")
        else:
            print ("Accountnumber", number, "was not found")
    #elif menu_choice == 4:
        #print("Lookup Number")
        #name = input("Name: ")
        #if name in numbers:
        #    print("The number is", numbers[name])
        #else:
        #    print(name, "was not found")
    elif menu_choice == 4:
        print ("Withdraw money from Account.")
        number = input("Accoutnnumber: ")
        if number in accounts:
            withdraw = float(input("How much money would you like to withdraw? > "))
            if withdraw < balance:
                #accounts[number]=balance
                number[balance] -= withdraw
                #balance vann number 444 bijv. !!
                print ("Your new balance is #", balance)
            else:
                print ("There are no sufficient funds on this accountnumber")
    elif menu_choice == 5:
        print ("Deposit money onto Account.")
        number = input("Accountnumber: ")
        if number in accounts:
            deposit = float(input("How much money would you like to deposit? > "))
            #accounts[number]=balance
            balance += deposit
            #balance vannn number 444 bijv. !!
            print ("Your new balance is #", balance)
        else:
            print ("That accountnumber does not exist.")
    elif menu_choice == 6:
        print ("Quit.")
        break
    else:
        print ("Please enter a number between 1 and 6.")
    print
    print_menu()

