from aiogram.fsm.state import StatesGroup, State

class StateAddCategory(StatesGroup):
    GET_NAME = State()