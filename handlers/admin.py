from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from settings import ADMIN_ID
from models.base import Histori,engine
from sqlalchemy.orm import Session
router = Router()

@router.message(Command('stats'))
async def admin_stats(message:Message):
    user = message.from_user.id
    if ADMIN_ID == user:
        with Session(bind=engine) as db:
            total = db.query(Histori).count()
            await message.answer(f"🎨 Всего сгенерировано фракталов: {total}")
            records = db.query(Histori).all()
            counter = {}
            for record in records:
                if record.parameters:
                    fractal_type = record.parameters.get('Fractal')
                    if fractal_type:
                        counter[fractal_type] = counter.get(fractal_type,0) +1
            if counter:
                response =  "🏆 ТОП-3 ФРАКТАЛОВ:\n\n"
                sorted_counter = sorted(counter.items(),key=lambda x:x[1],reverse=True)
                top3 = sorted_counter[:3]
                medals = ["🥇", "🥈", "🥉"]
                for i,(fractal,count) in enumerate(top3):
                    medal = medals[i] if i < 3 else "•"
                    response += f"{medal} {fractal}: {count} раз\n"
            else:
                response = "📭 Нет данных для топа фракталов"
            await message.answer(response)
    else:
        await message.answer('вы не админ')