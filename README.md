# Representing Logic Gates using a Neural Network

# How to use

```python
weights = [-0.1 , 0.2, 0.2]
bias = -0.2
dataset = np.array([
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
])
neural = Neural(weights, bias, dataset)
print(neural.logit)

#Lets try it out
```