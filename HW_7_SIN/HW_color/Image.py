class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.data = []
    def display_info(self):
        print(f"Image width: {self.width}, height: {self.height}")

class BinaryImage(Image):
    def __init__(self, width, height, data):
        super().__init__(width, height)
        self.data = data
    def display(self):
        for i in range(self.height):
            print(' '.join(str(self.data[i * self.width + j]) for j in range(self.width)))

class MonochromeImage(Image):
    def __init__(self, width, height, data):
        super().__init__(width, height)
        self.data = data
    def display(self):
        for i in range(self.height):
            print(' '.join(str(self.data[i * self.width + j]) for j in range(self.width)))

class ColorImage(Image):
    def __init__(self, width, height, data):
        super().__init__(width, height)
        self.data = data
    def display(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                r, g, b = self.data[i * self.width + j]
                row.append(f"[{r},{g},{b}]")
            print(' '.join(row))
# --------------------------------------------------------------------------------------------------------

# class Image:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         if not isinstance(self.width, int) or not isinstance(self.height, int):
#             raise ValueError("Ширина и высота должны быть целыми числами")
#         if self.width <= 0 or self.height <= 0:
#             raise ValueError("Ширина и высота должны быть положительными целыми числами")
#         self.size = width * height
#         self.data = []
# 
#     def display_info(self):
#         print(f"Image width: {self.width}, height: {self.height}")
# 
# class BinaryImage(Image):
#     def __init__(self, width, height, data):
#         super().__init__(width, height)
#         if not isinstance(data, list):
#             raise TypeError("Данные должны быть списком")
#         if len(data) != self.size:
#             raise ValueError("Длина данных не соответствует размеру изображения")
#         if not all(d in (0, 1) for d in data):
#             raise ValueError("Данные двоичного изображения должны содержать только 0 и 1")
#         self.data = data
# 
#     def display(self):
#         try:
#             for i in range(self.height):
#                 print(' '.join(str(self.data[i * self.width + j]) for j in range(self.width)))
#         except IndexError as e:
#             print(f"Ошибка отображения изображения: {e}")
# 
# class MonochromeImage(Image):
#     def __init__(self, width, height, data):
#         super().__init__(width, height)
#         if not isinstance(data, list):
#             raise TypeError("Данные должны быть списком")
#         if len(data) != self.size:
#             raise ValueError("Длина данных не соответствует размеру изображения")
#         if not all(isinstance(d, int) and 0 <= d <= 255 for d in data):
#             raise ValueError("Данные монохромного изображения должны быть целыми числами от 0 до 255.")
#         self.data = data
# 
#     def display(self):
#         try:
#             for i in range(self.height):
#                 print(' '.join(str(self.data[i * self.width + j]) for j in range(self.width)))
#         except IndexError as e:
#             print(f"Ошибка отображения изображения: {e}")
# 
# class ColorImage(Image):
#     def __init__(self, width, height, data):
#         super().__init__(width, height)
#         if not isinstance(data, list):
#             raise TypeError("Данные должны быть списком")
#         if len(data) != self.size:
#             raise ValueError("Длина данных не соответствует размеру изображения")
#         if not all(isinstance(d, tuple) and len(d) == 3 and all(isinstance(c, int) and 0 <= c <= 255 for c in d) for d in data):
#             raise ValueError("Данные цветного изображения должны представлять собой список кортежей по три целых числа в каждом (0–255).")
#         self.data = data
# 
#     def display(self):
#         try:
#             for i in range(self.height):
#                 row = []
#                 for j in range(self.width):
#                     r, g, b = self.data[i * self.width + j]
#                     row.append(f"[{r},{g},{b}]")
#                 print(' '.join(row))
#         except IndexError as e:
#             print(f"Ошибка отображения изображения: {e}")
