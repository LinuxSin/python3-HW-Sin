import numpy as np
import math
import copy

from Image import BinaryImage
from Image import MonochromeImage
from Image import ColorImage

class Convertor:
    def to_binary(self, image, threshold=128):
        if isinstance(image, BinaryImage):
            return copy.deepcopy(image)

        elif isinstance(image, MonochromeImage):
            result = BinaryImage(image.width, image.height, [])
            result.data = [255 if pixel > threshold else 0 for pixel in image.data]
            return result

        elif isinstance(image, ColorImage):
            monochrome_image = self.to_monochrome(image)
            return self.to_binary(monochrome_image, threshold)

        else:
            return None

    def to_monochrome(self, image):
        if isinstance(image, MonochromeImage):
            result = MonochromeImage(image.width, image.height, [])
            histogram = {i: len([x for x in image.data if x == i]) / image.size
                         for i in range(256)}

            average_initial = np.sum([key * value for key, value in histogram.items()])
            stddev_initial = math.sqrt(np.sum([value * (key - average_initial)**2 for key, value in histogram.items()]))

            average_final = np.mean(image.data)
            stddev_final = np.std(image.data)
            result.data = list(map(int, stddev_initial * (np.array(image.data) - average_final) / stddev_final + average_initial))
            return result

        elif isinstance(image, ColorImage):
            result = MonochromeImage(image.width, image.height, [])
            result.data = [(red + green + blue) // 3 for red, green, blue in image.data]
            return result

        elif isinstance(image, BinaryImage):
            result = MonochromeImage(image.width, image.height, [0] * image.size)
            white_pixels = [(i % image.width, i // image.width)
                            for i in range(image.size) if image.data[i] == 255]

            max_distance = math.sqrt(image.width ** 2 + image.height ** 2)
            for i in range(image.size):
                if image.data[i] == 255:
                    result.data[i] = 255
                else:
                    x, y = i % image.width, i // image.width
                    distance = min(math.sqrt((x - wx) ** 2 + (y - wy) ** 2) for wx, wy in white_pixels)
                    result.data[i] = int((1 - distance / max_distance) * 255)
            return result

        else:
            return None

    def to_color(self, image, palette=None):
        if isinstance(image, ColorImage):
            # Normalize color channels to improve contrast
            result = ColorImage(image.width, image.height, [])
            data_array = np.array(image.data)
            color_channels = [data_array[:, :, i] for i in range(3)]

            corrected_channels = []
            for channel in color_channels:
                average_initial, stddev_initial = np.mean(channel), np.std(channel)
                corrected_channels.append((channel - average_initial) / stddev_initial)

            result.set_data(np.stack(corrected_channels, axis=2).astype(int).tolist())
            return result

        elif isinstance(image, MonochromeImage):
            if palette is None:
                return None
            result = ColorImage(image.width, image.height, [])
            result.data = [palette[gray] for gray in image.data]
            return result

        elif isinstance(image, BinaryImage):
            monochrome_image = self.to_monochrome(image)
            return self.to_color(monochrome_image, palette)

        else:
            return None

    def __del__(self):
        pass
