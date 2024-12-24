import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    CallbackQuery,
    FSInputFile,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

API_TOKEN = "6898179198:AAHDFnDVaVTzFU710T8SjOsA2Z9fHOfbebw"
FORM_ROUTER = Router()


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@FORM_ROUTER.message(CommandStart())
async def start(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Рассчитать"),
                KeyboardButton(text="Информация"),
                KeyboardButton(text="Купить"),
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard
    )


@FORM_ROUTER.message(F.text == "Рассчитать")
async def main_menu(message: Message) -> None:
    inline_keyboard = InlineKeyboardBuilder(
        [
            [
                InlineKeyboardButton(
                    text="Рассчитать норму калорий", callback_data="calories"
                ),
                InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas"),
            ]
        ]
    )
    await message.answer("Выберите опцию", reply_markup=inline_keyboard.as_markup())


@FORM_ROUTER.message(F.text == "Купить")
async def get_buying_list(message: Message) -> None:
    products = {
        "apple": {
            "name": "Яблоко",
            "image": "apple.jpg",
            "description": "Сочный плод яблони, который употребляется в пищу в свежем и запеченном виде, служит сырьём в кулинарии и для приготовления напитков.",
            "price": 100,
        },
        "banana": {
            "name": "Банан",
            "image": "banana.jpg",
            "description": "Одна из древнейших пищевых культур, а для тропических стран — важнейшее пищевое растение и главная статья экспорта.",
            "price": 200,
        },
        "pear": {
            "name": "Груша",
            "image": "pear.jpg",
            "description": "Род плодовых и декоративных деревьев и кустарников семейства розовые (Rosaceae), а также их плод",
            "price": 300,
        },
        "orange": {
            "name": "Апельсин",
            "image": "orange.jpg",
            "description": "Самая распространённая цитрусовая культура во всех тропических и субтропических областях мира",
            "price": 400,
        },
    }
    keyboard = InlineKeyboardBuilder(
        [
            [
                InlineKeyboardButton(
                    text=products["orange"]["name"], callback_data="product_buying"
                ),
                InlineKeyboardButton(
                    text=products["banana"]["name"], callback_data="product_buying"
                ),
                InlineKeyboardButton(
                    text=products["pear"]["name"], callback_data="product_buying"
                ),
                InlineKeyboardButton(
                    text=products["apple"]["name"], callback_data="product_buying"
                ),
            ],
        ]
    )
    for key, value in products.items():
        await message.answer_photo(
            FSInputFile(value["image"]),
            caption=f"Название: {value['name']} | Описание: {value['description']} | Цена: {value['price']}",
        )
    await message.answer(
        "Выберите товар для покупки:", reply_markup=keyboard.as_markup()
    )


@FORM_ROUTER.callback_query(F.data == "product_buying")
async def send_confirm_message(call: CallbackQuery) -> None:
    await call.message.answer("Вы успешно приобрели продукт!")


@FORM_ROUTER.callback_query(F.data == "formulas")
async def send_formula(call: CallbackQuery) -> None:
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")


@FORM_ROUTER.callback_query(F.data == "calories")
async def set_age(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer("Введите свой возраст")
    await state.set_state(UserState.age)


@FORM_ROUTER.message(UserState.age)
async def set_height(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await state.set_state(UserState.height)


@FORM_ROUTER.message(UserState.height)
async def set_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(height=message.text)
    await message.answer("Введите свой вес")
    await state.set_state(UserState.weight)


@FORM_ROUTER.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = (
        int(data["weight"]) * 10 + int(data["height"]) * 6.25 - int(data["age"]) * 5 + 5
    )
    await message.answer(f"Норма калорий: {result}")


async def main() -> None:
    bot = Bot(token=API_TOKEN)

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(FORM_ROUTER)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
