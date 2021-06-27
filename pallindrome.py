def main():
    user_input_string = input("Enter string: ").lower()
    if user_input_string == user_input_string[::-1]:
        print(f" The string entered is pallindrome")
    else:
        print(f"The string is not pallindrome")

if __name__ == "__main__":
    main()

    