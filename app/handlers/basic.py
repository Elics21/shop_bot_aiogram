from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

rt = Router()
@rt.message(Command("start"))
async def start_com(m: Message):
    await m.answer("Привет! Это бот магазин!")