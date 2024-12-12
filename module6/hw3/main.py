from random import randrange


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed: int) -> None:
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx: int, dy: int, dz: int) -> None:
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self) -> None:
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self) -> None:
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self) -> None:
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self) -> None:
        print(f"Here are(is) {randrange(1, 5)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz: int) -> None:
        self._cords[2] -= int(abs(dz) * self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed: int) -> None:
        super().__init__(speed)
        self.sound = "Click-click-click"


if __name__ == "__main__":
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()
