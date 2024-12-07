from city.person import Person

class City():
    __max_count = 100
    __free_city_space = 100
    __cur_count = 0

    def __init__(self, name, count):
        try:                                                             # 
            if not isinstance(name, str):                                #
                raise TypeError('Имя должно быть строкой')                 # Обработка возможных исключений
            if not isinstance(count, int) or count < 0:                  #
                raise ValueError('Count должно быть неотрицательным целым числом') #
            val = min(count, City.__free_city_space)
            self._name = name
            self._max_count = val
            self._cur_count = 0
            City.__free_city_space -= val
        except(TypeError, ValueError) as e:
            print(f'Ошибка инициализации: {e}')

    def add_person(self):
        try:
            if(self._cur_count < self._max_count):
                self._cur_count += 1
                City.__cur_count += 1
                return True
            else:
                raise OverflowError('Невозможно добавить больше людей. В городе нет мест')
        except OverflowError as e:
            print(f'Добавление ошибки пользователя: {e}')
            return False

    def remove_person(self):
        try:
            if(self._cur_count > 0):
                self._cur_count -= 1
                City.__cur_count -= 1
                return True
            else:
                raise ValueError('Невозможно удалить человека, кол-во людей в городе уже ноль')
        except ValueError as e:
            print(f'Remove person error: {e}')
            return False
  
    def __str__(self):
        s = []
        s.append("------------------------ \n")
        s.append("Agglomeration: \n")
        s.append("------------------------\n")
        s.append("\n")
        s.append("Max_person_count: {}\n".format(City.__max_count))
        s.append("Free_counts_for_city: {}\n".format(City.__free_city_space))
        s.append("Agglomeration resident count: {}\n".format(City.__cur_count))
        s.append("\n")

        s.append("------------------------ \n")
        s.append("City: \n")
        s.append("------------------------\n")
        s.append("\n")
        s.append("Name: {}\n".format(self._name))
        s.append("Max_person_count: {}\n".format(self._max_count))
        s.append("Cur_count: {}\n".format(self._cur_count))
        s.append("\n")

        return ''.join(s)
