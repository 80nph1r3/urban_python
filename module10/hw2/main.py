import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int) -> None:
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self) -> None:
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            time.sleep(1)
            print(
                f"{self.name} сражается {self.days} дней, осталось {self.enemies} воинов"
            )
        print(f"{self.name} одержал победу спустя {self.days} дней!")


if __name__ == "__main__":
    knights = [Knight("Sir Lancelot", 10), Knight("Sir Galahad", 20)]
    for knight in knights:
        knight.start()
    for knight in knights:
        knight.join()

    print("Все битвы  закончилилсь!")
