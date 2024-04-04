from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, F

from app.keyboards.menu import menu_kb

rt = Router()

@rt.message(F.text == "Меню")
async def main_menu(m: Message):
    await m.answer("Категории Магазина:", reply_markup=menu_kb)