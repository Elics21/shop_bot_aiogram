from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from app.keyboards.category import category_1

rt = Router()

@rt.callback_query(F.data == "category-1")
async def category1_data(cl: CallbackQuery):
    await cl.message.edit_text("Категория 1:", reply_markup=category_1)
    await cl.answer("")