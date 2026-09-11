# # TASK 9 — Make Predictions

# # Use:

# # predictions = model.predict(X_test)

# # Then:

# # predicted_classes = (
# #     predictions >= 0.5
# # ).astype(int)

# # Print both.

# #########################################################################

# Make Predictions

# Now your trained neural network will make predictions on the unseen test data.

# Step 1 — Get predictions

# Run:

# predictions = model.predict(X_test)

# You will get values such as:

# [[0.12]
#  [0.87]
#  [0.34]
#  [0.91]]

# These are probabilities, not yet 0 or 1.

# Because your final layer is:

# Dense(1, activation="sigmoid")

# the output is between 0 and 1.

# Step 2 — Convert probabilities into classes

# Use:

# predicted_classes = (
#     predictions >= 0.5
# ).astype(int)

# The rule is:

# prediction >= 0.5  →  1
# prediction <  0.5  →  0

# For example:

# Probability    Class
# ---------------------
# 0.12           0
# 0.34           0
# 0.51           1
# 0.87           1
# 0.91           1
# Step 3 — Print both
# print("Predictions:")
# print(predictions)

# print("\nPredicted Classes:")
# print(predicted_classes)

# You should see something like:

# Predictions:
# [[0.12]
#  [0.87]
#  [0.34]
#  [0.91]]

# Predicted Classes:
# [[0]
#  [1]
#  [0]
#  [1]]
# 🧠 Understand the difference
# X_test
#    ↓
# model.predict()
#    ↓
# Probability
#    ↓
# 0.12, 0.87, 0.34, 0.91
#    ↓
# Threshold = 0.5
#    ↓
# Predicted class
#    ↓
# 0, 1, 0, 1
# ⭐ Important

# predictions tells you how confident the model is.

# predicted_classes tells you the final decision.

# For example:

# 0.92 → 1

# means the model predicts class 1 with approximately 92% probability.

# Now compare:

# print("Actual:", y_test)
# print("Predicted:", predicted_classes)

# This lets you see what the model actually predicted versus the correct answers.


