from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Товар 1", callback_data="item-1")],
    [InlineKeyboardButton(text="Товар 2", callback_data="item-2")]

])