def Gistograms():
	print('Расчет гистограммы для вектора (МОДУЛЬ_e): ')
	print('\n')
# 	Vectr = [1, 2, 3, 4]
# 	print('вектор: ', Vectr)
# 	max_element = max(Vectr)
# 	print('Максимальный элемент: ',max_element)
# 	min_element = min(Vectr)
# 	print('Минимальный элемент: ', min_element)
# 	
# 	shirina_interval = max_element - min_element
# 	print('Ширина интервала: ', shirina_interval)
# 	def calculate_histogram(data, num_bins):
#     # 1. Определить минимальное и максимальное значение
# 		min_value = float('inf')
# 		max_value = float('-inf')
# 		for num in data:
# 			if num < min_value:
# 				min_value = num
# 			if num > max_value:
# 				max_value = num
# 
#     # 2. Рассчитать ширину интервала
# 		range_value = max_value - min_value
# 		bin_width = range_value / num_bins
# 
#     # 3. Подсчитать значения в каждом интервале
# 		histogram = [0] * num_bins
# 		for num in data:
#         # Определить индекс интервала, в который попадает элемент
# 				if num == max_value:
#             # Обработка случая, когда число равно максимальному значению
# 					index = num_bins - 1
# 				else:
# 					index = int((num - min_value) / bin_width)
# 					histogram[index] += 1
# 
#     # 4. Печать результатов
# 		for i in range(num_bins):
# 			bin_start = min_value + i * bin_width
# 			bin_end = bin_start + bin_width
# 			print(f'Interval {i+1}: [{bin_start}, {bin_end}) - Count: {histogram[i]}')
# 
# # Пример использования
# 	data_vector = [1.0, 2.5, 3.5, 4.0, 5.5, 2.5, 3.0, 4.5, 6.0, 7.5, 8.0]
# 	num_bins = 5
# 	calculate_histogram(data_vector, num_bins)
