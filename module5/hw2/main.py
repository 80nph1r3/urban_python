class House:
    def __init__(self, name: str, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self) -> int:
        return self.number_of_floors

    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, new_floor: int) -> None:
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, new_floor + 1):
            print(i)


if __name__ == "__main__":
    h1 = House("ЖК Эльбрус", 10)
    h2 = House("ЖК Акация", 20)

    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))
