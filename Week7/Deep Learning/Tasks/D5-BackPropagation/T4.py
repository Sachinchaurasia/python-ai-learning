# # TASK 4 — Update the Weight

# # Add:

# # learning_rate = 0.01

# # w.assign_sub(learning_rate * gradient)

# # print("New Weight:", w.numpy())

# ############################################################################

# Update the Weight

# Now we will use the gradient calculated in Task 3 to update the weight.

# Step 1 — Set the learning rate
# learning_rate = 0.01

# We have:

# Old weight = 0.5
# Gradient = -36
# Learning rate = 0.01
# Step 2 — Update the weight
# w.assign_sub(learning_rate * gradient)

# TensorFlow's assign_sub() means:

# $$ w = w - (\text{learning rate} \times \text{gradient}) $$

# So:

# $$ w = 0.5 - (0.01 \times -36) $$ $$ w = 0.5 - (-0.36) $$ $$ w = 0.5 + 0.36 $$ $$ \boxed{w=0.86} $$
# Step 3 — Print the new weight
# print("New Weight:", w.numpy())
# Expected output
# New Weight: 0.86
# 🧠 Important intuition

# The weight increased:

# Old Weight                  New Weight
#    0.50   ───────────────►    0.86
#              +0.36

# Why?

# Because the gradient was negative (-36).

# Gradient Descent subtracts the gradient. Therefore, subtracting a negative gradient makes the weight increase.

# 🔥 Connect Tasks 3 & 4
# Prediction = 1.0
#        ↓
# True Value = 10.0
#        ↓
# Loss = 81.0
#        ↓
# Gradient = -36.0
#        ↓
# Update Weight
#        ↓
# 0.50 → 0.86

# This is the core idea of learning in a neural network: calculate the error → calculate the gradient → update the weights.


