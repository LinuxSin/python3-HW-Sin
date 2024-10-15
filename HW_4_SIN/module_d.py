import time

def Sklr_Proizved_two_vectros():
	start = time.time()
	print('Скалярное произведение двух векторов (МОДУЛЬ_d):')
	vectr_1 = [1, 1, 1]
	print('Вектор 1: ', vectr_1)
	vectr_2 = [3, 2, 2]
	print('Вектор 2: ', vectr_2)
	if len(vectr_1) != len(vectr_2):
		print("Векторы должны быть одной длины")
	
	result = 0
	
	for i in range(len(vectr_1)):
		result += vectr_1[i] * vectr_2[i]
	print('Скалярное произведение = ', result)
	finish = time.time()
	res = finish - start
	res_msec = res * 1000
	print('Время работы в миллисекундах: ', res_msec)
	
	print('Запись в файл: Смотреть время в файл time.txt')
	f = open('time.txt', 'a')
	f.write('Время работы МОДУЛЬ_D: ' + str(res_msec) + ' мс' + '\n')
	f.close()
	print('\n')

