# # TASK 4 — Compile

# # Use:

# # model.compile(
# #     optimizer="adam",
# #     loss="binary_crossentropy",
# #     metrics=["accuracy"]
# # )

# # Explain in your own words what each part means.


# There is no output from model.compile() if everything works correctly. It prepares the model for training.

# 🧠 Understand each part
# 1. optimizer="adam"

# Adam decides how the model's weights should be updated during learning.

# Think:

# Prediction → Calculate error → Adam → Adjust weights → Better prediction

# Adam is an optimization algorithm that uses the gradients to decide how much to change the weights.

# For your model:

# Old weights
#      ↓
#    Adam
#      ↓
# Updated weights
# 2. loss="binary_crossentropy"

# Loss tells us how wrong the model's prediction is.

# Your target is:

# Pass = 0
# Pass = 1

# So this is a binary classification problem.

# Therefore we use:

# loss="binary_crossentropy"

# For example:

# Actual:     1
# Prediction: 0.90
#              ↓
#         Small loss ✅

# But:

# Actual:     1
# Prediction: 0.10
#              ↓
#         Large loss ❌

# The model's goal during training is to reduce the loss.

# 3. metrics=["accuracy"]

# Accuracy tells us how many predictions the model got correct.

# For example, if the model makes 10 predictions and gets 8 correct:

# Accuracy = 8 / 10
#          = 80%

# During training, Keras will show something like:

# loss: 0.45
# accuracy: 0.78

# So:

# Loss → How wrong is the model?
# Accuracy → How many predictions are correct?
# 🔗 Put everything together
#                  MODEL
#                    │
#                    ▼
#             Make prediction
#                    │
#                    ▼
#         binary_crossentropy
#           calculates error
#                    │
#                    ▼
#                Gradients
#                    │
#                    ▼
#                 Adam
#           updates the weights
#                    │
#                    ▼
#           Model learns better
# ⭐ Remember this
# Component	Simple meaning
# optimizer="adam"	How to learn/update weights
# loss="binary_crossentropy"	How to measure prediction error
# metrics=["accuracy"]	How to measure correct predictions
# One-line understanding

# Loss tells the model how wrong it is, Adam tells it how to improve, and accuracy tells us how often it is correct.

