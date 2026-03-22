from aiogram import Router,F
from services.fractal_generator import generait_serpinski,draw_mandelbrot,draw_julia,draw_koch,draw_pifagor
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.fractal_states import Fract
from aiogram.types import BufferedInputFile
from keyboards.inline import keyboard_fractal,kebyoard_size,keyboard_color
from keyboards.reply import keyboard_gotovo
from sqlalchemy.orm import Session
from models.base import Histori,engine
txt = """<b>🎨 ВЫБЕРИТЕ ФРАКТАЛ</b>

🌀 <b>Доступные варианты:</b>

1. <b>Мандельброт</b> — классический фрактал
   • Итерационный
   • Настраиваемая детализация

2. <b>Жюлиа</b> — вариация Мандельброта  
   • Требует параметр C
   • Разнообразные формы

3. <b>Треугольник Серпинского</b> — рекурсивный
   • Геометрическая точность
   • Настраиваемая глубина

4. <b>Кривая Коха</b> — снежинка
   • Фрактальная линия
   • Красивые узоры

5. <b>Дерево Пифагора</b> — фрактальное дерево
   • Рекурсивное ветвление
   • Природные формы

📱 <b>Выберите фрактал:</b>"""
router = Router()
@router.message(Command('fractal'))
async def fractal(message:Message,state:FSMContext):
    await message.answer(txt,parse_mode='HTML',reply_markup=keyboard_fractal)
    await state.set_state(Fract.type_fractal)
@router.callback_query(F.data == 'Fractal:mandelbrot')
async def mandelbrot(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Fractal='mandelbrot')
    await callback.message.edit_text('✅ **ВЫБРАН МАНДЕЛЬБРОТ**',parse_mode='MarkdownV2',reply_markup=kebyoard_size)
    await state.set_state(Fract.size)
    await callback.answer()
@router.callback_query(F.data == 'Fractal:julia')
async def julia(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Fractal='julia')
    await callback.message.edit_text('✅ **ВЫБРАН Жюлиа**',parse_mode='MarkdownV2',reply_markup=kebyoard_size)
    await state.set_state(Fract.size)
    await callback.answer()
@router.callback_query(F.data == 'Fractal:serpinski')
async def serpinsk(callback:CallbackQuery,state:FSMContext):
    await state.update_data(Fractal='serpinski')
    await callback.message.edit_text('✅ **ВЫБРАН Серпинский**',parse_mode='MarkdownV2',reply_markup=kebyoard_size)
    await state.set_state(Fract.size)
    await callback.answer()
@router.callback_query(F.data == 'Fractal:koch')
async def koch(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Fractal='koch')
    await callback.message.edit_text('✅ **ВЫБРАН Кох**',parse_mode='MarkdownV2',reply_markup=kebyoard_size)
    await state.set_state(Fract.size)
    await callback.answer()
@router.callback_query(F.data == 'Fractal:pifagor')
async def pifagor(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Fractal='pifagor')
    await callback.message.edit_text('✅ **ВЫБРАН Пифагор**',parse_mode='MarkdownV2',reply_markup=kebyoard_size)
    await state.set_state(Fract.size)
    await callback.answer()
@router.callback_query(F.data == 'size:512')
async def size_512(callback: CallbackQuery, state: FSMContext):
    await state.update_data(size='512x512')
    txt = """✨ **Параметр сохранён: 512 × 512**
"""
    await callback.message.edit_text(txt,parse_mode='MarkdownV2',reply_markup=keyboard_color)
    await state.set_state(Fract.color)
    await callback.answer()
@router.callback_query(F.data == 'size:1024')
async def size_1024(callback: CallbackQuery, state: FSMContext):
    await state.update_data(size='1024x1024')
    txt = """✨ **Параметр сохранён: 1024 × 1024**
"""
    await callback.message.edit_text(txt,parse_mode='MarkdownV2',reply_markup=keyboard_color)
    await state.set_state(Fract.color)
    await callback.answer()
@router.callback_query(F.data == 'size:2048')
async def size_2048(callback: CallbackQuery, state: FSMContext):
    txt = """✨ **Параметр сохранён: 1024 × 1024**
"""
    await state.update_data(size='2048x2048')
    await callback.message.edit_text(txt,parse_mode='MarkdownV2',reply_markup=keyboard_color)
    await state.set_state(Fract.color)
    await callback.answer()
