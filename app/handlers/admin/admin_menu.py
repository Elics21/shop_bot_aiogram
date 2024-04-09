from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from app.keyboards.admin.admin_menu import admin_menu_kb, admin_change_category_kb, admin_delete_categoryes_kb
from app.states.state_add_category import StateAddCategory
from app.database.requests import set_category, get_categories, delete_categories
from config import ADMINS

rt = Router()

@rt.message(Command("admin"))
async def admin_menu(m: Message):
    if m.from_user.id in ADMINS:
        await m.answer("Добро пожаловать в админ меню!", reply_markup=admin_menu_kb)

@rt.message(F.text == "Управление категориями")
async def change_categorys(m: Message):
    if m.from_user.id in ADMINS:
        await m.answer("Выберите действие:", reply_markup=admin_change_category_kb)

@rt.message(StateFilter(None), F.text == "Добавить категорию")
async def add_category(m: Message, state: FSMContext):
    if m.from_user.id in ADMINS:
        await m.answer("Введите название категории:")
        await state.set_state(StateAddCategory.GET_NAME)

@rt.message(StateAddCategory.GET_NAME)
async def get_category_name(m: Message, state: FSMContext):
    await set_category(m.text)
    await m.answer(f"Категория '{m.text}' успешно добавленна!", reply_markup=admin_change_category_kb)
    await state.clear()

@rt.message(F.text == "Удалить категорию")
async def print_categorys_to_delete(m: Message, falg=False):
    if m.from_user.id in ADMINS:
        categoryes = await get_categories()
        categoryes_list = [i.name for i in categoryes]
        if not falg:
            await m.answer("Выберите категорию которую нужно удалить:",
                           reply_markup=await admin_delete_categoryes_kb(categoryes_list))
        else:
            await m.edit_text("Выберите категорию которую нужно удалить:",
                           reply_markup=await admin_delete_categoryes_kb(categoryes_list))
@rt.callback_query(F.data.startswith("del_category_"))
async def delete_category(cl: CallbackQuery):
    if cl.from_user.id in ADMINS:
        category = cl.data.split("_")[2]
        await delete_categories(category)
        await cl.answer("")
        await cl.message.edit_text("Успешно удалено!")

@rt.message(F.text == "Управление товарами")
async def change_items(m: Message):
    if m.from_user.id in ADMINS:
        pass
@rt.message(F.text == "Посмотреть пользователей")
async def print_users(m: Message):
    if m.from_user.id in ADMINS:
        pass
