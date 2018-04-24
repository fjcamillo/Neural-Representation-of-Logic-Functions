import numpy as np

class NeuralLogic:

    def __init__(self, weights, bias, x):
        self.weights = np.array(weights)
        self.x = np.array(x)
        self.bias = bias
        

    def perceptron(self):
        model = self.weights.transpose().dot(self.x) + self.bias
        logit = 1/(1+np.exp(-model()))
        return logit

