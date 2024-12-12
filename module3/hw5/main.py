def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:
        return 1
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    return first


if __name__ == "__main__":
    result = get_multiplied_digits(40203)
    print(result)
    result2 = get_multiplied_digits(402030)
    print(result2)
