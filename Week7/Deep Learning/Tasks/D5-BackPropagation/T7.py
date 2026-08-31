# TASK 7 — Explain Without Looking

# Here are the answers in simple words, so you can understand and explain them yourself.

# 1. What is backpropagation?

# Backpropagation is the process of sending the error from the output layer backward through the neural network to calculate how much each weight contributed to the error.

# In simple words:

# The model looks at its mistake and works backward to find which weights need to change and by how much.

# 2. What is a gradient?

# A gradient tells us how the loss changes when a weight changes.

# It also tells us the direction in which the loss increases.

# For example:

# Gradient = +5
# → Loss increases when weight increases

# Gradient = -5
# → Loss decreases when weight increases

# So we use the gradient to know which direction to move the weight.

# 3. What does a positive gradient mean for gradient descent?

# If the gradient is positive, gradient descent subtracts a positive value:

# $$ w_{new}=w-\text{positive value} $$

# Therefore, the weight decreases.

# Positive gradient
#        ↓
# Subtract it
#        ↓
# Weight decreases
# 4. What does a negative gradient mean?

# If the gradient is negative, we subtract a negative number.

# $$ w_{new}=w-(-\text{value}) $$

# Subtracting a negative becomes addition.

# Therefore, the weight increases.

# Negative gradient
#        ↓
# Subtract negative
#        ↓
# Weight increases

# Just like your previous task:

# $$ 0.8-(0.1\times-0.3)=0.83 $$

# So 0.8 → 0.83.

# 5. What is the learning rate?

# The learning rate controls how big a step the model takes when changing its weights.

# Small learning rate
# → Small updates
# → Slow learning

# Large learning rate
# → Large updates
# → Faster, but potentially unstable

# For example:

# Learning rate = 0.001 → 🐢
# Learning rate = 0.01  → 🚶
# Learning rate = 0.1   → 🏃
# 6. What is gradient descent?

# Gradient descent is an optimization algorithm that changes the weights in the direction that reduces the loss.

# Its basic idea is:

# Calculate loss
#      ↓
# Calculate gradient
#      ↓
# Move weight in the opposite direction
#      ↓
# Loss becomes smaller
#      ↓
# Repeat

# The goal is to find weights that give low loss.

# 7. What is the difference between backpropagation and gradient descent?

# This is very important.

# Backpropagation	Gradient Descent
# Calculates the gradients	Uses the gradients
# Finds how each weight affects the loss	Updates the weights
# Works backward through the network	Moves weights toward lower loss
# Answers: "How should each weight change?"	Answers: "Let's change the weights."
# Easy analogy 🧠

# Imagine you're going down a mountain:

# Backpropagation:

# "Which direction is downhill?"

# Gradient descent:

# "Okay, I'll take a step downhill."

# So:

# Backpropagation calculates the information needed for the update; gradient descent performs the update.

# 8. Why should the loss generally decrease during successful training?

# Because the purpose of training is to make the model's predictions closer to the correct answers.

# For example:

# Before training:

# Prediction = 1
# True value = 10
# Loss = 81

# After learning:

# Prediction = 6
# True value = 10
# Loss = 16

# Later:

# Prediction ≈ 10
# True value = 10
# Loss ≈ 0

# So successful training generally looks like:

# HIGH LOSS
#    ↓
#    ↓
#    ↓
# LOWER LOSS
#    ↓
#    ↓
# LOW LOSS
# 🔥 One-line summary

# Backpropagation calculates gradients, gradient descent uses those gradients to update weights, and the learning rate controls the size of those updates so that the loss can generally decrease.

# 🧠 Your 8 answers in ultra-short form
# Backpropagation → Calculates gradients by working backward through the network.
# Gradient → Tells how the loss changes with respect to a weight.
# Positive gradient → Weight decreases.
# Negative gradient → Weight increases.
# Learning rate → Controls the size of weight updates.
# Gradient descent → Updates weights to reduce loss.
# Backpropagation vs Gradient Descent → Backpropagation calculates gradients; gradient descent uses them to update weights.
# Loss decreases → Because successful training makes predictions closer to the correct answers.

