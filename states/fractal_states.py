from aiogram.fsm.state import State,StatesGroup
from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
router = Router()
class Fract(StatesGroup):
    type_fractal = State()
    size = State()
    color = State()
    parametrs = State()


