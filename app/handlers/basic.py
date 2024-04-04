from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from app.keyboards.main import main_kb

rt = Router()
@rt.message(Command("start"))
async def start_com(m: Message):
    await m.answer("Привет! Это бот магазин!", reply_markup=main_kb)