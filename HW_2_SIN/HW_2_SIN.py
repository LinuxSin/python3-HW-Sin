# №1 Напишите программу, в которой в бесконечном цикле пользователь вводит
# два числа, а программа выводит их сумму.
'''
while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a+b
    print("Summ: ", c )
'''
# -----------------------------------------------------------
# №2 Используйте циклы, чтобы вывести на консоль следующий набор символов:
# *  1  *  2  * 
# 3  *  4  *  5 
# *  6  *  7  * 
# 8  *  9  *  10 
# *  11 * 12  *
'''
a=5 
b=1
counter = 1
for i in range(a):
	for j in range(a):
		if b % 2 == 0:
			print(counter, end=" ")
			counter+=1
		else: print("*", end=" ")
		b+=1
	print()
'''
# -----------------------------------------------------------
# ----------------------------------------------------------------------------------------------
#  №3 Реализуйте программу «угадай число». Пользователь загадывает число, на входе
# указывает интервал, в котором находится загаданное число. Программа «угадывает» число
# до тех пор, пока не выдаст корректный ответ. Допустимые вопросы: Число равно N? Число
# меньше N? (возможно использовать метод дихотомии)
'''
import random
chislo = int(input('Введите число в диапазоне от 1 до 50: '))
a = 1 
b = 50
pr = random.randint (a,b)


if chislo == pr:
	print('Победа!')
else:
	while pr != chislo:
		if chislo > pr:
			print('Загаданное число больше: ', pr)
			a=pr
			pr=random.randint(a,b)
		
		elif chislo < pr:
			print ('Загаданное число меньше: ', pr)
			b = pr
			pr = random.randint(a,b)
			
	print(chislo)
	print ('Првыильно!')
'''


# # ----------------------------------------------------------------------------------------------


#  №4 Пользователь вводит числа, больше 0, критерий окончания ввода – число 0 Вывести
#  наибольшее среди всех чисел.

# 
# print('Введите натуральные числа через пробел: ')
# i = 0
# a = int(input())
# max_value = a
# while a != 0:
#    
#     a = int(input())
#     max_value = max(max_value, a)
# 
# print('Максимальное значение: ', max_value)

# -----------------------------------------------------------------------------------------------

# №5 Выведите на экран таблицу умножения чисел от одного до девяти.
'''
for a in range(1,10):
    for b in range(1,10):
        print("%4d" % (a*b), end='')
    print()
'''
# ----------------------------------------------------------------------------------------------

# ----------------------------------- СПИСКИ ------------------------------------------

# №1 Задан список чисел, представляющий собой выборку некой случайной величины. Найти
# минимальное значение в списке, максимальное, медиану. +++++++
'''
list_1=[7,2,9,3,23,5,4,1]
n = len(list_1)
max_element = max(list_1)
min_element = min(list_1)
list_1.sort()
print('Максимально значение: ', max_element)
print('Минимальное значение: ', min_element)
print('Отсортированный список: ', list_1)
i = n // 2
if n % 2 == 0:
	mediana = (list_1[i - 1] + list_1[i]) / 2
else:
	mediana = list_1[i]
print(f"Медиана: ", mediana)
'''


# -------------------------------------------------------------------------------------

# №2 Задан список из 20 элементов. Каждый элемент – число от 0 до 100 Рассчитать
# гистограмму значений, квантованную по числу 10: 1й бин – количество элементов списка в
# диапазоне [0,9], 2й бин – количество элементов списка в диапазоне [10,19]... Вывести
# результат. Перевести количество в вероятности встречаемости значения из диапазона.
# Вывести результат.

