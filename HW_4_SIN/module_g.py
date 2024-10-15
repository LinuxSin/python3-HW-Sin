import time

def File_R_W():
	start = time.time()
	print('чтение/запись данных в файл, из файла (МОДУЛЬ_g):')
	f = open('file.txt', 'r')
	print('Чтение из файла: ', *f)
	f.close()	
	print('Запись в файл: Смотреть в файл file1.txt')
	f = open('file1.txt', 'w')
	f.write('Hello Python!')
	f.close()
	finish = time.time()
	res = finish - start
	res_msec = res * 1000
	print('Время работы в миллисекундах: ', res_msec)
	
	print('Запись в файл: Смотреть время в файл time.txt')
	f = open('time.txt', 'a')
	f.write('Время работы МОДУЛЬ_G: ' + str(res_msec) + ' мс' + '\n')
	f.close()
	print('\n')
