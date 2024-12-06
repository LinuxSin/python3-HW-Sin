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
