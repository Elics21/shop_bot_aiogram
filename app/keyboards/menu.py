from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Категория-1", callback_data="category-1")],
    [InlineKeyboardButton(text="Категория-2", callback_data="category-2")],
    [InlineKeyboardButton(text="Категория-3", callback_data="category-3")],
])