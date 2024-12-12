"""
Шаблонный метод (Template method)
"""
import cv2
import numpy as np

# --------------------------------------------- Декоратор
# #---------------- Добавьте возможность вычисления параметров объектов (моменты hu):
# ------------------OpenCV: Image Moments




# -------------------------------------------------------------------------------------
class ObjectAnalysis(object):
    def template_method(self, image):
        image = self.noise_filtering(image)
        data = self.segmentation(image)
        data = self.object_parameters(data)

        return data

    def noise_filtering(self, image):
        raise NotImplementedError()

    def segmentation(self, data):
        raise NotImplementedError()

    def object_parameters(self, data):
        (image, data) = data
        (numLabels, labels, stats, centroids) = data
        x = []
        y = []
        w = []
        h = []
        area = []
        for i in range(1, numLabels):
            # extract the connected component statistics for the current
            # label
            x.append(stats[i, cv2.CC_STAT_LEFT])
            y.append(stats[i, cv2.CC_STAT_TOP])
            w.append(stats[i, cv2.CC_STAT_WIDTH])
            h.append(stats[i, cv2.CC_STAT_HEIGHT])
            area.append(stats[i, cv2.CC_STAT_AREA])

        return (x, y, w, h, area)


class BinaryImage(ObjectAnalysis):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        median = cv2.medianBlur(image, 5)
        return median

    def segmentation(self, image):
        output = cv2.connectedComponentsWithStats(
            image,
            4, # connectivity
            cv2.CV_32S)
        return (image, output)
# ----------------------------------------- Фильтр Гаусса OpenCV: Smoothing Images ----------------------------------------
# class MonochromeImage(BinaryImage):
#     def __init__(self):
#         pass
# 
#     def noise_filtering(self, image):
#         gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
#         return gaussian_blur
# 
#     def segmentation(self, image):
#         output = cv2.connectedComponentsWithStats(
#             image,
#             4,
#             cv2.CV_32S)
#         return (image, output)
# ------------------------------------ Выделение границ Canny -------------------------------------------------
class MonochromeImage(BinaryImage):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
        return gaussian_blur

    def segmentation(self, image):
        # Используем алгоритм Canny для выделения границ
        edges = cv2.Canny(image, 100, 200)

        # Для совместимости с остальными методами, используем connectedComponentsWithStats
        output = cv2.connectedComponentsWithStats(
            edges,
            4,
            cv2.CV_32S
        )
        return (edges, output)



#  ---------------------------------------- Сегментация: конвертация в монохром ( GrayScale), ----
#                                            применение алгоритма distance transform + watershed OpenCV:
# ---------------------------------------   Image Segmentation with Distance Transform and Watershed Algorithm  ---

class ColorImage(MonochromeImage):
    def __init__(self):
        pass
    def noise_filtering(self, image):
        # Применение фильтра Гаусса для удаления шумов
        gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
        return gaussian_blur

    def segmentation(self, image):
        # Шаг 1: Конвертация в градации серого
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Шаг 2: Применение бинаризации Otsu
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Шаг 3: Distance Transform
        dist_transform = cv2.distanceTransform(binary, cv2.DIST_L2, 5)

        # Шаг 4: Нормализация distance transform
        cv2.normalize(dist_transform, dist_transform, 0, 1.0, cv2.NORM_MINMAX)

        # Шаг 5: Бинаризация distance transform
        _, sure_fg = cv2.threshold(dist_transform, 0.4, 1.0, cv2.THRESH_BINARY)

        # Шаг 6: Определение фона
        sure_fg = np.uint8(sure_fg)
        sure_bg = cv2.dilate(binary, np.ones((3, 3), np.uint8), iterations=3)
        unknown = cv2.subtract(sure_bg, sure_fg)

        # Шаг 7: Маркировка условной водораздела
        _, markers = cv2.connectedComponents(sure_fg)
        markers = markers + 1
        markers[unknown == 255] = 0

        # Шаг 8: Watershed
        cv2.watershed(image, markers)
        image[markers == -1] = [255, 0, 0]  # Цвет границ

        output = cv2.connectedComponentsWithStats(np.uint8(markers == 1), 4, cv2.CV_32S)

        return (image, output)

"""
Декоратор - структурный паттерн
"""

class FilteredAnalysis(ObjectAnalysis):
    def __init__(self, obj):
        self._proc = obj

    def template_method(self, image):
        (_x, _y, _w, _h, _area) = self._proc.template_method(image)
        x = []
        y = []
        w = []
        h = []
        area = []
       

        for i in range(len(_area)):
            if _area[i] > 10 and _area[i] < 2500:
                x.append(_x[i])
                y.append(_y[i])
                w.append(_w[i])
                h.append(_h[i])
                area.append(_area[i])
                

        return (x,y,w,h,area)


if __name__== '__main__':
    print(f'Monochrome Image Processing')
    mono_segm = MonochromeImage()
    (x,y,w,h, area) = mono_segm.template_method(cv2.imread('../data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]]) 
    
    print('\n')
    # filt_bin = FilteredAnalysis(BinaryImage())
    # (x, y, w, h, area) = filt_bin.template_method(cv2.imread('../data/1.jpg', cv2.IMREAD_GRAYSCALE))
    
    print("Binary Image Processing")
    bin_segm = BinaryImage()
    (x,y,w,h,area) = bin_segm.template_method(cv2.imread('../data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
            print([x[i], y[i], w[i],h[i],area[i]])

    print("Decorated Binary Image Processing")
    filt_bin = FilteredAnalysis(BinaryImage())
    (x, y, w, h, area) = filt_bin.template_method(cv2.imread('../data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
            print([x[i], y[i], w[i],h[i],area[i]])
            
            
    print('\n')        
    print(f'Color Image Processing')
    color_segm = ColorImage()
    (x, y, w, h, area) = color_segm.template_method(cv2.imread('../data/1.jpg'))
    for i in range(len(area)):
            print([x[i], y[i], w[i], h[i], area[i]])       
