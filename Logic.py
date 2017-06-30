import numpy as np
from functools import reduce


def perceptron(weight, bias, x):
    model = np.sum(np.add(np.dot(x, weight), bias))
    print(model)
    logit = 1/(1+np.exp(-model))
    return logit

def main():
    logic = {
        'logic_and' : {
            'w0': -5,
            'w1': -20,
            'w2': 10
        },
        'logic_or': {
            'w0': -5,
            'w1': 20,
            'w2': 10
        },
        'logic_not': {
            'w0': 10,
            'w1': 10
        },
        'bias': 1
    }
    dataset = np.array([
        [1,0,0],
        [1,0,1],
        [1,1,0],
        [1,1,1]
    ])

    #Logic AND
    weights = np.array([logic['logic_and']['w1'],logic['logic_and']['w2']])
    first = perceptron(weights, logic['bias'], dataset[0])
    second = perceptron(weights, logic['bias'], dataset[1])
    third = perceptron(weights, logic['bias'], dataset[2])
    fourth = perceptron(weights, logic['bias'], dataset[3])
    print("""
    Logic AND:
    0 0 \t {}
    0 1 \t {}
    1 0 \t {}
    1 1 \t {}
    """.format(first, second, third, fourth))
    #Logic OR
    weights = np.array([logic['logic_or']['w1'],logic['logic_or']['w2']])
    first = perceptron(weights, logic['bias'], dataset[0])
    second = perceptron(weights, logic['bias'], dataset[1])
    third = perceptron(weights, logic['bias'], dataset[2])
    fourth = perceptron(weights, logic['bias'], dataset[3])
    print("""
    Logic OR:
    0 0 \t {}
    0 1 \t {}
    1 0 \t {}
    1 1 \t {}
    """.format(first, second, third, fourth))


if __name__ == '__main__':
    main()
