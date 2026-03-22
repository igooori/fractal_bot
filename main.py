import asyncio
from aiogram import Bot,Dispatcher
from aiogram.types import BotCommand
from settings import TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.start import router as router_start
from handlers.fractal import router as router_fractal
from handlers.histori import router as histori_router
from handlers.admin import router as admin_router

async def set_my(bot:Bot):
    commands = [
        BotCommand(command='start',description='👋 Начать работу'),
        BotCommand(command='fractal',description='✨ Выбор фрактала'),
        BotCommand(command='histori',description='👥 Общая история')
    ]
    await bot.set_my_commands(commands)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
async def main():
    dp.include_router(router_start)
    dp.include_router(router_fractal)
    dp.include_router(histori_router)
    dp.include_router(admin_router)
    await set_my(bot)
    await dp.start_polling(bot)
    
asyncio.run(main())