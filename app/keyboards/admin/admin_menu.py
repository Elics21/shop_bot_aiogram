from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Добавить категорию")],
    [KeyboardButton(text="Добавить товар")],
    [KeyboardButton(text="Посмотреть пользователей")]
], resize_keyboard=True)