'''
list1 = [1, 100, 25, 4, 37, 6, 41, 8, 9, 88, 47, 12, 53, 68, 15, 74, 17, 99, 19, 20]
print('Список: ', list1)
print('Гистограмма: ')
bin1 = 0
dlina_list1 = 0
for i in list1:
	if 0 <= i <= 9:
		bin1 +=1
	dlina_list1 +=1
print('Диапазон [0, 9]: ', bin1)
ver1 = bin1 / dlina_list1

bin2 = 0
for i in list1:
	if 10 <= i <= 19:
		bin2 +=1
	dlina_list1 +=1
print('Диапазон [10, 19]: ', bin2)
ver2 = bin2 / dlina_list1

bin3 = 0
for i in list1:
	if 20 <= i <= 29:
		bin3 +=1
	dlina_list1 +=1
print('Диапазон [20, 29]: ', bin3)
ver3 = bin3 / dlina_list1

bin4 = 0
for i in list1:
	if 30 <= i <= 39:
		bin4 +=1
	dlina_list1 +=1
print('Диапазон [30, 39]: ', bin4)
ver4 = bin4 / dlina_list1

bin5 = 0
for i in list1:
	if 40 <= i <= 49:
		bin5 +=1
	dlina_list1 +=1
print('Диапазон [40, 49]: ', bin5)
ver5 = bin5 / dlina_list1

bin6 = 0
for i in list1:
	if 50 <= i <= 59:
		bin6 +=1
	dlina_list1 +=1
print('Диапазон [50, 59]: ', bin6)
ver6 = bin6 / dlina_list1

bin7 = 0
for i in list1:
	if 60 <= i <= 69:
		bin7 +=1
	dlina_list1 +=1
print('Диапазон [50, 59]: ', bin7)
ver7 = bin7 / dlina_list1

bin8 = 0
for i in list1:
	if 70 <= i <= 79:
		bin8 +=1
	dlina_list1 +=1
print('Диапазон [70, 79]: ', bin8)
ver8 = bin8 / dlina_list1

bin10 = 0
for i in list1:
	if 80 <= i <= 89:
		bin10 +=1
	dlina_list1 +=1
print('Диапазон [80, 89]: ', bin10)
ver10 = bin10 / dlina_list1

bin11 = 0
for i in list1:
	if 90 <= i <= 99:
		bin11 +=1
	dlina_list1 +=1
print('Диапазон [90, 99]: ', bin11)
ver11 = bin11 / dlina_list1

bin12 = 0
for i in list1:
	if 100 <= i <= 110:
		bin12 +=1
	dlina_list1 +=1
print('Максимальное значение 100: ', bin12)
ver12 = bin12 / dlina_list1

print('Вероятности: ')
print('Диапазон [0, 9]: ', ver1)
print('Диапазон [10, 19]: ', ver2)
print('Диапазон [20, 29]: ', ver3)
print('Диапазон [30, 39]: ', ver4)
print('Диапазон [40, 49]: ', ver5)
print('Диапазон [50, 59]: ', ver6)
print('Диапазон [60, 69]: ', ver7)
print('Диапазон [70, 79]: ', ver8)
print('Диапазон [80, 89]: ', ver10)
print('Диапазон [90, 99]: ', ver11)
print('Максимальное значение 100: ', ver12)
'''



# -------------------------------------------------------------------------------------

# №3 Заданы два вектора, размерности N. Найти покомпонентные сумму, умножение, вывести
# результат. Для вектора с бОльшей нормой рассчитать результат умножения на скаляр.
# Скаляр, размерность задаются из консоли. Заполнение векторов – при помощи генератора
# псевдослучайных чисел. +++++++
'''
import random
import math

N = int(input('Введите размерность N: '))
Vectr1 = []
Vectr2 = []

for _ in range(0, N):
	Vectr1.append(random.randint(1,5))
	Vectr2.append(random.randint(1,5))
print('Размерность Vectr1:    ', Vectr1)
print('Размерность Vectr2:    ', Vectr2)

Vectr3 = [0] * len(Vectr1) # новый вектор для хранения результатов суммы
for i in range(len(Vectr1)):
	Vectr3[i] = Vectr1[i] + Vectr2[i]
print('Покомпонентная сумма: ', Vectr3)

Vectr4 = [0] * len(Vectr1) # новый вектор для хранения результатов произведения
for i in range(len(Vectr1)):
	Vectr4[i] = Vectr1[i] * Vectr2[i]
print('Покомпонентное умножение: ', Vectr4)

sum_kvdrt_vectr1 = 0
for i in Vectr1:
	sum_kvdrt_vectr1 += i **2
dlin1 = sum_kvdrt_vectr1 ** 0.5
print("Длина (норма) вектора Vectr1: ", dlin1)

sum_kvdrt_vectr2 = 0
for i in Vectr2:
	sum_kvdrt_vectr2 += i **2
dlin2 = sum_kvdrt_vectr2 ** 0.5
print("Длина (норма) вектора Vectr2: ", dlin2)

if dlin1 > dlin2:
	print('Vectr1 имеет большую норму: ', dlin1)
else:
	print('Vectr2 имеет большую норму: ', dlin2)

Sklr_Vectr=[]
S = int (input('Введите скаляр: '))
if dlin1 > dlin2:
	for i in Vectr1:
		Sklr_Vectr.append(i*S)
	print('Результат умножения Vectr1 на скаляр: ', Sklr_Vectr)
else:
	for i in Vectr2:
		Sklr_Vectr.append(i*S)
	print('Результат умножения Vectr2 на скаляр: ', Sklr_Vectr)
'''
# -------------------------------------------------------------------------------------

# №4 Задана матрица (двумерный список), задан вектор, размерности корректны для
# реализации математических операций. Реализовать умножение матрицы на вектор. +++++++
'''
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
'''


# -------------------------------------------------------------------------------------
#  №5 Дан список, в который могут быть включены положительные и отрицательные значения.
# Все отрицательные значения заменить на среднее среди ближайших левого и правого
# положительного значения исходного массива.
'''
list_1 = [1, -2, 5, -7, 9]
print('Изначальный список: ', list_1)
sred1 = (list_1[0] + list_1[2]) / 2
sred2 = (list_1[2] + list_1[4]) / 2
list_1[1] = sred1
list_1[3] = sred2
print('Новый список: ', list_1)
'''
# -------------------------------------------------------------------------------------
# № 6
# Дан первый список элементов: массив данных. Дан второй список элементов – ядро
# фильтра (например, длина вектора = 3). Выполнить сверточную фильтрацию элементов
# первого списка, используя элементы второго списка в качестве ядра свертки.


# --------------------------------------------------------------------------