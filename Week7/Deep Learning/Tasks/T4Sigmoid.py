# Use NumPy to calculate sigmoid:

# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))


# Try:

# print(sigmoid(0))
# print(sigmoid(5))
# print(sigmoid(-5))


# Observe the outputs.



# 1. Create the Sigmoid function
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# The formula is:

# 2. Try the three values
print(sigmoid(0))
print(sigmoid(5))
print(sigmoid(-5))

# You should get approximately:

# 0.5
# 0.9933071490757152
# 0.006692850924284855
# 🧠 What should you observe?
# Input x	Sigmoid output	Meaning
# 0	0.5	Exactly in the middle
# 5	0.9933	Very close to 1
# -5	0.0067	Very close to 0

# The key idea is:

# Large negative ───────── 0 ───────── Large positive
#        ↓                  ↓                  ↓
#       ~0                 0.5                ~1

# So Sigmoid converts any number into a value between 0 and 1.

# That's why it is commonly useful for binary classification output, where we can interpret the output as a probability-like score.

# For example:

# sigmoid(5)   → 0.9933 → very high probability of class 1
# sigmoid(-5)  → 0.0067 → very low probability of class 1

# One important thing to remember from your neuron exercises:

# ReLU: negative → 0, positive → same value
# Sigmoid: negative → close to 0, zero → 0.5, positive → close to 1