
gussing_num = input("Enter two digit number: ")


def guess_number(gussing_num):
    while (len(gussing_num) != 2) and (gussing_num.isalpha()):
        gussing_num = input("Please input two digit: ")
        guess_number(gussing_num)

    try:

        input_2 = list(gussing_num)
        if (len(input_2) != 2):
            gussing_num = input("Please input two digit: ")
            guess_number(gussing_num)
        else: 
            print(input_2) 

    except ValueError:
        gussing_num = input("Please input two digit: ")
        guess_number(gussing_num)
    input_3 = int(input_2[0]) + int(input_2[1])
    if input_3 in range(1,10):
        print("You win!!! Your number input gave a result of one digit number")
        gussing_num = input("Would you play again? yes or no : ")
        if gussing_num == "yes":
            gussing_num = input("Please input two digit: ")
            guess_number(gussing_num)

        else:
            print("Thanks for playing")
        
            
    else:
        print("Try Again !!!")
        gussing_num = input("Please input two digit: ")
        guess_number(gussing_num)

    return str(input_3)


result = guess_number(gussing_num)

    
   

