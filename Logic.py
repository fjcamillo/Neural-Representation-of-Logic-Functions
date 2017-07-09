import numpy as np
from functools import reduce


def perceptron(weight, bias, x):
    model = np.add(np.dot(x, weight), bias)
    print('model: {}'.format(model))
    logit = 1/(1+np.exp(-model))
    print('Type: {}'.format(logit))
    return np.round(logit)

def compute(logictype, weightdict, dataset):
    weights = np.array([ weightdict[logictype][w] for w in weightdict[logictype].keys()[::-1]])
    output = np.array([ perceptron(weights, weightdict['bias'][logictype], val) for val in dataset])
    print(logictype)
    return logictype, output

def main():
    logic = {
        'logic_and' : {
            'w0': -0.1,
            'w1': 0.2,
            'w2': 0.2
        },
        'logic_or': {
            'w0': -0.1,
            'w1': 0.7,
            'w2': 0.7
        },
        'logic_not': {
            'w0': 0.5,
            'w1': -0.7
        },
        'logic_nand': {
            'w0': 0.6,
            'w1': -0.8,
            'w2': -0.8
        },
        'logic_nor': {
            'w0': 0.5,
            'w1': -0.7,
            'w2': -0.7
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
        },
        'bias': {
            'logic_and': -0.2,
            'logic_or': -0.1,
            'logic_not': 0.1,
            'logic_xor': 1,
            'logic_xnor': 1,
            'logic_nand': 0.3,
            'logic_nor': 0.1
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
    logic_not = compute('logic_not', logic, [[1,0],[1,1]])
    logic_xor = compute('logic_xor', logic, dataset)
    logic_xnor = compute('logic_xnor', logic, dataset)
    logic_nand = compute('logic_nand', logic, dataset)
    logic_nor = compute('logic_nor', logic, dataset)

    def template(dataset, name, data):
        # act = name[6:]
        print("Logic Function: {}".format(name[6:].upper()))
        print("X0\tX1\tX2\tY")
        toPrint = ["{1}\t{2}\t{3}\t{0}".format(output, *datas) for datas, output in zip(dataset, data)]
        for i in toPrint:
            print(i)

    gates = [logic_and, logic_or, logic_xor, logic_not, logic_xnor, logic_nand, logic_nor]

    for i in gates:
        template(dataset, *i)

    # print("""
    # Logic XOR:
    # 0 0 \t {}
    # 0 1 \t {}
    # 1 0 \t {}
    # 1 1 \t {}
    # """.format(*Logic_xor)

if __name__ == '__main__':
    main()
