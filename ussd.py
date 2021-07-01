import getpass
global balance
sender1 = {}
prompt1 = input("Enter your name : ")
prompt2 = input("Enter account number: ")
prompt3 = input("Enter phone number: ")
prompt4 = input("Enter bank name: ")
receiver = {"name":prompt1, "accountnumber":prompt2, "phonenumber":prompt3, "bankname":prompt4,}

class Ussd:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver


    def buy_airtime (self,amount):
        if self.sender["name"] in sender1.values:
            x= input("Enter your bank USSD Code: ")
            try:
                if len(x)== 3:
                    #int(x)
                    print(f"*%s* #%i " %(x,amount))
                else:
                    if x.isalpha():
                        print("Please enter your 3 digit bank USSD Code ")
                        self.buy_airtime(amount)
                    else:
                        print("Please enter your 3 digit bank USSD Code ")
                        self.buy_airtime(amount)
            except ValueError:
                print("Please enter your 3 digit bank USSD Code ")
                self.buy_airtime(amount)
        else:
            print(f"Please, register your phone number")
            pass #self.register()

    def register(self, **kwargs):
        sender1["name"]= input("Enter Your Name: ")
        sender1["phonenumber"] = input("Enter Your phonenumber: ")
        a,b,c,d,e,f,g,h,i,j,k = sender1["phonenumber"]
        if len(sender1["phonenumber"]) == 11:
            print(f"%s%s%s-%s%s%s-%s%s%s " %(a,b,c,d,e,e,g,h,i,j,k))







                        

