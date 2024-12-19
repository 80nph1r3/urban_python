import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

API_TOKEN = "6898179198:AAHDFnDVaVTzFU710T8SjOsA2Z9fHOfbebw"
FORM_ROUTER = Router()


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@FORM_ROUTER.message(F.text.lower() == "calories")
async def start(message: Message, state: FSMContext) -> None:
    await message.answer("Введите свой возраст")
    await state.set_state(UserState.age)


@FORM_ROUTER.message(UserState.age)
async def set_height(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await state.set_state(UserState.height)


@FORM_ROUTER.message(UserState.height)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await message.answer("Введите свой вес")
    await state.set_state(UserState.weight)


@FORM_ROUTER.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = (
        int(data["weight"]) * 10 + int(data["height"]) * 6.25 - int(data["age"]) * 5 + 5
    )
    await message.answer(f"Норма калорий: {result}")
    await state.clear()


@FORM_ROUTER.message()
async def all_messages(message: Message, state: FSMContext) -> None:
    await message.answer('Введите "calories", чтобы начать общение.')


async def main() -> None:
    bot = Bot(token=API_TOKEN)

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(FORM_ROUTER)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
