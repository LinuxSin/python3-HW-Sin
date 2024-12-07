from city.person import Person
from city.city import City
from city.city_list import CityList
from city.family import Family

def person_test():
    try:
        p = Person('a', 'b', 'c')
        #help(p)
        #print(dir(p))
        print(p)
    except Exception as e:
        print(f"Произошла ошибка в Person: {e}")

def city_test():
    try:
        c1 = City("City1", 10)
        #print(c1)
        c2 = City("City2", 50)
        #print(c2)

        #for i in range(15):
        #    c1.add_person()

        #for i in range(5):
        #    c1.remove_person()
        #    c2.remove_person()

        #print(c1)

        c2.tmp1 = 10
        c2.tmp2 = 20

        # print(c1.__dict__)
        # print(c2.__dict__)

        # print(dir(c1))
        #print(dir(c2))

        #print(hasattr(c2, 'tmp3' ))

        #for att in dir(c2):
        #    print(att, getattr(c2, att))
    except AttributeError as ae:
        print(f"Ошибка атрибута в city: {ae}")
    except Exception as e:
        print(f"Ошибка в city: {e}")

def city_list_test():
    try:
        c3 = CityList("City_with_named_persons", 50)

        c3.add_family("Син", ["Михайловна", "Наталья"])
        c3.add_family("Ли", ["Евгеньевна", "Зоя"])

        print(c3)

        c3.remove_family("Doe")
        print(c3)
    except KeyError as ke:
        print(f"Ключевая ошибка в city_list: {ke}")
    except Exception as e:
        print(f"Произошла ошибка city_list: {e}")

if __name__ == '__main__':
    print("Program is started")
    try:
        city_list_test()
    except Exception as e:
        print(f"Ошибка в файле main.py: {e}")
    print("Работа программы завершена")
# ---------------------------------------------------------------------------------------------


