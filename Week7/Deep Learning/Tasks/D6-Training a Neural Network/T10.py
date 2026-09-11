# # TASK 10 — THINKING QUESTIONS

# # Answer without copying:

# # 1. What does model.fit() do?
# # 2. What is an epoch?
# # 3. What is a batch?
# # 4. What is the difference between training and testing data?
# # 5. Why do we scale numerical features?
# # 6. What does optimizer="adam" mean?
# # 7. Why do we use binary_crossentropy here?
# # 8. What is validation data?
# # 9. What does model.evaluate() do?
# # 10. What is overfitting?
# # 11. What is the difference between loss and val_loss?
# # 12. Why shouldn't we judge a model only by training accuracy?


# #################################################################################################

# 1. What does model.fit() do?

# model.fit() trains the neural network. It gives the model the training inputs (X_train) and correct answers (y_train) so that the model can adjust its weights and learn patterns.

# 2. What is an epoch?

# An epoch means the model has gone through the entire training dataset once.

# For example:

# epochs=50

# means the model gets 50 opportunities to learn from the training data.

# 3. What is a batch?

# A batch is a small group of training samples processed together before the model updates its weights.

# For example:

# batch_size=4

# means the model processes 4 samples at a time.

# 4. What is the difference between training and testing data?

# Training data is used to teach the model and update its weights.

# Testing data is kept separate and is used after training to check how well the model performs on unseen data.

# Training data
#      ↓
# Model learns
#      ↓
# Testing data
#      ↓
# Check performance
# 5. Why do we scale numerical features?

# We scale numerical features so that features with very different numerical ranges don't dominate the learning process.

# For example:

# Study Hours  → 2–10
# Attendance   → 60–100
# Score        → 40–95

# Scaling puts them on a more comparable range, which can help neural networks learn faster and more effectively.

# 6. What does optimizer="adam" mean?

# Adam is the optimization algorithm used to update the neural network's weights during training.

# It looks at the gradients and decides how the weights should be changed to reduce the loss.

# Think:

# Prediction
#     ↓
# Calculate loss
#     ↓
# Calculate gradients
#     ↓
# Adam updates weights
#     ↓
# Better prediction
# 7. Why do we use binary_crossentropy here?

# Because our problem is binary classification.

# We are predicting two possible classes:

# 0 → Fail
# 1 → Pass

# And our output layer uses:

# Dense(1, activation="sigmoid")

# binary_crossentropy is designed to measure the error between the predicted probability and the actual binary label.

# 8. What is validation data?

# Validation data is data that the model doesn't directly use to update its weights during training.

# It is used to monitor how well the model is generalizing while training.

# When we write:

# validation_split=0.2

# 20% of the training data is separated for validation.

# X_train
#   │
#   ├── 80% → Training
#   │
#   └── 20% → Validation
# 9. What does model.evaluate() do?

# model.evaluate() checks the trained model's performance on the supplied data.

# When we run:

# model.evaluate(X_test, y_test)

# the model makes predictions on the test data and calculates metrics such as:

# Test Loss
# Test Accuracy

# It evaluates the model; it doesn't train it.

# 10. What is overfitting?

# Overfitting happens when the model learns the training data too specifically, including patterns or noise that don't generalize well.

# You might see:

# Training accuracy   ↑↑↑
# Training loss       ↓↓↓

# Validation accuracy ↓
# Validation loss     ↑

# The model is becoming very good on training data but worse on unseen data.

# 11. What is the difference between loss and val_loss?

# loss is the error calculated on the training data.

# val_loss is the error calculated on the validation data.

# loss
#  ↓
# How wrong is the model on training data?

# val_loss
#  ↓
# How wrong is the model on validation data?

# Generally, we want both to decrease, while watching carefully for a growing gap between them.

# 12. Why shouldn't we judge a model only by training accuracy?

# Because a model can have very high training accuracy but still perform poorly on new data.

# For example:

# Training Accuracy = 99%
# Test Accuracy     = 65%

# This could indicate that the model has overfit the training data.

# That's why we also look at:

# Training performance
#         +
# Validation performance
#         +
# Test performance
# 🧠 The big picture

# You have now covered the complete basic neural-network workflow:

# Prepare Data
#      ↓
# Scale Features
#      ↓
# Build Model
#      ↓
# Compile Model
#      ↓
# model.fit()
#      ↓
# Training
#      ↓
# Validation
#      ↓
# model.evaluate()
#      ↓
# Testing
#      ↓
# model.predict()
#      ↓
# Predictions

# TASK 10 complete = you understand the basic training/evaluation cycle of a neural network.


