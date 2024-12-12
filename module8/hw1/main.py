def add_everything_up(a: int | float | str, b: int | float | str) -> int | float | str:
    try:
        return a + b
    except TypeError:
        return f"{a}{b}"


if __name__ == "__main__":
    print(add_everything_up(123.456, "строка"))
    print(add_everything_up("яблоко", 4215))
    print(add_everything_up(123.456, 7))
