import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    CallbackQuery,
    FSInputFile,
    InlineKeyboardButton,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from crud_functions import add_user, get_all_products, is_included

API_TOKEN = ""
FORM_ROUTER = Router()


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@FORM_ROUTER.message(CommandStart())
async def start(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Рассчитать"),
                KeyboardButton(text="Информация"),
                KeyboardButton(text="Купить"),
                KeyboardButton(text="Регистрация"),
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard
    )


@FORM_ROUTER.message(F.text == "Регистрация")
async def sign_up(message: Message, state: State) -> None:
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@FORM_ROUTER.message(RegistrationState.username)
async def set_username(message: Message, state: State) -> None:
    if await is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await state.set_state(RegistrationState.username)
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await state.set_state(RegistrationState.email)


@FORM_ROUTER.message(RegistrationState.email)
async def set_email(message: Message, state: State) -> None:
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


@FORM_ROUTER.message(RegistrationState.age)
async def set_user_age(message: Message, state: State) -> None:
    await state.update_data(age=message.text)
    user_data = await state.get_data()
    await add_user(user_data["username"], user_data["email"], user_data["age"])


@FORM_ROUTER.message(F.text == "Рассчитать")
async def main_menu(message: Message) -> None:
    inline_keyboard = InlineKeyboardBuilder(
        [
            t[
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
    products = await get_all_products()
    keyboard = InlineKeyboardBuilder(
        [
            [
                InlineKeyboardButton(text=product[1], callback_data="product_buying")
                for product in products
            ],
        ]
    )
    images = ["orange.jpg", "banana.jpg", "pear.jpg", "apple.jpg"]
    for product, image in zip(products, images):
        await message.answer_photo(
            FSInputFile(image),
            caption=f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}",
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
