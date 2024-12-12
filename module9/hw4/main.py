from typing import Callable
from random import choice


def get_advanced_writer(file_name: str) -> Callable:
    def write_everything(*data_set):
        with open(file_name, "w") as file:
            for data in data_set:
                file.write(str(data))
                file.write("\n")

    return write_everything


class MysticBall:
    def __init__(self, *words) -> None:
        self.words = words

    def __call__(self) -> str:
        return choice(self.words)


if __name__ == "__main__":
    first = "Мама мыла раму"
    second = "Рамена мало было"
    result = list(map(lambda char1, char2: char1 == char2, first, second))

    write = get_advanced_writer("example.txt")
    write("Это строчка", ["А", "это", "уже", "число", 5, "в", "списке"])

    first_ball = MysticBall("Да", "Нет", "Наверное")
    print(first_ball())
    print(first_ball())
    print(first_ball())
