# Representing Logic Gates using a Neural Network

# How to use

In the example below we've created a simple `Logic And` using our class

```python
>>> from neurallogic import Neural
>>> bias = -0.2
>>> weights = [-0.1 , 0.2, 0.2]
>>> import numpy as np
>>> dataset = np.array([
...     [1,0,0],
...     [1,0,1],
...     [1,1,0],
...     [1,1,1]
... ])
>>> neural = Neural(weights, bias, dataset)
>>> neural.logit
array([[0.42555748],
       [0.47502081],
       [0.47502081],
       [0.52497919]])
>>> neural.__converted__()
array([[0.],
       [0.],
       [0.],
       [1.]])
```

Here's another example in creating a simple `Logic Or` using our class

```python
>>> from neurallogic import Neural
>>> import numpy as np
>>> bias = -0.1
>>> weights = [-0.1, 0.7,0.7]
>>> dataset = np.array([
...     [1,0,0],
...     [1,0,1],
...     [1,1,0],
...     [1,1,1]
... ])
>>> neural = Neural(weights, bias, dataset)
>>> neural.logit
array([[0.450166  ],
       [0.62245933],
       [0.62245933],
       [0.76852478]])
>>> neural.__converted__()
array([[0.],
       [1.],
       [1.],
       [1.]])
>>> 
```

