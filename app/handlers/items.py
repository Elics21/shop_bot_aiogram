from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from app.database.requests import get_item

rt = Router()

@rt.callback_query(F.data.startswith("item_"))
async def item(cl: CallbackQuery):
    item_id = cl.data.split("_")[1]
    item = await get_item(item_id)
    await cl.message.answer(f"Название: {item.name}\n"
                            f"Описание: {item.description}\n\n"
                            f"Цена: {item.price}", reply_markup=await back_category(item.category))

    await cl.answer("")

async def back_category(category_id):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data=f"category_{category_id}"))
    return keyboard.as_markup()