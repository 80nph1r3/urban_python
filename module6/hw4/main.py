from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(
        self,
        color: list[int],
        *sides: int,
    ) -> None:
        self.set_color(*color)
        if not self.__is_valid_sides(*sides):
            self.set_sides(*[1 for _ in range(self.sides_count)])
        else:
            self.set_sides(*sides)
        self.filled = True

    def get_color(self) -> list[int]:
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r: int, g: int, b: int) -> None:
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides: int) -> bool:
        return (
            all(map(lambda side: isinstance(side, int) and side > 0, sides))
            and len(sides) == self.sides_count
        )

    def get_sides(self) -> list[int]:
        return self.__sides

    def set_sides(self, *new_sides) -> None:
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self) -> int:
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list[int], *sides: int) -> None:
        super().__init__(color, *sides)

    def set_sides(self, *sides: int):
        super().set_sides(*sides)
        self.__radius = self.get_sides()[0] / 2 / pi

    def get_square(self) -> float:
        return self.__radius**2 * pi


class Triangle(Figure):
    sides_count = 3

    def get_square(self) -> float:
        half_len = len(self) / 2
        sides = self.get_sides()
        return sqrt(
            half_len
            * (half_len - sides[0])
            * (half_len - sides[1])
            * (half_len - sides[2])
        )


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list[int], *sides: int) -> None:
        if len(sides) == 1 and sides[0] > 0:
            sides = [sides[0] for _ in range(self.sides_count)]
        super().__init__(color, *sides)

    def get_volume(self) -> int:
        return self.get_sides()[0] ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle1 = Triangle((255, 255, 255), 3, 4, 5)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    print(triangle1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    print(triangle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))
    print(len(triangle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
    print(triangle1.get_square())
    print(circle1.get_square())
