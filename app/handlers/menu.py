from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from app.keyboards.menu import menu

rt = Router()

@rt.message(F.text == "Меню")
async def main_menu_m(m: Message):
    await m.answer("Категории Магазина:", reply_markup= await menu())

@rt.callback_query(F.data == "to_menu")
async def main_menu_cl(cl: CallbackQuery):
    await cl.message.edit_text("Категории Магазина:", reply_markup= await menu())
    await cl.answer("")