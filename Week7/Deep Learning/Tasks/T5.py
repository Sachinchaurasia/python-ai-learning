# # TASK 5 — THINKING QUESTIONS

# # Answer these yourself:

# # 1. What is a loss function?
# # 2. Why do we need loss after forward propagation?
# # 3. When is MSE commonly used?
# # 4. When is binary cross-entropy commonly used?
# # 5. If the actual value is 1 and prediction is 0.99, should loss be high or low?
# # 6. If actual is 1 and prediction is 0.01, should loss be high or low?
# # 7. What is the difference between loss and accuracy?
# # 8. Does calculating loss itself update the weights?


# 1. What is a loss function?

# A loss function measures how wrong the model's prediction is compared to the actual answer.

# Small loss → prediction is close to the actual value.
# Large loss → prediction is far from the actual value.

# Example:

# Actual = 1
# Prediction = 0.9
# → Small loss
# 2. Why do we need loss after forward propagation?

# Forward propagation gives us the prediction, but we need to know how good or bad that prediction is.

# The loss function tells us the error:

# Input
#   ↓
# Forward Propagation
#   ↓
# Prediction
#   ↓
# Loss Function
#   ↓
# How wrong is the prediction?

# The optimizer then uses this information during training to adjust the weights.

# 3. When is MSE commonly used?

# MSE (Mean Squared Error) is commonly used for regression problems, where the model predicts continuous numerical values.

# Examples:

# Predicting salary
# Predicting house price
# Predicting temperature
# Predicting sales

# Example:

# Actual salary = ₹50,000
# Predicted salary = ₹48,000

# MSE can measure how far the prediction is from the actual value.

# 4. When is binary cross-entropy commonly used?

# Binary Cross-Entropy is commonly used for binary classification, where there are two possible classes.

# Examples:

# Spam / Not Spam
# Yes / No
# Pass / Fail
# 0 / 1
# Disease / No Disease

# Usually, the output layer has:

# Dense(1, activation="sigmoid")
# 5. If the actual value is 1 and prediction is 0.99, should loss be high or low?

# Low.

# The model predicted:

# Actual:     1
# Prediction: 0.99

# The prediction is very close to the correct answer, so the loss should be very small.

# 6. If actual is 1 and prediction is 0.01, should loss be high or low?

# High.

# The model predicted:

# Actual:     1
# Prediction: 0.01

# The model is very confident in the wrong direction, so Binary Cross-Entropy gives a large loss.

# 7. What is the difference between loss and accuracy?

# Loss measures how wrong the predictions are.

# Accuracy measures how many predictions are correct.

# For example:

# Actual:      [1, 0, 1, 0]
# Prediction:  [0.9, 0.4, 0.8, 0.3]

# After applying a classification threshold, the predictions may all be correct, giving:

# Accuracy = 100%

# But loss also considers how confident the predictions are.

# So:

# Accuracy tells us how often we're correct. Loss tells us how wrong our predictions are.

# 8. Does calculating loss itself update the weights?

# No.

# Calculating the loss only measures the error. It does not change the model's weights.

# During training, the process is roughly:

# Forward Propagation
#        ↓
# Prediction
#        ↓
# Calculate Loss
#        ↓
# Calculate Gradients
#        ↓
# Backpropagation
#        ↓
# Optimizer updates weights

# So remember:

# Loss measures the error; the optimizer updates the weights.

# 🔥 One-line summary
# Forward propagation → "What did I predict?"
# Loss function       → "How wrong am I?"
# Backpropagation      → "Which weights caused the error?"
# Optimizer            → "How should I change those weights?"