def calculate_structure_sum(data_structure) -> int:
    if isinstance(data_structure, (list, tuple, set)):
        return sum(calculate_structure_sum(item) for item in data_structure)
    elif isinstance(data_structure, dict):
        return calculate_structure_sum(
            [*data_structure.keys(), *data_structure.values()]
        )
    elif isinstance(data_structure, (int, float)):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    else:
        return 0


if __name__ == "__main__":
    data_structure = [
        [1, 2, 3],
        {"a": 4, "b": 5},
        (6, {"cube": 7, "drum": 8}),
        "Hello",
        ((), [{(2, "Urban", ("Urban2", 35))}]),
    ]

    result = calculate_structure_sum(data_structure)
    print(result)
