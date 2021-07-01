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
        return {"statusypkkjgfds`
    else:
        return {"status": False, "message": "invalid card kindly enter a new card"}