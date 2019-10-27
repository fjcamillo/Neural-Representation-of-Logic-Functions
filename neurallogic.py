import numpy as np

class Neural:
    """Creates a Perceptron
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, weights, bias, x):
        """[summary]
        
        Arguments:
            weights {[type]} -- [description]
            bias {[type]} -- [description]
            x {[type]} -- [description]
        """
        self.weights = np.array(list(weights), dtype=np.double).reshape(len(weights), 1)
        self.x = np.array(x)
        self.bias = bias
        self.logit = self.perceptron()
        

    def perceptron(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """
        model = self.x.dot(self.weights) + self.bias
        logit = 1/(1+np.exp(-model))
        return logit

    def __wshape__(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """
        return self.weights.shape

    def __xshape__(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """
        return self.x.shape
    
    def __converted__(self):
        return np.round(self.logit)
