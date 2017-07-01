import numpy as np
from functools import reduce


def perceptron(weight, bias, x):
    model = np.sum(np.add(np.dot(x, weight), bias))
    logit = 1/(1+np.exp(-model))
    return logit

def compute(logictype, weightdict, dataset):
    weights = np.array([ w for w in weightdict[logictype].keys()])
    output = np.array([ perceptron(weights, weightdict['bias'][logictype], val) for val in dataset])
    return output

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
        'logic_nand': {
            'w0': -5,
            'w1': 20,
            'w2': 10
        },
        'logic_nor': {
            'w0': -5,
            'w1': 20,
            'w2': 10
        },
        'logic_xor': {
            'w0': -5,
            'w1': 20,
            'w2': 10
        },
        'logic_xnor': {
            'w0': -5,
            'w1': 20,
            'w2': 10
        }
        'bias': {
            'logic_and': 1,
            'logic_or': 1,
            'logic_not': 1,
            'logic_xor': 1,
            'logic_xnor': 1,
            'logic_nand': 1,
            'logic_nor': 1
        }
    }
    dataset = np.array([
        [1,0,0],
        [1,0,1],
        [1,1,0],
        [1,1,1]
    ])

    logic_and = compute('logic_and', logic, dataset)
    logic_or = compute('logic_or', logic, dataset)
    logic_xor = compute('logic_xor', logic, dataset)
    logic_not = compute('logic_not', logic, [[1,0],[1,1]])
    print logic_and
    # print("""
    # Logic XOR:
    # 0 0 \t {}
    # 0 1 \t {}
    # 1 0 \t {}
    # 1 1 \t {}
    # """.format(*Logic_xor)

if __name__ == '__main__':
    main()
