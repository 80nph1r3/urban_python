def personal_sum(numbers: list[int | float]) -> tuple:
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчета суммы: {num}")

    return (result, incorrect_data)


def calculate_average(numbers: list[int | float]) -> float | None:
    try:
        num_sum = personal_sum(numbers)
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return
    try:
        return num_sum[0] / (len(numbers) - num_sum[1])
    except ZeroDivisionError:
        return 0


if __name__ == "__main__":
    print(
        f'Результат 1: {calculate_average("1, 2, 3")}'
    )  # Строка перебирается, но каждый символ - строковый тип
    print(
        f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}'
    )  # Учитываются только 1 и 3
    print(f"Результат 3: {calculate_average(567)}")  # Передана не коллекция
    print(f"Результат 4: {calculate_average([42, 15, 36, 13])}")  # Всё должно работать
