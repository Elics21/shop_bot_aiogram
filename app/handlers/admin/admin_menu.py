from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from app.keyboards.admin.admin_menu import admin_menu_kb
from app.states.state_add_category import StateAddCategory
from app.database.requests import set_category
from config import ADMINS

rt = Router()

@rt.message(Command("admin"))
async def admin_menu(m: Message):
    if m.from_user.id in ADMINS:
        await m.answer("Добро пожаловать в админ меню!", reply_markup=admin_menu_kb)

@rt.message(StateFilter(None), F.text == "Добавить категорию")
async def add_category(m: Message, state: FSMContext):
    if m.from_user.id in ADMINS:
        await m.answer("Введите название категории:")
        await state.set_state(StateAddCategory.GET_NAME)

@rt.message(StateAddCategory.GET_NAME)
async def get_category_name(m: Message, state: FSMContext):
    # await state.update_data(category_name = m.text)
    # data = await state.get_data()
    # await m.answer(f"Вы ввели название: {data["category_name"]}")
    await set_category(m.text)
    await m.answer(f"Категория '{m.text}' успешно добавленна!")
    # await state.clear()
