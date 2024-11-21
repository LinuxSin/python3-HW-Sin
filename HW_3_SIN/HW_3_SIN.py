#  №1 Реализовать функцию (или набор функций), которые выводят на экран таблицы
# умножения, деления, вычитания, сложения для чисел 1..9. Выбор таблицы осуществляется
# пользователем.
'''
def tabl_Umnojeniy():
	print('Таблица умножения: ')
	for i in range(1, 10):
		for j in range(1, 10):
			result = i * j
			print(f'{i}*{j} = {result}')
		print()
# tabl_Umnojeniy()

def tabl_Deleniy():
	print('Таблица деления: ')
	for i in range(1, 10):
		for j in range(1, 10):
			result = i / j if j !=0 else 'undefined'
			print(f"{i} / {j} = {result}")
		print()
# tabl_Deleniy()

def tabl_summ():
	print('Таблица сложения: ')
	for i in range(1, 10):
		for j in range(1, 10):
			result = i+j
			print(f'{i} + {j} = {result}')
		print()
# tabl_summ()

def tabl_raznost():
	print('Таблица вычитания: ')
	for i in range(1, 10):
		for j in range(1, 10):
			result = i - j
			print(f'{i} - {j} = {result}')
		print()
# tabl_raznost()
print('Выберите таблицу: ')
def vybor():
	print('1. Умножение')
	print('2. Деление')
	print('3. Сложение')
	print('4. Вычитание')
	
	vbr = input ('Введите номер таблицы: ')
	if vbr == '1':
		tabl_Umnojeniy()
	elif vbr == '2':
		tabl_Deleniy()
	elif vbr == '3':
		tabl_summ()
	elif vbr == '4':
		tabl_raznost()
vybor()
'''
# 2
# Реализуйте функции:
# a.
# Создающая вектор заданной длины N, заполнение – случайные числа от 0..1
# b.
# Создающая матрицу MxN, заполнение – случайные числа 0..1
# c.
# Умножающая матрицу на вектор (см. предыдущее ДЗ)
# d.
# Печатающую матрицу
# e.
# Печатающую вектор
# f.
# Находящую сумму диагональных элементов матрицы
# g.
# Реализующая двумерную свертку изображения.
'''
import random
import math
import numpy as np
from scipy.signal import convolve2d

def function_a():
	print('function_a - Создающая вектор заданной длины N, заполнение – случайные числа от 0..1: ')
	N = int(input('Введите размерность Вектора: '))
	Vectr1 = []
	for _ in range(0, N):
		Vectr1.append(random.uniform(0, 1))
	print('Размерность Vectr1:    ', Vectr1)
function_a()
print('\n')


print('function_b - Создающая матрицу MxN, заполнение – случайные числа 0..1: ')
def function_b():
    N = int(input("Введите количество строк матрицы: "))
    M = int(input("Введите количество столбцов матрицы: "))   
    matrix = np.random.random((N, M))
    return matrix
random_matrix = function_b()
print("Случайная матрица:")
print(random_matrix)
print('\n')



def function_c():
	print('function_c - Умножающая матрицу на вектор: ')
	vector = [1, 1, 1]
	print(f'Вектор: ', vector)
	matrix = [[1, 1, 1],
		  [2, 2, 2],
		  [3, 3, 3]]
	print(f'Матрица: ')
	for mat in matrix:
		print(mat)
		result = [0, 0, 0]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result[i] += matrix[i][j]*vector[j]
	print(f'Результат: ', result)
	print('\n')
function_c()



def function_d(matrix):
	print('function_d - Печатающая матрицу: ')
	for row in matrix:
		print(' '.join(map(str, row)))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

function_d(matrix)
print('\n')


def function_e(Vectr):
	print('function_e - Печатающая вектор: ')
	print(Vectr)
Vectr = [1, 2, 3]
function_e(Vectr)
print('\n')


def function_f(Matrix):
	print('function_f -  Находящую сумму диагональных элементов матрицы ')
	print('Матрица: ')
	for row in Matrix:
		print(' '.join(map(str, row)))
	return sum(Matrix[i][i] for i in range(len(Matrix)))
Matrix = [
	[1, 1, 1],
	[2, 2, 2],
	[3, 3, 3]
	]
result = function_f(Matrix)
print('Сумма диагональных элементов: ', result)
print('\n')

def function_g():
	print('function_g - двумерная свертка изображения')
	massiv_1 = np.array([
		[1, 1, 1],
		[1, 1, 1],
		[1, 1, 1]
	])
	
	yadro = np.array([
		[1, 0, -1],
		[1, 0, -1]
	])
	
	result = convolve2d(massiv_1, yadro, mode='same', boundary='fill', fillvalue=0)
	print(result)
function_g()
'''
# №3
# В обработке изображений разделяют одноканальные и многоканальные изображения.
# Предположим, у Вас есть функция для фильтрации одноканального изображения
# (двумерная свертка). Реализуйте декоратор, позволяющий применять фильтрацию для
# многоканального случая: операцию двумерной функции необходимо применить
# поканально. Способ хранения изображения : по слоям (компонента красного цвета,
# компонента синего цвета, компонента зеленого цвета). Т.е. размерность данных [M,N,3]
'''
import numpy as np
from scipy.signal import convolve2d

def channel_filter(func):
    def wrapper(image):
        # изображение имеет размерность [M, N, 3]
        assert image.ndim == 3 and image.shape[2] == 3, "Image must have 3 channels."

        # Применяем функцию для каждого канала отдельно
        channels = [func(image[:, :, i]) for i in range(3)]

        # Собираем обратно в многоканальное изображение
        return np.stack(channels, axis=-1)
    return wrapper

@channel_filter
def function_g(channel):
    # Это внутренняя функция, которая будет применена к каждому каналу изображения
    #print('function_g - двумерная свертка изображения для одного канала')

    # Задаём некоторый массив для примера
    yadro = np.array([
        [1, 0, -1],
        [1, 0, -1]
    ])

    # Применяем двумерную свёртку
    result = convolve2d(channel, yadro, mode='same', boundary='fill', fillvalue=0)
    return result

# Пример использования
image = np.random.rand(5, 5, 3)  # Случайное изображение размеренности [M, N, 3]
filtered_image = function_g(image)
print("Filtered Image: ", filtered_image)
'''
# 4
# Реализовать функцию автоматического конвертирования для цветового вектора из модели
# RGB в модель YIQ (и обратно). Цвет кодируется вектoром из 4х значений: первые три
# компоненты- цвет, четвертая – тип (0 – RGB, 1 – YIQ).
'''
def convert_color_massiv(color_massiv):
    x, y, z, type_massiv = color_massiv
    if type_massiv == 0:  # RGB to YIQ
        # Преобразуем из RGB в YIQ
        Y = 0.299 * x + 0.587 * y + 0.114 * z
        I = 0.596 * x - 0.274 * y - 0.322 * z
        Q = 0.211 * x - 0.523 * y + 0.312 * z
        return [Y, I, Q, 1]
    elif type_massiv == 1:  # YIQ to RGB
        # Преобразуем из YIQ в RGB
        R = x + 0.956 * y + 0.621 * z
        G = x - 0.272 * y - 0.647 * z
        B = x - 1.105 * y + 1.702 * z
        return [R, G, B, 0]
rgb_massiv_red = [255, 0, 0, 0]  # Красный цвет в RGB
rgb_massiv_green = [0, 255, 0, 0]  # Зеленый цвет в RGB
rgb_massiv_blue = [0, 0, 255, 0] # Синий цвет в RGB
yiq_massiv_Y = convert_color_massiv(rgb_massiv_red)
yiq_massiv_I = convert_color_massiv(rgb_massiv_green)
yiq_massiv_Q = convert_color_massiv(rgb_massiv_blue)
print('Massiv YIQ:')
print("Y:", yiq_massiv_Y)
print('I: ', yiq_massiv_I)
print('Q: ', yiq_massiv_Q, '\n')
print('Massiv RGB: ')
converted_to_rgb_red = convert_color_massiv(yiq_massiv_Y)
converted_to_rgb_green = convert_color_massiv(yiq_massiv_I)
converted_to_rgb_blue = convert_color_massiv(yiq_massiv_Q)
print("R:", converted_to_rgb_red)
print('G: ', converted_to_rgb_green)
print('B: ', converted_to_rgb_blue)
'''
# ------------------------------------------------------------------------------------



