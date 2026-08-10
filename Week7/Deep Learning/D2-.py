import numpy as np

# Inputs
x = np.array([2, 3])

# Weights
w = np.array([0.5, 0.4])

# Bias
b = 0.2

# Weighted sum
z = np.dot(x, w) + b

print("Weighted Sum:", z)

def relu(x):
    return max(0, x)

output = relu(z)

print("ReLU Output:", output)

#Try a negative Example
x = np.array([2, 3])

w = np.array([-0.5, -0.4])

b = 0.2

z = np.dot(x, w) + b

print("Weighted Sum:", z)
print("ReLU Output:", relu(z))