from Image import BinaryImage
from Image import MonochromeImage
from Image import ColorImage

from Convertor import Convertor

if __name__ == "__main__":

    convertor = Convertor()

    binary_data = [0, 255, 0, 255, 255, 0, 0, 255, 0]
    monochrome_data = [50, 100, 150, 200, 50, 100, 150, 200, 50]
    color_data = [[100, 150, 200], [200, 100, 50], [50, 50, 50],
                  [255, 255, 255], [0, 0, 0],      [128, 128, 128],
                  [100, 50, 150],  [50, 150, 200], [200, 100, 50]]
    
    palette = {i: [i, 255 - i, i // 2] for i in range(256)}

    binary_image = BinaryImage(3, 3, binary_data)
    monochrome_image = MonochromeImage(3, 3, monochrome_data)
    color_image = ColorImage(3, 3, color_data)

    print("\nИсходное бинарное изображение:")
    binary_image.display()

    print("\nИсходное монохромное изображение:")
    monochrome_image.display()

    print("\nИсходное цветное изображение:")
    color_image.display()

    print("\nМонохромное в монохромное:")
    monochrome2monochrome_image = convertor.to_monochrome(monochrome_image)
    monochrome2monochrome_image.display()

    print("\nЦветное в монохромное:")
    color2monochrome_image = convertor.to_monochrome(color_image)
    color2monochrome_image.display()

    print("\nМонохромное в цветное:")
    monochrome2color_image = convertor.to_color(monochrome_image, palette)
    monochrome2color_image.display()

    print("\nМонохромное в бинарное:")
    monochrome2binary_image = convertor.to_binary(monochrome_image, threshold=100)
    monochrome2binary_image.display()

    print("\nБинарное в монохромное:")
    binary2monochrome_image = convertor.to_monochrome(binary_image)
    binary2monochrome_image.display()

    print("\nЦветное в бинарное:")
    color2binary_image = convertor.to_binary(color_image, threshold=128)
    color2binary_image.display()

    print("\nБинарное в цветное:")
    binary2color_image = convertor.to_color(binary_image, palette)
    binary2color_image.display()
