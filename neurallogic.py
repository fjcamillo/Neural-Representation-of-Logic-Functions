import numpy as np

class Neural:
    """Creates a Perceptron then returns the result of the perceptron using the data
    you declared
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, weights, bias, x):
        """Initializes the Neural Class
        
        Arguments:
            weights {list} -- List of doubles containing all the weights
            bias {double} -- Data Bias
            x {np.array} -- Dataset
        """
        self.weights = np.array(list(weights), dtype=np.double).reshape(len(weights), 1)
        self.x = np.array(x)
        self.bias = bias
        self.logit = self.perceptron()
        

    def perceptron(self):
        """Builds the Perceptron
        
        Returns:
            np.array -- numpy array containing all the answers that the perceptron gave
        """
        model = self.x.dot(self.weights) + self.bias
        logit = 1/(1+np.exp(-model))
        return logit

    def __wshape__(self):
        """Retrieves the shape of the weights
        
        Returns:
            tuple -- shape of the weights
        """
        return self.weights.shape

    def __xshape__(self):
        """Retrieves the shape of the dataset
        
        Returns:
            tuple -- shape of the dataset
        """
        return self.x.shape
    
    def __converted__(self):
        """Converts the output of the perceptron into a rounded version
        
        Returns:
            numpy array -- array of the rounded up results of the perceptron
        """
        return np.round(self.logit)
