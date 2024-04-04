from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_name = "category-1"

item_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад", callback_data=category_name)],
])