from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from app.keyboards.main import main_kb
import app.database.requests as rq

rt = Router()
@rt.message(Command("start"))
async def start_com(m: Message):
    await rq.set_user(m.from_user.id)
    await m.answer("Привет! Это бот магазин!", reply_markup=main_kb)