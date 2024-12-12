if __name__ == "__main__":
    first = ["Strings", "Student", "Computers"]
    second = ["Строка", "Урбан", "Компьютер"]
    first_result = (
        abs(len(string1) - len(string2))
        for string1, string2 in zip(first, second)
        if len(string1) != len(string2)
    )
    second_result = (
        len(first[string_index]) == len(second[string_index])
        for string_index in range(len(first))
    )
    print(list(first_result), list(second_result), sep="\n")
