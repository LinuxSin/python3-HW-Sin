
class Person:
    def __init__(self, _name, _surname,_midname):
        print("Creation person with name {} {} {} is in process".format(_name, _surname, _midname))
        self._name = _name
        self._surname = _surname
        self._middle_name = _midname

    def __str__(self):
        return "{} {} {}".format(self._name, self._surname, self._middle_name)

    def __del__(self):
        print("Person {} {} {} was removed".format(self._name, self._surname, self._middle_name))

