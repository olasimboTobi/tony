def validate(n):
    if len(str(n)) > 16:
        return False
    else:
        if len(str(n)) % 2 == 0:
            for i in str(n[0::2]):
                digit = int(str(n[i])) * 2
                while digit > 9:
                    digit = sum(map(int, str(digit)))
            dig_sum = sum(map(int, str(n)))
            return True if dig_sum % 10 == 0 else False
        elif len(str(n)) % 2 != 0:
            for i in str(n[1::2]):
                digit = int(str(n[i])) * 2
                while digit > 9:
                    digit = sum(map(int, str(digit)))
            dig_sum = sum(map(int, str(n)))
            return True if dig_sum % 10 == 0 else False