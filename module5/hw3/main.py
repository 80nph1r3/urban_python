from typing import Type


class House:
    def __init__(self, name: str, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self) -> int:
        return self.number_of_floors

    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __is_house(self, object: object) -> None:
        if not isinstance(object, House):
            raise TypeError(
                "Оператор можно использовать только с экземплярами класса House"
            )

    def __is_int(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Операцию можно проводить только с целыми числами")

    def __eq__(self, other: object) -> bool:
        self.__is_house(other)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other: object) -> bool:
        self.__is_house(other)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other: object) -> bool:
        self.__is_house(other)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other: object) -> bool:
        self.__is_house(other)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other: object) -> bool:
        self.__is_house(other)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other: object) -> bool:
        self.__is_house(other)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value: int) -> object:
        self.__is_int(value)
        self.number_of_floors += value
        return self

    def __radd__(self, value: int) -> object:
        return self.__add__(value)

    def __iadd__(self, value: int) -> object:
        return self.__add__(value)

    def __sub__(self, value: int) -> object:
        self.__is_int(value)
        self.number_of_floors -= value
        return self

    def __isub__(self, value: int) -> object:
        return self.__sub__(value)

    def __rsub__(self, value: int) -> object:
        return self.__sub__(value)

    def __mul__(self, value: int) -> object:
        self.__is_int(value)
        self.number_of_floors *= value
        return self

    def __imul__(self, value: int) -> object:
        return self.__mul__(value)

    def __rmul__(self, value: int) -> object:
        return self.__mul__(value)

    def __floordiv__(self, value: int) -> object:
        self.__is_int(value)
        self.number_of_floors //= value
        return self

    def __rfloordiv__(self, value: int) -> object:
        return self.__floordiv__(value)

    def __ifloordiv__(self, value: int) -> object:
        return self.__floordiv__(value)

    def __truediv__(self, value: int) -> object:
        self.__is_int(value)
        self.number_of_floors /= value
        return self

    def __rtruediv__(self, value: int) -> object:
        return self.__truediv__(value)

    def __itruediv__(self, value: int) -> object:
        return self.__truediv__(value)

    def __mod__(self, value: int) -> object:
        self.__is_int(value)
        self.number_of_floors %= value
        return self

    def __rmod__(self, value: int) -> object:
        return self.__mod__(value)

    def __imod__(self, value: int) -> object:
        return self.__mod__(value)

    def __pow__(self, value: int) -> object:
        self.__is_int(value)
        self.number_of_floors **= value
        return self

    def __rpow__(self, value: int) -> object:
        return self.__pow__(value)

    def __ipow__(self, value: int) -> object:
        return self.__pow__(value)

    def go_to(self, new_floor: int) -> None:
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, new_floor + 1):
            print(i)


if __name__ == "__main__":
    h1 = House("ЖК Эльбрус", 10)
    h2 = House("ЖК Акация", 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__
    h1 -= 1
    print(h1)
    h1 *= 2
    print(h1)
    h1 //= 2
    print(h1)
    h1 %= 20
    print(h1)
    h1 /= 3
    print(h1)
    h1 **= 5
    print(h1)
