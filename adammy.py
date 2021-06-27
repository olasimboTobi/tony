number = input("Enter a number between ")
number = input("Enter num")

while number.isalpha() or len(number)>2 or len(number)<2 or "." in number or number[0]=="-":
    if number.alpha():
        number = input("number is alpha")

    elif "." in number:
        number = input("The number is float")
    elif len(number)>2 or len(number)< 2:
        number = input("length of number is less than 2")
    #check for negetive number 
    elif number[0] == "-":
        number = input("Number is negative")


sum_of_numbers = int(number[0] + int(number[1]))
while sum_of_numbers > 9:
    number = input("Sum is greater than 9 ")
    sum_of_numbers = int(number[0]) + int(number[1])
    
print(sum_of_numbers)
