from datetime import datetime
import getpass
balance = 10000
def checkLuhn(card_number):
    sum_of_digit = 0
    is_second = False
    card_number_reversed = card_number[::-1]
    for single_digit in card_number_reversed:
        if single_digit.isalpha():
            return {"message": "An alpabet cannot exist in your card_number", "status":False}
        digit_to_integer = int(single_digit)
        if (is_second == True):
            digit_to_integer = digit_to_integer * 2
        sum_of_digit += digit_to_integer // 10
        sum_of_digit += digit_to_integer % 10
        is_second = not is_second
    if (sum_of_digit % 10 == 0):
        return {"status": True}
    else:
        return {"status": False, "message": "invalid card kindly enter a new card"}
def check_expiry(date):
    month = date.split("/")[0]
    year = date.split("/")[-1]
    if month.isdigit() and year.isdigit() and date[2] == "/" and int(month)<=12 and  int(month)>=1 :
        current_month = datetime.now().strftime("%m")
        current_year = datetime.now().strftime("%y")
        if int(year) == int(current_year) and int(month) >= int(current_month):
            return {"status": True}
        elif int(year) > int(current_year):
            return {"status": True}
        else:
            return {"message": "Your card has expired", "status": False}
    else:
        return {"message": "Expiry date mismatch", "status": False}
def withdrawal():
    amount = input("Enter amount you wish to withdraw\n")
    try:
        converted_amount = float(amount) 
        global balance
        if converted_amount <= balance:
            new_balance = balance - converted_amount
        balance = new_balance
        return {"message": f"Withdrawal successful. Balance is {new_balance}", "status":True}
    except ValueError:
        return {"message": "Error dispensing money", "status": False}
def check_balance():
    return {"message": f"Your balance is {balance}"}    

def execute(credit_card, expiry_date, pin):
    actual_pin = "2345"
    trials = 1
    check_card_validity = checkLuhn(credit_card)
    card_expired = check_expiry(expiry_date)
    
    while (check_card_validity.get("status") == False or card_expired.get("status") == False or pin !=actual_pin) and trials <= 3:
        print (trials)
        if check_card_validity.get("status") == False:
            credit_card = input(f"{check_card_validity.get('message')} \n  enter credit card details\n")
            trials += 1
        if card_expired.get("status") == False:
            expiry_date = input(f"{card_expired.get('message')} enter expiry date of your card (format: 'MM/YY', e.g 01/22) \n")
            trials += 1
        if pin != actual_pin:
            pin = getpass.getpass(prompt="Incorrect pin entered. Kindly provide the correct pin")
    if trials > 3:
        print("Your card has been blocked due to fraudulent transactions kindly contact your nearest bank branch")
        return
    customer_action = input("What actions would you like to perform?\nFor Withdrawal enter 1 \nFor Checking balance enter 2\n")

    action_object = {
        "1": withdrawal,
        "2": check_balance,
        "exit": {"message":"Thank you for banking with us"}
    }
    print(customer_action)
    while customer_action not in action_object.keys():
        customer_action = input(
        "Incorrect entry, What actions would you like to perform?\nFor Withdrawal enter 1 \nFor Checking balance enter 2\n Or enter exit to stop")
    print(action_object.get(customer_action.lower())().get("message"))
    perform_action_again = input("Would you like to perform the activity again? Y or N\n")
    if perform_action_again.lower() == "y":
        execute(credit_card, expiry_date, pin)
    else:
        print("Thank you for banking with us do have a great day")

credit_card = input("enter credit card details\n")
expiry_date = input("enter expiry date of your card (format: 'MM/YY', e.g 01/22) \n")
pin = getpass.getpass(prompt="Enter your password")
execute(credit_card, expiry_date, pin)