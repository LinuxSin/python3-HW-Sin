# from city.person import Person
# 
# class Family:
#     def __init__(self, surname):
#         self._surname = surname
#         self._members = []
# 
#     def add_member(self, name, middle_name=None):
#         if middle_name is None:
#             middle_name = self._generate_middle_name()
#         person = Person(name, self._surname, middle_name)
#         self._members.append(person)
# 
#     def _generate_middle_name(self):
#         if self._members:
#             # Let’s derive a middle name from the first member’s name
#             return self._members[0]._name
#         return ""
# 
#     def remove_member(self, name):
#         self._members = [member for member in self._members if member._name != name]
# 
#     def __str__(self):
#         members_str = ', '.join(str(member) for member in self._members)
#         return f"Family '{self._surname}': {members_str}" if members_str else f"Family '{self._surname}' has no members"
# 
#     def __del__(self):
#         print(f"Family {self._surname} was deleted")
# ---------------------------------------------------------------------------------------------
from city.person import Person

class Family:
    def __init__(self, surname):
        self._surname = surname
        self._members = []

    def add_member(self, name, middle_name=None):
        try:
            if not name:
                raise ValueError("Имя не может быть пустым")

            if middle_name is None:
                middle_name = self._generate_middle_name()

            person = Person(name, self._surname, middle_name)
            self._members.append(person)
        except Exception as e:
            print(f"Не удалось добавить жителя: {e}")

    def _generate_middle_name(self):
        try:
            if self._members:
                # Let’s derive a middle name from the first member’s name
                return self._members[0]._name
            return ""
        except IndexError:
            print("Ошибка создания отчества - нет доступных жителей")
            return ""

    def remove_member(self, name):
        try:
            if not name:
                raise ValueError("Имя не может быть пустым")

            original_count = len(self._members)
            self._members = [member for member in self._members if member._name != name]

            if len(self._members) == original_count:
                print(f"No member with the name '{name}' was found.")
        except Exception as e:
            print(f"Не удалось удалить жителя: {e}")

    def __str__(self):
        try:
            members_str = ', '.join(str(member) for member in self._members)
            return f"Family '{self._surname}': {members_str}" if members_str else f"Family '{self._surname}' has no members"
        except Exception as e:
            return f"Ошибка создания строки семьи: {e}"

    def __del__(self):
        print(f"Family {self._surname} was deleted.")
