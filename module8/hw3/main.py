class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin: int) -> bool | None:
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номера")
        if not 1_000_000 <= vin <= 9_999_999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, numbers: str) -> bool | None:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message) -> None:
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message) -> None:
        self.message = message


if __name__ == "__main__":
    try:
        first = Car("Model1", 1_000_000, "f123dj")
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f"{first.model} успешно создан")

    try:
        second = Car("Model2", 300, "т001тр")
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f"{second.model} успешно создан")

    try:
        third = Car("Model3", 2020202, "нет номера")
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f"{third.model} успешно создан")
