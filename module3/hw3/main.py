def print_params(a=1, b="строка", c=True) -> None:
    print(a, b, c)


if __name__ == "__main__":
    print_params()
    print_params(2)
    print_params(3, "str")
    print_params(4, "string", False)
    print_params(b=25)
    print_params(c=[1, 2, 3])

    values_list = [5, "line", True]
    values_dict = {"a": 8, "b": "lesson", "c": False}
    print_params(*values_list)
    print_params(**values_dict)

    values_list_2 = [12, False]
    print_params(*values_list_2, 42)
