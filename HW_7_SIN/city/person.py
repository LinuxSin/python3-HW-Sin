
# class Person:
#     def __init__(self, _name, _surname,_midname):
#         print("Creation person with name {} {} {} is in process".format(_name, _surname, _midname))
#         self._name = _name
#         self._surname = _surname
#         self._middle_name = _midname
# 
#     def __str__(self):
#         return "{} {} {}".format(self._name, self._surname, self._middle_name)
# 
#     def __del__(self):
#         print("Person {} {} {} was removed".format(self._name, self._surname, self._middle_name))

# -------------------------------------------------------------------------------------------------------------------


class Person:
    def __init__(self, _name, _surname, _midname):
        try:
            if not all(isinstance(x, str) and x.strip() for x in [_name, _surname, _midname]):
                raise ValueError("Имя, фамилия и отчество должны быть непустыми строками")

            print("Creation person with name {} {} {} is in process".format(_name, _surname, _midname))
            self._name = _name
            self._surname = _surname
            self._middle_name = _midname

        except ValueError as e:
            print("Ошибка при создании жителя:", e)
            raise
        except Exception as e:
            print("При создании жителя произошла непредвиденная ошибка:", e)
            raise

    def __str__(self):
        try:
            return "{} {} {}".format(self._name, self._surname, self._middle_name)
        except Exception as e:
            print("Ошибка при создании строкового представления:", e)
            raise

    def __del__(self):
        try:
            print("Person {} {} {} was removed".format(self._name, self._surname, self._middle_name))
        except Exception as e:
            print("Ошибка при удалении жителя:", e)
