from aiogram import Router
from app.handlers.basic import rt as basic_rt

router = Router()
router.include_routers(basic_rt)


