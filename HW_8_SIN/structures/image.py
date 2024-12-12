# import cv2
# 
# """
# Абстрактная фабрика 
# """
# 
# class AbstractFactoryImageReader():
#     def read_image(self, file_path):
#         raise NotImplementedError()
# 
# class BinImageReader(AbstractFactoryImageReader):
#     def read_image(self, file_path):
#         raise NotImplementedError()
# 
# class MonochromeImageReader(AbstractFactoryImageReader):
#     def read_image(self, file_path):
#         image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
#         return image
# 
# class ColorImageReader(AbstractFactoryImageReader):
#     def read_image(self, file_path):
#         raise NotImplementedError()
# 
# def get_image_reader(ident):
#     if ident == 0:
#         return BinImageReader()
#     elif ident == 1:
#         return MonochromeImageReader()
#     elif ident == 2:
#         return ColorImageReader()
# 
# if __name__ == "__main__":
#     try:
#         for i in range(3):
#             print(get_image_reader(i))
#     except Exception as e:
#         print(e)

# --------------------------------------------------------------------

import cv2
"""
Абстрактная фабрика 
"""

class AbstractFactoryImageReader():
    def read_image(self, file_path):
        raise NotImplementedError()

class BinImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        # Читаем изображение в режиме бинарного (черно-белого) изображения
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        return binary_image

class MonochromeImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        # Читаем изображение в режиме монохромного (оттенки серого) изображения
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        return image

class ColorImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        # Читаем изображение в цветном режиме
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        return image

def get_image_reader(ident):
    if ident == 0:
        return BinImageReader()
    elif ident == 1:
        return MonochromeImageReader()
    elif ident == 2:
        return ColorImageReader()
    else:
        raise ValueError("Unknown image reader identifier")

if __name__ == "__main__":
   try:
        
        file_path = "/home/sin/Desktop/PYTHON/HW_8_SIN/structures/1.jpg"
        for i in range(3):
            reader = get_image_reader(i)
            print(f"Using {reader.__class__.__name__}")
            try:
                image = reader.read_image(file_path)
                print(f"Successfully read image with {reader.__class__.__name__}")
            except ValueError as ve:
                print(ve)
                
   except Exception as e:
        print(f"Error: {e}")
