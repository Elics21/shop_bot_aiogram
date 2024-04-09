from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

admin_menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Управление категориями")],
    [KeyboardButton(text="Управление товарами")],
    [KeyboardButton(text="Посмотреть пользователей")]
], resize_keyboard=True)

admin_change_category_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Добавить категорию")],
    [KeyboardButton(text="Удалить категорию")],
    [KeyboardButton(text="Изменить категорию")],
], resize_keyboard=True)

async def admin_delete_categoryes_kb(categoryes: List[str]):
    keyboard = InlineKeyboardBuilder()
    for category in categoryes:
        keyboard.add(InlineKeyboardButton(text=category, callback_data=f"del_category_{category}"))
    return keyboard.adjust(1).as_markup()

async def admin_change_categoryes_kb(categoryes: List[str]):
    keyboard = InlineKeyboardBuilder()
    for category in categoryes:
        keyboard.add(InlineKeyboardButton(text=category, callback_data=f"change_category_{category}"))
    return keyboard.adjust(1).as_markup()
