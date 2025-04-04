import numpy as np

class Degree:
    def __init__(self):
        self.threshold = 0

    def f(self, x):
        return 1 if x > self.threshold else 0
