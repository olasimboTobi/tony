import getpass


def receiver_number2():
    try:
        receiver_number = input("Enter receiver's phone number: ")
        receiver_number1 = list(receiver_number)
        a,b,c,d,e,f,g,h,i,j,k = receiver_number1
        if len(receiver_number1) == 11:
            receiver_number1 = (f"%s%s%s-%s%s%s-%s%s%s-%s%s " %(a,b,c,d,e,e,g,h,i,j,k))
            print(receiver_number1)
            return receiver_number1
    except ValueError:
        print("Enter 11 digits")
        receiver_number2()
phonenum2= receiver_number2()

customer_name = input("Enter your name:")

password = "1234"




class Ussd:
    def __init__(self, customer_name, phonenum2, password):
        self.customer_name = customer_name
        self.password = 1234
        self.phonenum2 = phonenum2
        self.balance = 10000

    def option(self):
        while("true"):
            print("1. Check balance ")
            print("2. Buy airtime. ")
            print("3. Transfer funds between number ")
            print("4. Quit ")
            click_option = input("Select your option: ")
            number = int(click_option)
            if (number == 1):
                self.check_balance()
            elif (number == 2):
                amount = int(input('Enter amount: '))
                self.buy_airtime_for_yourself(amount)
            elif (number == 3):
                amount = int(input('Enter amount: '))
                self.buy_airtime_for_others(amount,phonenum2,password)
            elif (number == 4):
                self.quit_transaction()


    def buy_airtime_for_yourself(self,amount):
        dial = input("Enter your ussd code: ")
        #dial1 = int(dial)
        try:
            if dial.isdigit():
                a,b,c = dial
                print(f"*%s%s%s#" %(a,b,c))
            else:
                print(f"Please enter the correct value")
                self.buy_airtime_for_yourself(amount)
        except ValueError:
            print(f"Please enter the correct value")
            self.buy_airtime_for_yourself(amount)
        print("Welcome to USSD Banking. Please note a #6.98 will be deducted from your balance")
        choose= input("""Please choose an option:\n 
        1. Accept \n 
        2. Cancel:  """)
        try:
            if choose == "1":
                amount1 = amount + 6.98
                if (amount1 > self.balance):
                    print("You don't have sufficient funds in your account")
                else:
                    self.balance -= amount1
                    print(f"{self.customer_name} has recharged #{amount1} to his phone and your account balance is {self.balance} Naira")
                    print("Would you like to do another transaction? Please, select option")
            else:
                if choose == "2":
                    print("Transaction aborted")
                    exit()  
        except ValueError:
            print(f"Please enter the correct value")
            self.buy_airtime_for_yourself(amount)

        
        
  
    def check_balance(self):
        print(f"{self.customer_name} has {self.balance} Naira ")

    
    def buy_airtime_for_others(self,amount,phonenum2,password1):
        dial = input("Enter your ussd code: ")
        #dial1 = int(dial)
        try:
            if dial.isdigit():
                a,b,c = dial
                print(f"*%s%s%s#" %(a,b,c))

            else:
                print(f"Please enter the correct value")
                self.buy_airtime_for_others(amount,phonenum2,password1)
        except ValueError:
            print(f"Please enter the correct value")
            self.buy_airtime_for_others(amount, phonenum2,password1)

        password1 = input("Enter password: " )
        phonenum1 = input("Enter phone number: ")
        if self.phonenum2 == phonenum1 and self.password == password1:
            print("Welcome to USSD Banking. Please note a #6.98 will be deducted from your balance")
            choose= input("Please choose an option 1. Accept \n 2. Cancel: ")
            try:
                if choose == "1":
                    amount1 = amount + 6.98
                    if (amount1 > self.balance):
                        print("You don't have sufficient funds in your account")
                    else:
                        self.balance -= amount1
                        print(f"{self.customer_name} has successfully recharged #{amount1} to {phonenum2} and your balance is {self.balance} Naira")
                        print("Would you like to perform another transaction? Please, choose your option. ")
                else:
                    if choose == "2":
                            exit()  
            except ValueError:
                print(f"Please enter the correct value")
                self.buy_airtime_for_others(amount,phonenum2,password1)

    def quit_transaction(self):
        input_1 = input("Would you like to perform another transaction? yes or no : ")
        if input_1 == "yes":
            self.option()

        else:
            print('Your transaction is successful.')
            exit()

        
        
        

            
def main():
    user_1 = Ussd(customer_name, phonenum2,password )
    user_1.option()
    

if __name__ == "__main__":
    main()
