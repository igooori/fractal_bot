from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.orm import Session
from models.base import Histori,engine
from handlers.fractal import parametr
import json
router = Router()

@router.message(Command('histori'))
async def histori(message:Message):
    user_id = message.from_user.id
    with Session(bind=engine) as db:
        response = "<b>🎨 История ваших фракталов:</b>\n\n"
        histori = db.query(Histori).filter(Histori.user_id == user_id).all()
        if not histori:
            await message.answer(
                "📭 Вы ещё не создали ни одного фрактала.\n"
                "Начните с /fractal"
            )
            return
        for historis in histori:
            params = historis.parameters
            fractal_icons = {
            'julia': '🌀 Жюлиа',
            'mandelbrot': '🎯 Мандельброт',
            'serpinski': '🔺 Серпинский',
            'koch': '❄️ Кох',
            'pifagor': '🌳 Дерево Пифагора'
            }
            fractal_type = params.get('Fractal', "").lower()
            name = fractal_icons.get(fractal_type)

            response += f"<b>• {name}</b>\n"
            response += f"• Размер: <code>{params.get('size')}</code>\n"
            response += f"• Цветовая схема: <code>{params.get('color')}</code>\n"
            response += f"• Параметры: <code>{params.get('parametrs')}</code>\n"
            response += "\n"
    await message.answer(response,parse_mode='HTML')