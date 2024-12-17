import threading
import time
from random import randint
from queue import Queue


class Table:
    def __init__(self, number: int) -> None:
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def run(self) -> None:
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables: Table) -> None:
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest) -> None:
        for guest in guests:
            is_seated = False
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    print(f"{guest.name} сел за стол {table.number}")
                    is_seated = True
                    break
            if not is_seated:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self) -> None:
        while not self.queue.empty() or any(
            map(lambda table: table.guest, self.tables)
        ):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if not self.queue.empty() and not table.guest:
                    table.guest = self.queue.get()
                    print(
                        f"{table.guest.name} вышел из очереди и сел за стол номер {table.number}"
                    )
                    table.guest.start()


if __name__ == "__main__":
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        "Maria",
        "Oleg",
        "Vakhtang",
        "Sergey",
        "Darya",
        "Arman",
        "Vitoria",
        "Nikita",
        "Galina",
        "Pavel",
        "Ilya",
        "Alexandra",
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
