import asyncio # это acyncio для асинхронного бота
from PIL import Image,ImageDraw # библиотека PIl для работы с изображение и image это для работы с фото а imageDraw это чтобы рисовать изображение

import math # я незнаю
import io # для чтения байтов в памяти зачем непомню уже
def RGB_color(color_name:str) -> tuple: # это функция для работы с цветами
    color_c = {
        'blue': (0,0,255), # сдесь такие циферки потомучто например 0,0,255 это blue потомучто пк непонимает например карсный он понимает только цыфры вот я и взял такие цыфры потомучто эти цыфры это цыета
        'red': (255,0,0),
        'green': (0,255,0) 
    }
    return color_c.get(color_name) # это вернуть получить color name непомню зачем
def draw_serpinski(draw,top,left,right,depth,color): # здесь создаем серпинского
    if depth == 0: # это глубина рекурсии скорее всего 0
        draw.polygon([top,left,right],outline=color,fill=color) # нарисуйте многоугольник это и в многоугольнике же есть верх низ лево право и в конце делаем на него цвета
    else: # это если глубина рекурсии не 0 а другая
        mid_left = ((top[0]+left[0])//2,(top[1]+left[1])//2) # это все формулы для генерации серпинского и они должы быть все разные потомучто нет смысла делать одно и тоже все должы быть разные это же бесконечное множество серпинского
        mid_right = ((top[0]+right[0])//2,(top[1]+right[1])//2)
        mid_botton = ((left[0]+right[0])//2,(left[1]+right[1])//2)
        draw_serpinski(draw,top,mid_left,mid_right,depth -1,color) # это му рисуем серпинского и указываем все что есть верх низ и тд главное чтобы неповторялась
        draw_serpinski(draw,mid_left,left,mid_botton,depth -1,color)
        draw_serpinski(draw,mid_right,mid_botton,right,depth -1,color)
def generait_serpinski(size:tuple,color:str,depth:int) -> io.BytesIO: # это мы генерируем серпинского
    width, height = size # 'это размер ширины и высоты
    image = Image.new('RGB',(width,height)) #это мы ширину высоту создаем на белом фоне
    draw = ImageDraw.Draw(image) # тут уже рисуем то что создавали в переменной imge
    rgb_color = RGB_color(color) # здесь мы функцию вставляем и говорим color 
    # depth = depth.get('depth',5)
    line = 50 # линия 50 непомню зачем
    top = (width //2,line) # наверху ширину делим на 2 а линия 50 остаеться
    left = (line, height -line) # здесь мы указывает линию высоту - линиию линия у нас 50
    right = (width-line,height - line) # здесь мы ширину-линию 50 и потом высоту -линию 50
    draw_serpinski(draw,top,left,right,depth,rgb_color) # сдесь мы все обьединяем все что есть мы нарисовали
    image_byte = io.BytesIO() # делаем изображение в байтах
    image.save(image_byte,format='PNG') # сохраняем изображение в байтах в формате пнг
    image_byte.seek(0) # непонмню уже делаем изображение в байтах и ищем 0
    return image_byte # это возвращаем изображение в байтах
def rgb_color(color_name:str) -> tuple:
    color_s = {
        'blue': (0,0,255),
        'red': (255,0,0),
        'green': (0,255,0)
    }
    return color_s.get(color_name)
def genraitate_mandelbrot(max_it,color_name,pixel_x:int,pixel_y:int,width:int,height:int,center_x: float = -0.5,center_y:float = 0.0,scale:float = 1.0):
    math_x = (pixel_x / width - 0.5) * (3.5 / scale) + center_x
    math_y = (pixel_y / height - 0.5) * (2.0 / scale) + center_y
    zx,zy = 0,0
    ite = 0
    while ite < max_it:
        if zx*zx + zy*zy > 4:
            break
        newz = zx*zx - zy*zy + math_x
        newy = 2*zx*zy + math_y
        zx,zy = newz,newy
        ite +=1
    if ite == max_it:
        return(0,0,0)
    else:
        base_color = rgb_color(color_name)
        intens = min(1.0,ite / 50)
        r = int(base_color[0] * intens)
        g = int(base_color[1] * intens)
        b = int(base_color[2] * intens)
    return(r,g,b)
def draw_mandelbrot(max_it,color_name,width=512,height=512,x=-0.5,y=0.0,scale=1.0) -> io.BytesIO:
    image = Image.new('RGB',(width,height))
    for p in range(width):
        for y in range(height):
            color = genraitate_mandelbrot(color_name=color_name,
                                         pixel_x=p,
                                          pixel_y=y,
                                          width=width,
                                          height=height,
                                          scale=scale,
                                          max_it=max_it)
            image.putpixel((p,y),color)  
    image_byte = io.BytesIO() 
    image.save(image_byte,format='PNG') 
    image_byte.seek(0)
    return image_byte
def generait_julia(color_name,pixle_x,pixle_y,width,height,c_real,c_imag,max_interations = 100,scale=1.0):
    math_x = (pixle_x / width - 0.5) * (3.5 / scale)
    math_y = (pixle_y / height - 0.5) * (2.0 / scale)
    zx,zy = math_x,math_y
    ite = 0
    while ite < max_interations:
        if zx*zx + zy*zy > 4:
            break
        newz = zx*zx - zy*zy + c_real
        newy = 2*zx*zy + c_imag
        zx,zy = newz,newy
        ite += 1
    if ite == max_interations:
        return (0,0,0)
    else:
        base_color = rgb_color(color_name)
        intens = min(1.0, ite / 50)
        r = int(base_color[0] * intens)
        g = int(base_color[1] * intens)
        b = int(base_color[2] * intens)
        return (r, g, b)
def draw_julia(color_name,width,height,c_real,c_imag,max_interations = 100,scale=1.0) -> io.BytesIO:
    image = Image.new('RGB',(width,height))
    for p in range(width):
        for y in range(height):
            color = generait_julia(color_name=color_name,
                                          pixle_x=p,
                                          pixle_y=y,
                                          width=width,
                                          height=height,
                                          scale=scale,
                                          max_interations=max_interations,
                                          c_real=c_real,
                                          c_imag=c_imag)
            image.putpixel((p,y),color)  
    image_byte = io.BytesIO() 
    image.save(image_byte,format='PNG') 
    image_byte.seek(0)
    return image_byte
def generait_koch(start,end,depth):
    if depth == 0:
        return [start,end]
    else:
        x1,y1 = start
        x2,y2 = end
        p1 = (x1 + (x2 - x1) / 3,y1+ (y2 - y1) / 3)
        p2 = (x1 + 2 *(x2 - x1) / 3,y1+ 2 * (y2 - y1) / 3)
        angle = math.atan2(y2 - y1,x2 - x1)
        lenght = math.sqrt((x2 - x1) **2 + (y2 - y1)**2) / 3
        px = p1[0] + lenght * math.cos(angle + math.pi/3)
        py = p1[1] + lenght * math.sin(angle + math.pi/3)
        peak = (px,py)
        return (generait_koch(start,p1,depth-1)[:-1]+
                generait_koch(p1,peak,depth-1)[:-1]+
                generait_koch(peak,p2,depth-1)[:-1]+
                generait_koch(p2,end,depth-1))
def draw_koch(color_name,width=512,height=512,depth=4,line_wight=2):
    image = Image.new('RGB',(width,height))
    draw = ImageDraw.Draw(image)
    base_color = rgb_color(color_name)
    center_x,center_y = width / 2,height / 2 
    size = min(width,height) * 0.4
    sides = [
        ((center_x,center_y - size),(center_x + size * 0.866, center_y + size * 0.5)),
        ((center_x + size * 0.866, center_y + size * 0.5),(center_x - size * 0.866,center_y + size * 0.5)),
        ((center_x - size * 0.866,center_y + size * 0.5),(center_x,center_y - size))
    ]
    for start,end in sides:
        points = generait_koch(start,end,depth)
        for i in range(len(points) - 1):
            x1,y1 = points[i]
            x2,y2 = points[i + 1]
            draw.line([(x1,y1),(x2,y2)],fill=base_color,width=line_wight)
    image_byte = io.BytesIO()
    image.save(image_byte, format='PNG')
    image_byte.seek(0)
    return image_byte
def generate_pythagoras_tree(x, y, length, angle_deg, depth):
    if depth == 0:
        return []
    
    angle_rad = math.radians(angle_deg)
    end_x = x + length * math.cos(angle_rad)
    end_y = y - length * math.sin(angle_rad)
    
    branch_angle = 45
    scale = 0.7
    next_depth = depth - 1
    next_length = length * scale
    
    return [(x, y, end_x, end_y)] + \
           generate_pythagoras_tree(end_x, end_y, next_length, angle_deg + branch_angle, next_depth) + \
           generate_pythagoras_tree(end_x, end_y, next_length, angle_deg - branch_angle, next_depth)
def draw_pifagor(color_name,width=512,height=512,depth=4,lines_width=2):
    start_x = width // 2
    start_y = height - 50
    start = min(width,height) // 4
    lines = generate_pythagoras_tree(start_x,start_y,start,90,depth)
    image = Image.new('RGB',(width,height))
    draw = ImageDraw.Draw(image)
    color = rgb_color(color_name)
    for x1,y1,x2,y2 in lines:
        draw.line([(x1,y1),(x2,y2)],fill=color,width=lines_width)
    image_byte = io.BytesIO()
    image.save(image_byte, format='PNG')
    image_byte.seek(0)
    return image_byte




