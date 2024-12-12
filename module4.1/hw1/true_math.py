from math import inf


def divide(first: int | float, second: int | float) -> float:
    if second == 0:
        return inf
    return first / second
