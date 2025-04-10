import numpy as np

class Perceptron:
    def __init__(self):
        self.w= np.random.uniform(-0.5, 0.5, 3)  # atributos + bias
        self.learning_rate= 0.1
        
    def set_w(self, new_w):
        if isinstance(new_w, np.ndarray) and new_w.shape == self._w.shape: 
            self._w = new_w
        else:
            raise ValueError("O peso deve ser um array NumPy do mesmo tamanho que self._w!")
            
    def set_learning_rate(self, new_learning_rate):
        if isinstance(new_learning_rate, float): 
            self.learning_rate = self.learning_rate
        else:
            raise ValueError("Valor inválido")