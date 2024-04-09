from app.database.model import async_session
from app.database.model import User, Item, Category
from sqlalchemy import select, func, delete

async def set_user(tg_id, first_name, balance):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            user = User(tg_id=tg_id, first_name=first_name, balance=balance)
            session.add(user)
            await session.commit()

async def set_category(name):
    async with async_session() as session:
        category_count = await session.scalar(select(func.count(Category.id)))
        category = Category(id=category_count + 1, name=name)
        session.add(category)
        await session.commit()

async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

async def delete_categories(category_name):
    async with async_session() as session:
        await session.execute(delete(Category).where(Category.name == category_name))
        await session.commit()

async def get_category_items(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category == category_id))

async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))

async def get_user_info(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))