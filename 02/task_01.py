class MedianFinder:
    def __init__(self):
        self.elements = []

    def add_num(self, x):
        self.elements.append(x)

    def find_median(self):
        self.elements.sort()
        size = len(self.elements)
        if size == 0:
            return 0.
        elif size % 2:
            return self.elements[size // 2]
        else:
            return (self.elements[size // 2 - 1] + self.elements[size // 2 - 1]) / 2
