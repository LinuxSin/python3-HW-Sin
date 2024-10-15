import time

def Proizved_Matrix_Vectr():
	start = time.time()
	print('Произведение <Матрица-вектор> (МОДУЛЬ_B):')
	Vector_1 = [1, 1, 1]
	print('Вектор: ', Vector_1 )
	
	matrix = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
	print('Матрица: ')
	for tabl in matrix:
		print(tabl)
	
	result = [0, 0, 0]
	
	for i in range(len(matrix)):            # Проходим по кол-во строк матрицы matrix
		for j in range(len(matrix[0])):     # Проходим по кол-во столбцов матрицы matrix
			result[i] += matrix[i][j] * Vector_1[j]
	print('Результат: ')
	print(result)
	finish = time.time()
	res = finish - start
	res_msec = res * 1000
	print('Время работы в миллисекундах: ', res_msec)
	
	print('Запись в файл: Смотреть время в файл time.txt')
	f = open('time.txt', 'a')
	f.write('Время работы МОДУЛЬ_B: ' + str(res_msec) + ' мс' + '\n')
	f.close()
	print('\n')



