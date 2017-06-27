import numpy as np
from functools import reduce


def perceptron(weight, bias, x):
    logit = np.sum(np.add(np.dot(x, weight), bias))
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
