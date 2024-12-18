import time
import asyncio


async def start_strongman(name: str, power: int) -> None:
    print(f"Силач {name} начал соревнования")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнование")


async def start_tournament() -> tuple[asyncio.Task]:
    await asyncio.gather(
        start_strongman("Pasha", 3),
        start_strongman("Denis", 4),
        start_strongman("Apollon", 5),
    )


if __name__ == "__main__":
    asyncio.run(start_tournament())
