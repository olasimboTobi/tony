input_1 = input("number1 : ")


# try:
    # if len(input_1)== 2:
    #     input_2 = list(input_1)
    #     print(input_2)
    #     input_3 = int(input_2[0]) + int(input_2[1])
    #     print(f"Total: {input_3}")    
if len(input_1) < 2:
    input_1 = input("Please input two digit: ")

elif len(input_1) > 2:
    input_1 = input("Please input two digit: ")

elif input_1.isalpha():
    input_1 = input("Please input two digit: ")

# else:
#     # len(input_1)== 2:
input_2 = list(input_1)
print(input_2)
input_3 = int(input_2[0]) + int(input_2[1])
if input_3 in range(1,10):
    print("You win!!! Your number input gave a result of one digit number")
else:
    print("Try Again !!!")
    input_1 = input("Please input two digit: ")

# except ValueError:
#         input_1 = input("Please input two digit: ")

# """for i in range(0,10):
#     result = i
#     print(f"{result}")"""

    
   


