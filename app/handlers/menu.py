from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from app.keyboards.menu import menu
from app.database.requests import get_user_info

rt = Router()

@rt.message(F.text == "Меню")
async def main_menu_m(m: Message):
    await m.answer("Категории Магазина:", reply_markup= await menu())

@rt.callback_query(F.data == "to_menu")
async def main_menu_cl(cl: CallbackQuery):
    await cl.message.edit_text("Категории Магазина:", reply_markup= await menu())
    await cl.answer("")

@rt.message(F.text == "Профиль")
async def profile(m: Message):
    user = await get_user_info(m.from_user.id)
    text = (f"Имя: {user.first_name}\n"
            f"ID: {user.tg_id}\n"
            f"Баланс: {user.balance} руб.")
    await m.answer(text)

@rt.message(F.text == "Поддержка")
async def help(m: Message):
    await m.answer("Тех. Поддержка - @Rubinchik22")