import pytest
from PIL import Image
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.fractal_generator import genraitate_mandelbrot,draw_mandelbrot

def test_mandelbrot():
    color = genraitate_mandelbrot(100,100,200,200) #что это за цифры откуда они взялись
    assert len(color) == 3
    r,g,b = color
    assert 0 <= r <= 255 #вопрос: зачем тут 255 откуда оно взялось
    assert 0 <= g <= 255 #впорос зачем такие больше =< зачем это надо и почему мы стравниваем с 0
    assert 0 <= b <= 255
    print('генератор мандельброт работает') #этот принт нужен чтобы понять что до сюдо дошло и в терминале ты понял что до сюда дошло значит все работает
def test_image():
    image = draw_mandelbrot(width=100,height=100) #проверка что изображение рисуеться только непомню зачем тут по 100 что эти цыфры тут делают
    assert image is not None
    assert isinstance(image,Image.Image)
    assert image.size == (100,100)
    assert image.mode == 'RGB'
    print('создание изобр работает')
def test_colors():
    color_center = genraitate_mandelbrot(100,100,200,200)
    color_corner = genraitate_mandelbrot(10,10,200,200)
    assert color_center != color_corner
    print('цвета работают')
if __name__ == '__main__':
    test_mandelbrot()
    test_image()
    test_colors()
    print('тесты успешно')

