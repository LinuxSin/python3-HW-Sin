# from city.city import City
# import random
# from city.person import Person
# 
# 
# class CityList(City):
# 
#     def __init__(self, name, count):
#         super(CityList, self).__init__(name, count)
#         self.__person_list = []
# 
# 
#     def add_person(self, p):
#         if super(CityList, self).add_person():
#             self.__person_list.append(p)
# 
# 
#     def add_person(self, *args):
#         p = random.randint(1,100)
#         s = str(p)
#         if super().add_person():
#             self.__person_list.append(Person(s,s+s, s+s+s))
# 
# 
#     def remove_person(self, i):
#         if super(CityList,self).remove_person():
#             i = i % len(self.__person_list)
#             del self.__person_list[i]
# 
#     def __str__(self):
#         s1 = super(CityList, self).__str__()
#         s = []
#         s.append(s1)
#         s.append("List of residents \n")
# 
#         for (i,v) in enumerate(self.__person_list):
#             s.append(" - {} - {} \n".format(i,v))
# 
#         return ''.join(s)
# 
#     def __del__(self):
#         print("The city {} was deleted from agglomeration".format(self._name))
# -------------------------------------------------------------------------------------------------

from city.city import City
import random
from city.person import Person
from city.family import Family

class CityList(City):
    def __init__(self, name, count):
        super(CityList, self).__init__(name, count)
        self.__person_list = []
        self.__family_list = []

    def add_family(self, surname, members):
        if sum(len(f._members) for f in self.__family_list) + len(members) <= self._max_count:
            family = Family(surname)
            for member in members:
                family.add_member(member)
            self.__family_list.append(family)

    def remove_family(self, surname):
        self.__family_list = [f for f in self.__family_list if f._surname != surname]

    def __str__(self):
        s1 = super(CityList, self).__str__()
        s = [s1]
        s.append("List of families\\n")
        for family in self.__family_list:
            s.append(str(family) + "\\n")
        return ''.join(s)

    def __del__(self):
        print(f"The city {self._name} was deleted from agglomeration")
