from aiogram import Router
from app.handlers.user.basic import rt as basic_rt
from app.handlers.user.menu import rt as menu_rt
from app.handlers.user.category import rt as category_rt
from app.handlers.user.items import rt as items_rt
from app.handlers.admin.admin_menu import rt as admin_rt

router = Router()
router.include_routers(basic_rt, menu_rt, category_rt, items_rt, admin_rt)


