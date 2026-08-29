# Implement:

# import numpy as np

# x = np.array([4, 5])
# w = np.array([0.3, 0.2])
# b = 0.1

# z = np.dot(x, w) + b

# print("Weighted Sum:", z)

# output = max(0, z)

# print("ReLU Output:", output)



# 1. Create the input values
# x = np.array([4, 5])

# This represents:

# x₁ = 4
# x₂ = 5

# So:

# x = [4, 5]
# 2. Create the weights
# w = np.array([0.3, 0.2])

# This represents:

# w₁ = 0.3
# w₂ = 0.2

# So:

# w = [0.3, 0.2]
# 3. Create the bias
# b = 0.1

# The bias is simply:

# b = 0.1

# Remember the neuron formula:

# 4. Calculate the weighted sum
# z = np.dot(x, w) + b

# np.dot() performs multiplication and addition:

# np.dot([4, 5], [0.3, 0.2])

# = (4 × 0.3) + (5 × 0.2)

# = 1.2 + 1.0

# = 2.2

# Then add bias:

# 2.2 + 0.1 = 2.3

# Therefore:

# z = 2.3
# 5. Apply ReLU
# output = max(0, z)

# ReLU means:

# if z > 0 → z
# if z < 0 → 0

# Here:

# z = 2.3

# Since 2.3 > 0:

# ReLU(2.3) = 2.3
# Complete program
# import numpy as np

# x = np.array([4, 5])
# w = np.array([0.3, 0.2])
# b = 0.1

# z = np.dot(x, w) + b

# print("Weighted Sum:", z)

# output = max(0, z)

# print("ReLU Output:", output)
# Expected output
# Weighted Sum: 2.3
# ReLU Output: 2.3
# 🧠 The pattern you should remember

# Whenever you see a simple neuron:

# Inputs → Weights → Multiply → Add → Bias → Activation

# In Python/NumPy:

# z = np.dot(x, w) + b
# output = max(0, z)

# So the manual calculation and the NumPy code are doing exactly the same thing.
