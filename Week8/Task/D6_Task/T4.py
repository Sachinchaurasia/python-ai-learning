# 💻 TASK 4 — Tiny Python Exercise

# You don't need TensorFlow or PyTorch for this exercise.

# Run:

import numpy as np

Q = np.array([1, 0])
K1 = np.array([1, 0])
K2 = np.array([0, 1])

score1 = np.dot(Q, K1)
score2 = np.dot(Q, K2)

print("Score 1:", score1)
print("Score 2:", score2)

# You should get:

# Score 1: 1
# Score 2: 0
# Think:

# Why is:

# Q ↔ K1

# more similar than:

# Q ↔ K2

# ?

# This tiny exercise gives you the intuition behind attention scores.

###############################################################################################