@router.callback_query(F.data == 'color:blue')
async def blue(callback: CallbackQuery, state: FSMContext):
    await state.update_data(color='blue')
    await callback.message.delete()
    await callback.message.answer(
        '✅ Цвет сохранён: синий',
        reply_markup=keyboard_gotovo
    )
    await state.set_state(Fract.parametrs)
    await callback.answer()
@router.callback_query(F.data == 'color:red')
async def red(callback: CallbackQuery, state: FSMContext):
    await state.update_data(color='red')
    await callback.message.delete()
    await callback.message.answer(
        '✅ Цвет сохранён: крсаный',
        reply_markup=keyboard_gotovo
    )
    await state.set_state(Fract.parametrs)
    await callback.answer()
@router.callback_query(F.data == 'color:green')
async def green(callback: CallbackQuery, state: FSMContext):
    await state.update_data(color='green')
    await callback.message.delete()
    await callback.message.answer(
        '✅ Цвет сохранён: зеленый',
        reply_markup=keyboard_gotovo
    )
    await state.set_state(Fract.parametrs)
    await callback.answer()
@router.message(Fract.parametrs)
async def parametr(message:Message,state:FSMContext):
    parametrs = message.text
    await state.update_data(parametrs=parametrs)
    data = await state.get_data()
    fractal_type = data.get('Fractal')
    if fractal_type == 'serpinski':
        if not message.text.isdigit():
            txt = """<b>📐 Введите глубину рекурсии:</b> от <b>0</b> до <b>10</b>

✨ <b>Что это значит?</b>
Глубина определяет, насколько детальным будет треугольник

🔄 <b>Как работает:</b>
• 0-3 — простые формы
• 4-7 — хорошо видна структура  
• 8-10 — максимальная детализация

⚠️ <b>Внимание:</b>
Глубина 10+ может создавать очень сложные изображения

🎨 <b>Рекомендации:</b>
Для первого раза попробуйте 5-7

🚀 <b>Введите число от 0 до 10:</b>"""
            await message.answer(txt,parse_mode='HTML')
            return
        elif int(message.text) > 10:
            await message.answer('❌ ошибка введите от 0 до 10')
        else:
            await message.answer('✅ Числа сохранены! Генерирую фрактал...')
            size_str = data['size']
            color = data['color']
            depth = int(message.text)
            width, height = map(int, size_str.split('x'))
            size_tuple = (width, height)
            image = generait_serpinski(size_tuple,color,depth)
            file = BufferedInputFile(image.getvalue(),filename="fractal.png")
            await message.answer_photo(file,caption='Вот твой фрактал Серпинского!')
            with Session(bind=engine) as db:
                hustori = Histori(
                    user_id = message.from_user.id,
                    parameters = data
                )
            db.add(hustori)
            db.commit()
            await state.clear()
    if fractal_type == 'mandelbrot':
        if not message.text.isdigit():
            txt = """<b>🔢 Введите число:</b> от <b>20</b> до <b>1000</b>

⚡ <b>Что это такое?</b>
Это количество итераций для расчета фрактала

📊 <b>Как влияет:</b>
✅ Больше число = больше деталей
⏱️ Больше число = дольше ждать

🎯 <b>Рекомендации по размерам:</b>
• 512x512 → 100-200
• 1024x1024 → 200-400  
• 2048x2048 → 400-800

💡 <b>Примеры:</b> 100, 250, 500, 750

🚀 <b>Вводите число:</b>"""
            await message.answer(txt,parse_mode='HTML')
            return
        elif int(message.text) < 21:
            await message.answer('❌ ошибка введите от 20 до 1000')
        elif int(message.text) > 101:
            await message.answer('❌ ошибка введите от 20 до 1000')
        else:
            await message.answer('✅ Числа сохранены! Генерирую фрактал...')
            size = data['size']
            color = data['color']
            depth = int(message.text)
            width,height = map(int,size.split('x'))
            size_tupl = (width,height)
            image = draw_mandelbrot(color_name=color,width=width,height=height,
                                    x=-0.5,y=0.0,scale=1.0,max_it=depth)
            file = BufferedInputFile(image.getvalue(),filename="fractal.png")
            await message.answer_photo(file,caption='Вот твой фрактал Мандельброт!')
            with Session(bind=engine) as db:
                hustori = Histori(
                    user_id = message.from_user.id,
                    parameters = data
                )
            db.add(hustori)
            db.commit()
            await state.clear()
    if fractal_type == 'koch':
        if not message.text.isdigit():
            txt = """<b>❄️ Введите глубину:</b> от <b>0</b> до <b>7</b>

⚡ <b>Что это такое?</b>
Уровень рекурсии для снежинки Коха

📊 <b>Как влияет:</b>
✅ Больше число = больше деталей
⏱️ Больше число = дольше ждать

🎯 <b>Рекомендации по размерам:</b>
• 512x512 - 3-5
• 1024x1024 - 4-6  
• 2048x2048 - 5-7

💡 <b>Примеры:</b> 3, 4, 5, 6

🚀 <b>Вводите глубину:</b>"""
            await message.answer(txt,parse_mode='HTML')
            return
        elif int(message.text) > 8:
            await message.answer('❌ ошибка введите от 0 до 7')
        else:
            await message.answer('✅ Числа сохранены! Генерирую фрактал...')
            size = data['size']
            color = data['color']
            depth = int(message.text)
            width,height = map(int,size.split('x'))
            image = draw_koch(color_name=color,width=width,height=height,depth=depth,line_wight=1)
            file = BufferedInputFile(image.getvalue(),filename="fractal.png")
            await message.answer_photo(file,caption='Вот твой фрактал Кох!')
            with Session(bind=engine) as db:
                hustori = Histori(
                    user_id = message.from_user.id,
                    parameters = data
            )
            db.add(hustori)
            db.commit()
            await state.clear()
    if fractal_type == 'pifagor':
        if not message.text.isdigit():
            txt = """<b>🌳 Введите глубину дерева:</b> от <b>0</b> до <b>10</b>

⚡ <b>Что это такое?</b>
Уровень рекурсии для Дерева Пифагора

📊 <b>Как влияет:</b>
✅ Больше число = больше ветвей
🌿 Больше число = пышнее крона
⏱️ Больше число = дольше ждать

🎯 <b>Рекомендации по размерам:</b>
• 512x512 - 4-6
• 1024x1024 - 5-8  
• 2048x2048 - 6-10

💡 <b>Примеры:</b> 5, 6, 7, 8

🚀 <b>Вводите глубину:</b>"""
            await message.answer(txt,parse_mode='HTML')
            return
        elif int(message.text) > 10:
            await message.answer('❌ ошибка введите от 0 до 10')
        else:
            await message.answer('✅ Числа сохранены! Генерирую фрактал...')
            size = data['size']
            color = data['color']
            depth = int(message.text)
            width,height = map(int,size.split('x'))
            image = draw_pifagor(color_name=color,width=width,height=height,depth=depth,lines_width=2)
            file = BufferedInputFile(image.getvalue(),filename="fractal.png")
            await message.answer_photo(file,caption='Вот твой фрактал Дерево пифагора!')
            await state.clear()
    if message.text == '➡️ ДАЛЕЕ':
        txt = """<b>🔢 ВВЕДИТЕ ЧИСЛО</b>

<b>📌 Диапазон:</b> от <b>-3</b> до <b>3</b>

<b>💡 Примеры:</b>
• <code>-0.7</code> — классический Жюлиа
• <code>0.285</code> — красивый фрактал
• <code>0.0</code> — симметричный вариант
• <code>-0.8</code> — популярный параметр

<b>⚠️ Важно:</b>
- Только числа (можно дробные)
- Не текст, не символы
- От <b>-3.0</b> до <b>+3.0</b>

<b>🚀 Вводите число:</b>"""
        await message.answer(txt,parse_mode='HTML')
        return
    if fractal_type == 'julia':
        parts = message.text.split()
        if len(parts) != 2:
            await message.answer('❌ Для Жюлиа нужно ДВА числа через пробел!\nПример: -0.7 0.27')
            return
        c_real = float(parts[0])
        c_image = float(parts[1])
        
        if c_real < -3 or c_real > 3:
            await message.answer('❌ ошибка введите от -3 до 3')
            return
        elif c_image < -3 or c_image > 3:
            await message.answer('❌ ошибка введите от -3 до 3')
            return
        await message.answer('✅ Числа сохранены! Генерирую фрактал...')
        size = data['size']
        color = data['color']
        width,height = map(int,size.split('x'))
        image = draw_julia(color_name=color,width=width,height=height,
                               c_real=c_real,c_imag=c_image,scale=1.0,max_interations=100)
        file = BufferedInputFile(image.getvalue(),filename="fractal.png")
        await message.answer_photo(file,caption='Вот твой фрактал Жюлиа!')
        with Session(bind=engine) as db:
            hustori = Histori(
                user_id = message.from_user.id,
                parameters = data
            )
            db.add(hustori)
            db.commit()
        await state.clear()

            