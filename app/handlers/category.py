from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from app.keyboards.items import items

rt = Router()

@rt.callback_query(F.data.startswith("category_"))
async def category1_data(cl: CallbackQuery):
    category_id = cl.data.split("_")[1]
    await cl.message.edit_text("Категория 1:", reply_markup=await items(category_id))
    await cl.answer("")