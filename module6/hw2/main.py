class Vehicle:
    __COLOR_VARIANTS = ["red", "green", "blue", "yellow"]

    def __init__(self, owner: str, model: str, engine_power: int, color: str) -> None:
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        print(
            self.get_model(),
            self.get_horsepower(),
            self.get_color(),
            f"Владелец: {self.owner}",
            sep="\n",
        )

    def set_color(self, color: str) -> None:
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color.lower()
        else:
            print(f"Нельзя сменить цвет на {color}")


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5


if __name__ == "__main__":
    vehicle1 = Sedan("Fedos", "Toyota Mark II", 500, "blue")
    vehicle1.print_info()

    vehicle1.set_color("Pink")
    vehicle1.set_color("GREEN")
    vehicle1.owner = "Vasyok"

    vehicle1.print_info()
