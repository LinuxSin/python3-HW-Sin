import math
import time
def Filter_Vectr():
	start = time.time()
	vector = [1, 2, 3]
	yadro_vector = [-1, 0, 1]
	res_1 = 0
	res_2 = 0
	res_3 = 0
	print('Вектор: ', vector)
	print('Ядро: ', yadro_vector)
	res_1 = vector[0] * yadro_vector[1] + vector[1] * yadro_vector[2]
	res_2 = vector[0] * yadro_vector[0] + vector[1] * yadro_vector[1] + vector[2] * yadro_vector[2]
	res_3 = vector[1] * yadro_vector[0] + vector[2] * yadro_vector[1]
	print(f'Результат: ', res_1, res_2, res_3)
	finish = time.time()
	res = finish - start
	res_msec = res * 1000
	print('Время работы в миллисекундах: ', res_msec)
	
	print('Запись в файл: Смотреть время в файл time.txt')
	f = open('time.txt', 'a')
	f.write('Время работы МОДУЛЬ_F: ' + str(res_msec) + ' мс' + '\n')
	f.close()
	print('\n')
	
	
	
# 	print('Фильтрация вектора ядерным фильтром (МОДУЛЬ_F):')
# 	vector = [1, 2, 3, 4, 5]
# 	kernel = [-1, 0, 1]
# 
# # Длина исходного вектора и ядра
# 	vector_length = len(vector)
# 	kernel_length = len(kernel)
# 
# # Результирующий вектор
# 	result_length = vector_length + 1  # Выход за пределы вектора
# 	result = [0] * result_length
# 
# # Основной алгоритм
# 	for i in range(result_length):
#     # Переменная для хранения суммы
# 		sum_value = 0
# 		for j in range(kernel_length):
#         # Индекс по исходному вектору
# 			vector_index = i + j - 1  # Смещение для реализации выходов за пределы
# 
#         # Проверяем, находится ли индекс в пределах вектора
# 			if 0 <= vector_index < vector_length:
# 				sum_value += vector[vector_index] * kernel[j]
# 
#     # Сохраняем результат
# 		result[i] = sum_value
# 
# # Вывод результата
# 	print(result)
# 
