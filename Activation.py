import numpy as np

class Degree:
    def __init__(self):
        self.threshold = 0

    def f(self, x: np.array):
        for el in x:
            if el > self.threshold:
                return 1
            else:
                return 0