from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

rt = Router()

@rt.callback_query(F.data == "item-1")
async def items(cl: CallbackQuery):
    await cl.message.edit_text("Item-1")
    await cl.answer("")