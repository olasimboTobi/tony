from getpass import getpass

#Password Confirmation
user_password1 = getpass('Enter password : ')
def get_password(pwd):
    user_pwd = list(pwd)
    print(f"{user_pwd}")
    try:
        if len(user_pwd) == 4:
            return " ".join(user_pwd)
        else:
            print("Please wrong password. Enter a password that is exactly 4 digit")
            user_password1 = getpass('Enter password : ')
            get_password(pwd)

    except ValueError:
        print("Please,look wrong password. Enter a password that is exactly 4 digit")
        user_password1 = getpass('Enter password : ')
        get_password(pwd)
        

user_password = get_password(user_password1)

#Expired Date Validation
current_date= int(input("Enter Issued Card Year: "))
card_expired_date = int(input("Enter Expired Date: "))
try:

    if current_date not in range(current_date,(card_expired_date + 1)):
        print("Card has expired")
        exit()
    else:
        print("Card not expired")

except:
    exit()

#Card Type Identification
user_card_type = getpass("Enter Issue Identification Number: ")
def get_card_type(card_type1):
    try:
        if card_type1.startswith('4'):
            print(f"Your atm card is a Visa card")
        elif card_type1.startswith('5'):
            card_type2 = list(card_type1)
            if len(card_type2) == 19:
                print(f"This card is a Verve card")
            elif len(card_type2) == 16:
                print(f"This card is a Master card")
            else:
                print("Please, input the complete number. ")
                user_card_type = getpass("Enter Issue Identification Number: ")
                get_card_type(card_type1)
        else:
            print(f"Issue Identification number not complete")
            user_card_type = getpass("Enter Issue Identification Number: ")
            get_card_type(card_type1)
    except RecursionError:
        print(f"Issue Identification number not complete1")
        user_card_type = getpass("Enter Issue Identification Number: ")
        get_card_type(card_type1)
        

card_number = get_card_type(user_card_type)


#Input the Name of the Bank
bank_name = input("Enter Bank Name: ")



#Implimentation of Atmcard

class Atmcard:
    def __init__(self, name, customer, password, card_type ):
        self.bank_name = name
        self.customer_name = input('Enter customer name : ')
        self.password = password
        self.balance = 10000.0
        self.card_type = card_type


    def welcome_message(self):
        print(f"Welcome to {self.bank_name} bank ")


    def option(self):
        while("true"):
            print("1. Check balance ")
            print("2. Withdraw Money. ")
            print("3. Deposit Money ")
            print("4. Quit ")
            click_option = input("Select your option: ")
            number = int(click_option)
            if (number == 1):
                self.show_balance()
            elif (number == 2):
                amount = int(input('Enter amount: '))
                self.withdraw_money(amount)
            elif (number == 3):
                amount = int(input('Enter amount: '))
                self.deposit_money(amount)
            elif (number == 4):
                self.quit_transaction()


    def ask_password(self):
        #user_password = int(getpass('Enter password : '))
        if (user_password != self.password):
            print("Wrong Password")
        else:
            self.option()

    
    def show_clearbalance(self):
        print(f"{self.customer_name} has {self.balance} Naira ")


    
    def withdraw_money(self, amount):
        if (amount > self.balance):
            print("You don't have sufficient funds in your account")
        else:
            self.balance -= amount
            print(f"{self.customer_name} has withdraw #{amount} and your balance is {self.balance} Naira")

    
    def deposit_money(self, amount):
        self.balance += amount
        print(f"{self.customer_name} has deposited #{amount} and the total balance is {self.balance} Naira ")
    

    
    def quit_transaction(self):
        input_1 = input("Would you like to perform another transaction? yes or no : ")
        if input_1 == "yes":
            self.ask_password()

        else:
            print('Thank you for banking with us.')
            exit()
        
        
#Instantiation of Atmcard

def main():
    user_1 = Atmcard(bank_name, 'Ojo',user_password,card_number)
    user_1.welcome_message()
    user_1.ask_password()

if __name__ == "__main__":
    main()

