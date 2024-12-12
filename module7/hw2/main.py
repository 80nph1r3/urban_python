def custom_write(file_name: str, strings: list[str]) -> dict:
    string_positions = {}
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(len(strings)):
            string_positions[(i + 1, file.tell())] = strings[i]
            file.write(f"{strings[i]}\n")

    return string_positions


if __name__ == "__main__":
    info = [
        "Text for tell.",
        "Используйте кодировку utf-8.",
        "Because there are 2 languages!",
        "Спасибо!",
    ]

    result = custom_write("test.txt", info)
    for elem in result.items():
        print(elem)
