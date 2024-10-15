import time

def Proizved_Matrix():
	start = time.time()
	print('Произведение двух матриц (МОДУЛЬ_А): ')
	matrix_1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
	print('Матрица 1: ')
	for tabl in matrix_1:
		print(tabl)
	
	matrix_2 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
	print('Матрица 2: ')
	for tabl in matrix_2:
		print(tabl)
		
	result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	
	for i in range(len(matrix_1)):              # Проход по строкам матрицы matrix_1
		for j in range(len(matrix_2[0])):       # Проход по столбцам матрицы matrix_2
			for k in range(len(matrix_1[0])):   # Проход по каждому элементу строки матрицы matrix_1 и столбца matrix_2
				result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
	print('Результат: ')
	for tabl in result_matrix:
		print(tabl)
	finish = time.time()
	res = finish - start
	res_msec = res * 1000
	print('Время работы в миллисекундах: ', res_msec)
	
	print('Запись в файл: Смотреть время в файл time.txt')
	f = open('time.txt', 'w')
	f.write('Время работы МОДУЛЬ_А: ' + str(res_msec) + ' мс' + '\n')
	f.close()
	print('\n')












# main()

