# # TASK 5 — Train

# # Try:

# # history = model.fit(
# #     X_train,
# #     y_train,
# #     epochs=50,
# #     batch_size=4,
# #     validation_split=0.2
# # )

# # Observe:

# # loss
# # accuracy
# # val_loss
# # val_accuracy


# #########################################################################################

# Training the Neural Network. Now you will actually make the model learn from X_train and y_train.

# Step 1 — Run this code
# history = model.fit(
#     X_train,
#     y_train,
#     epochs=50,
#     batch_size=4,
#     validation_split=0.2
# )
# Step 2 — What each part means
# Parameter	Meaning
# X_train	Training input/features
# y_train	Correct answers/labels
# epochs=50	Model sees the training data 50 times
# batch_size=4	Model processes 4 samples at a time
# validation_split=0.2	20% of training data is kept aside for validation
# history	Stores the training results
# Step 3 — Observe these 4 values

# While training, you'll see something similar to:

# Epoch 1/50
# loss: 0.68
# accuracy: 0.62
# val_loss: 0.65
# val_accuracy: 0.75

# Epoch 2/50
# loss: 0.61
# accuracy: 0.75
# val_loss: 0.59
# val_accuracy: 0.75

# ...

# Don't worry if your exact numbers are different.

# Step 4 — Understand them

# loss
# How wrong the model's predictions are.

# ➡️ Generally, lower is better.

# accuracy
# Percentage of training predictions that are correct.

# ➡️ Generally, higher is better.

# val_loss
# How wrong the model is on the validation data it didn't train directly on.

# ➡️ Generally, lower is better.

# val_accuracy
# Percentage of validation predictions that are correct.

# ➡️ Generally, higher is better.

# 🧠 The important pattern

# Ideally, during training:

# loss       ↓
# accuracy   ↑
# val_loss   ↓
# val_accuracy ↑

# Think of it like:

#              MODEL LEARNING
#                    │
#                    ▼
#         ┌─────────────────────┐
#         │ Training Data       │
#         │ X_train + y_train   │
#         └──────────┬──────────┘
#                    │
#                    ▼
#               Neural Network
#                    │
#              adjusts weights
#                    │
#                    ▼
#         ┌─────────────────────┐
#         │ Better Predictions  │
#         └─────────────────────┘
# Step 5 — Check the final values

# After training, run:

# print(history.history.keys())

# Then:

# print("Final Loss:", history.history["loss"][-1])
# print("Final Accuracy:", history.history["accuracy"][-1])
# print("Final Val Loss:", history.history["val_loss"][-1])
# print("Final Val Accuracy:", history.history["val_accuracy"][-1])

# Your task: run the training and send me the output from the 50 epochs (or at least the final few epochs). I'll help you interpret whether your model is learning properly, overfitting, or underfitting.