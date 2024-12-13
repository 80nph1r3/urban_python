class Plant:
    edible = False

    def __init__(self, name: str) -> None:
        self.name = name


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food: Plant) -> None:
        if not isinstance(food, Plant):
            print(f"{self.name} ест только растения!")
            return
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


if __name__ == "__main__":
    a1 = Predator("Волк с Уолл-Стрит")
    a2 = Mammal("Хатико")
    p1 = Flower("Цветик семицветик")
    p2 = Fruit("Заводной апельсин")

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)

    a1.eat(p1)
    a2.eat(p2)
    a2.eat(a1)

    print(a1.alive)
    print(a2.fed)
