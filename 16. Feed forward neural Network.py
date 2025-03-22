import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def feedforward(inputs, weights, biases):
    layer1 = sigmoid(np.dot(inputs, weights[0]) + biases[0])
    output = sigmoid(np.dot(layer1, weights[1]) + biases[1])
    return output
np.random.seed(42)
inputs = np.array([0.5, 0.8])  
weights = [
    np.random.rand(2, 3),  
    np.random.rand(3, 1)   
]
biases = [
    np.random.rand(3),  
    np.random.rand(1)   
]
output = feedforward(inputs, weights, biases)
print("Neural Network Output:", output)
