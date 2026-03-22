from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

keyboard_fractal = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🎯 Мандельброт',callback_data='Fractal:mandelbrot'),
                                                     InlineKeyboardButton(text='🌀 Жюлиа',callback_data='Fractal:julia')],
                                                     [InlineKeyboardButton(text='🔺 Серпинский',callback_data='Fractal:serpinski'),
                                                     InlineKeyboardButton(text='❄️ Кох',callback_data='Fractal:koch')],
                                                     [InlineKeyboardButton(text='🌳 Дерево Пифагора',callback_data='Fractal:pifagor')]])


kebyoard_size = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='512x512',callback_data='size:512'),
                                                     InlineKeyboardButton(text='1024x1024',callback_data='size:1024'),
                                                     InlineKeyboardButton(text='2048x2048',callback_data='size:2048')]])

keyboard_color = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='синий',callback_data='color:blue'),
                                                     InlineKeyboardButton(text='красный',callback_data='color:red'),
                                                     InlineKeyboardButton(text='зеленый',callback_data='color:green')]])


