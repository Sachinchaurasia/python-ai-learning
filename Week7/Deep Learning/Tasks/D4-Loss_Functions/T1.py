# 🔥 TASK 1 — MSE Manually

# Given:

# Actual:
# [10, 20, 30]

# Prediction:
# [8, 18, 33]

# Calculate:

# 1. Errors
# 2. Squared errors
# 3. Mean Squared Error

# Then verify using:

# np.mean((actual - prediction) ** 2)

import numpy as np
actual=np.array([10,20,30])
prediction=np.array([8,18,33])

print("Errors",actual-prediction)
print("Squared Errors",(actual-prediction)**2)

mse=np.mean((actual-prediction)**2)
print("MSE",mse)
