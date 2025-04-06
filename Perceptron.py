
import numpy as np
from Activation import Degree

class Perceptron:
    def __init__(self):
        self.w= np.random.uniform(-0.5, 0.5, 3)  # atributos + bias
        self.learning_rate= 0.1