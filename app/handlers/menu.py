from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from app.keyboards.menu import menu_kb

rt = Router()

@rt.message(F.text == "Меню")
async def main_menu_m(m: Message):
    await m.answer("Категории Магазина:", reply_markup=menu_kb)

@rt.callback_query(F.data == "menu")
async def main_menu_cl(cl: CallbackQuery):
    await cl.message.edit_text("Категории Магазина:", reply_markup=menu_kb)
    await cl.answer("")