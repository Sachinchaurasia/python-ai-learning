# Experiment With Epochs

# Now we want to understand how the number of epochs affects learning.

# Run the same model with different epoch values:

# 1️⃣ Try 5 epochs
# history_5 = model.fit(
#     X_train,
#     y_train,
#     epochs=5,
#     batch_size=4,
#     validation_split=0.2
# )

# Observe:

# Training loss
# Validation loss
# Training accuracy
# Validation accuracy
# 2️⃣ Try 20 epochs
# history_20 = model.fit(
#     X_train,
#     y_train,
#     epochs=20,
#     batch_size=4,
#     validation_split=0.2
# )
# 3️⃣ Try 50 epochs
# history_50 = model.fit(
#     X_train,
#     y_train,
#     epochs=50,
#     batch_size=4,
#     validation_split=0.2
# )
# 4️⃣ Try 100 epochs
# history_100 = model.fit(
#     X_train,
#     y_train,
#     epochs=100,
#     batch_size=4,
#     validation_split=0.2
# )
# ⚠️ Important

# For a fair experiment, create a new model before each experiment. Otherwise, the 20-epoch experiment will continue learning from the model already trained for 5 epochs.

# For example:

# def create_model():
#     model = Sequential([
#         Dense(8, activation="relu", input_shape=(3,)),
#         Dense(4, activation="relu"),
#         Dense(1, activation="sigmoid")
#     ])

#     model.compile(
#         optimizer="adam",
#         loss="binary_crossentropy",
#         metrics=["accuracy"]
#     )

#     return model

# Then:

# model_5 = create_model()
# history_5 = model_5.fit(
#     X_train, y_train,
#     epochs=5,
#     batch_size=4,
#     validation_split=0.2
# )

# Do the same for 20, 50, and 100 epochs.

# 🧠 What are we looking for?

# Think about this pattern:

# Epochs	Training Loss	Validation Loss	Training Accuracy	Validation Accuracy
# 5	Usually higher	Usually higher	Usually lower	Usually lower
# 20	↓	↓	↑	↑
# 50	↓	↓/stable	↑	↑/stable
# 100	May ↓ further	May ↑	May ↑	May ↓

# The important concept is overfitting.

# Good learning
# Training Loss       ↓
# Validation Loss     ↓
# Training Accuracy   ↑
# Validation Accuracy ↑
# Possible overfitting
# Training Loss       ↓↓↓
# Training Accuracy   ↑↑↑

# Validation Loss     ↑
# Validation Accuracy ↓

# That means the model is becoming very good at memorizing the training data, but its performance on unseen validation data is getting worse.

# 🎯 Your task

# Run 5 → 20 → 50 → 100 epochs and compare the four values.

# Then send me your results. I'll help you identify which epoch count is best and whether overfitting starts to appear.
