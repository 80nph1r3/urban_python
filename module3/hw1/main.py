def count_calls():
    global calls
    calls += 1


def string_info(string: str) -> tuple:
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string: str, list_to_search: list[str]) -> bool:
    count_calls()
    for list_string in list_to_search:
        if string.lower() == list_string.lower():
            return True
    return False


if __name__ == "__main__":
    calls = 0
    print(string_info("Capybara"))
    print(string_info("Armageddon"))
    print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))  # Urban ~ urBAN
    print(is_contains("cycle", ["recycling", "cyclic"]))  # No matches
    print(calls)
