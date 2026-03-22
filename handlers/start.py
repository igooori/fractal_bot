from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.inline import keyboard_fractal
router = Router()

@router.message(Command('start'))
async def start(message:Message):
    await message.answer(
    "🎨 <b>Добро пожаловать в Генератор Фракталов!</b>\n\n"
    "✨ Этот бот создаёт удивительные математические изображения:\n"
    "• Бесконечно сложные узоры\n"
    "• Уникальные цветовые палитры\n"
    "• Профессиональная визуализация\n\n"
    "🚀 <b>Чтобы начать:</b> напишите /fractal\n\n"
    "<i>Выберите фрактал → настройте параметры → получите уникальное изображение!</i>",
    parse_mode="HTML"
)