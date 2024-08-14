def get_multiplied_digits(number):
    str_number = str(number)
    frist = int(str_number[0])
    if len(str_number) == 1:
        return int(str_number)
    elif len(str_number) > 1:
        return frist * get_multiplied_digits(int(str_number[1:]))





result = get_multiplied_digits(49283)
print(result)

