from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

API_TOKEN = ""
DP = Dispatcher(storage=MemoryStorage())


@DP.message(CommandStart())
async def start(message: Message) -> None:
    print("Привет! Я бот помогающий твоему здоровью.")


@DP.message()
async def all_messages(message: Message) -> None:
    print("Введите команду /start, чтобы начать общение.")


async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await DP.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
