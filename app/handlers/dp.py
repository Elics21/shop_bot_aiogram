from aiogram import Router
from app.handlers.basic import rt as basic_rt
from app.handlers.menu import rt as menu_rt
from app.handlers.category import rt as category_rt
from app.handlers.items import rt as items_rt

router = Router()
router.include_routers(basic_rt, menu_rt, category_rt, items_rt)


