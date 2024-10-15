import time

def Sled_Matrix():
	start = time.time()
	print('След Матрицы (МОДУЛЬ_С):')
	matrix = [[1, 1, 1, 1],
		      [1, 2, 1, 1],
		      [1, 1, 3, 1],
		      [1, 1, 1, 4]
		      ]
	sled_result = 0
	print('Матрица: ')
	for tabl in matrix:
		print(tabl)
	print('Диагональ матрицы: ')
	for i in range(len(matrix)):
		sled_result += matrix[i][i]
		print(matrix[i][i])
	
	print('Результат: ',sled_result)
	finish = time.time()
	res = finish - start
	res_msec = res * 1000
	print('Время работы в миллисекундах: ', res_msec)
	
	print('Запись в файл: Смотреть время в файл time.txt')
	f = open('time.txt', 'a')
	f.write('Время работы МОДУЛЬ_C: ' + str(res_msec) + ' мс' + '\n')
	f.close()
	print('\n')
