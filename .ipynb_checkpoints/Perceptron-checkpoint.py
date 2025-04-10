import numpy as np
from Activations import Degree

class Perceptron:
    def __init__(self):
        self.w= np.random.uniform(-0.5, 0.5, 3)
        print(f'Pesos iniciais: {self.w}')
        self.learning_rate= 0.1
        
    def fit(self, X, y, activation) -> list[int]:
        x = np.insert(X, 0, 1, axis=1)

        epoch= 0
        convergence= False
        adjusts = 0
        
        while not convergence:
            convergence = True
            
            for i in range(len(X)):
                u = np.dot(x[i], self.w)
        
                y_predicted = activation.f(u)
                error = y[i] - y_predicted
                
                if error != 0:
                    convergence = False
                    self.w = self.w + self.learning_rate * error * x[i]
                    adjusts += 1
                
        
            epoch += 1
            
        print(f'Pesos após o treino: {self.w}')

        return epoch, adjusts
        