from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

keyboard_gotovo = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='➡️ ДАЛЕЕ')]])

keyboard_replay = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🔁 Повтор',callback_data='replay')]])
