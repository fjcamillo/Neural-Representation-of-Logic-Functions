import numpy as np
from functools import reduce


def perceptron(weight, bias, x):
    model = np.sum(np.add(np.dot(x, weight), bias))
    logit = 1/1+np.exp(model)
    return logit

def main():
    logic = {
        'logic_and' : {
            'w1': -20,
            'w2': 10,
        },
        'logic_or': {
            'w1': 20,
            'w2': 10,
        },
        'logic_not': {
            'w1': 10,
        },
        'bias': 1
    }
    dataset = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ])

    #Logic AND
    weights = np.array([logic['logic_and']['w1'],logic['logic_and']['w2']])
    print(weights)
    neuron = perceptron(weights, logic['bias'], dataset)
    print(neuron)
    #Logic OR
    # weights = np.array([logic['logic_or']])
    # neuron = perceptron(weights, logic['bias'], dataset)



if __name__ == '__main__':
    main()
