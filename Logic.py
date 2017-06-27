import numpy as np
from functools import reduce


def perceptron(weight, bias, x):
    model = np.sum(np.add(np.dot(x, weight), bias))
    logit = 1/1+np.exp(model)
    return logit

def main():
    logic = {
        'logic_and' : {
            'w1': ,
            'w2': ,
        },
        'logic_or': {
            'w1': ,
            'w2': ,
        }
        'logic_not': {
            'w1': ,
        }
    }
    dataset = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ])
    

if __name__ == '__main__':
    main()
