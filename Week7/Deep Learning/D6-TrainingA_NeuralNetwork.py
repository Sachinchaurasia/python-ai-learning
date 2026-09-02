import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  StandardScaler


#Load dataset
df=pd.read_csv("Student_data.csv")

#Features and Target

x=df[[
    "Studey_Hours",
    "Attendance",
    "Previous_Score"
    
]]

y=df["Pass"]

#Train Test Split

x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=0.2,
                                               random_state=42)

#Feature scaling

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)

x_test=scaler.transform(x_test)

#Create Neural Network Model

model=tf.keras.Sequential([
    
    tf.keras.layers.Dense(8,activation="relu"),
    tf.keras.layers.Dense(4,activation="relu"),
    tf.keras.layers.Dense(1,activation="sigmoid")
])

#Compile

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
    
)
                   
                   
#Train the mmodel
history=model.fit(x_train,
                  y_train,
                  epochs=50,
                  batch_size=16,
                  validation_split=0.2)


#Evaluate the model
test_loss,test_accuracy=model.evaluate(x_test,y_test)

print("Test loss:",test_loss)
print("Test Accuracy:",test_accuracy)

#Plot Loss

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training and Validation Accuracy")

plt.show()

#################################################################################

# 1. Import libraries
# import pandas as pd
# import numpy as np
# import tensorflow as tf
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# You are importing:

# pandas → work with CSV/dataframes
# numpy → numerical operations
# tensorflow → build and train the neural network
# matplotlib → plot accuracy
# train_test_split → divide data into training/testing
# StandardScaler → scale features

# You aren't directly using numpy in the code shown, so that import can currently be removed.

# 2. Load dataset
# df = pd.read_csv("Student_data.csv")

# This loads your CSV into a pandas DataFrame.

# Your data looks like:

# Study Hours	Attendance	Previous Score	Pass
# 2	60	45	0
# 3	65	50	0
# 4	70	55	1
# 5	75	60	1

# Here:

# Features (X) = information used to make the prediction.

# Target (y) = what you want to predict.

# 3. Select features
# x = df[[
#     "Studey_Hours",
#     "Attendance",
#     "Previous_Score"
# ]]

# Your neural network receives 3 inputs for each student:

# Studey_Hours
# Attendance
# Previous_Score

# For example:

# [6, 88, 72]
# 4. Select target
# y = df["Pass"]

# Pass is your target.

# You have:

# 0 → Fail
# 1 → Pass

# So the neural network is solving a binary classification problem.

# 5. Train/Test Split
# x_train, x_test, y_train, y_test = train_test_split(
#     x,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# You have 15 records.

# With:

# test_size=0.2

# approximately:

# 15 × 20% = 3

# So approximately:

# 12 → training
# 3  → testing

# The model learns from the 12 training examples.

# The 3 test examples are kept aside to evaluate the model.

# 6. Feature Scaling
# scaler = StandardScaler()

# x_train = scaler.fit_transform(x_train)
# x_test = scaler.transform(x_test)

# This is very important.

# Your three features have very different ranges:

# Study Hours       → 1–8
# Attendance        → 55–95
# Previous Score    → 40–80

# Without scaling, Attendance and Previous_Score have much larger numerical values than Study_Hours.

# StandardScaler converts them into standardized values.

# Conceptually:

# Original data
#       ↓
# StandardScaler
#       ↓
# Scaled data
#       ↓
# Neural Network
# Why fit_transform() for training?
# x_train = scaler.fit_transform(x_train)

# fit() → learns the mean and standard deviation.

# transform() → performs the scaling.

# Therefore:

# fit_transform()

# does both.

# Why only transform() for test?
# x_test = scaler.transform(x_test)

# Because the test data must be transformed using the same scaling learned from the training data.

# We don't want the test data influencing the training process.

# 7. Create Neural Network

# This is the heart of your program:

# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(8, activation="relu"),
#     tf.keras.layers.Dense(4, activation="relu"),
#     tf.keras.layers.Dense(1, activation="sigmoid")
# ])

# Your architecture is:

#        INPUT
#          │
#          │
#     3 features
#          │
#          ▼
#  ┌─────────────────┐
#  │ Dense: 8 neurons│
#  │     ReLU        │
#  └─────────────────┘
#          │
#          ▼
#  ┌─────────────────┐
#  │ Dense: 4 neurons│
#  │     ReLU        │
#  └─────────────────┘
#          │
#          ▼
#  ┌─────────────────┐
#  │ Dense: 1 neuron │
#  │    Sigmoid      │
#  └─────────────────┘
#          │
#          ▼
#      Pass/Fail
# First Dense layer
# Dense(8, activation="relu")

# This creates 8 neurons.

# Each neuron learns different patterns from:

# Study Hours
# Attendance
# Previous Score
# Second Dense layer
# Dense(4, activation="relu")

# This has 4 neurons.

# It takes information produced by the previous layer and learns higher-level patterns.

# Output layer
# Dense(1, activation="sigmoid")

# Only one neuron is needed because you have two possible outcomes:

# Fail = 0
# Pass = 1

# The sigmoid produces a value between:

# 0 and 1

# For example:

# 0.12 → likely Fail
# 0.25 → likely Fail
# 0.76 → likely Pass
# 0.94 → likely Pass
# 8. Compile the model
# model.compile(
#     optimizer="adam",
#     loss="binary_crossentropy",
#     metrics=["accuracy"]
# )

# This tells TensorFlow how to train the network.

# Optimizer
# optimizer="adam"

# Adam determines how the weights should be updated during training.

# Conceptually:

# Prediction
#     ↓
# Calculate error
#     ↓
# Backpropagation
#     ↓
# Calculate gradients
#     ↓
# Adam updates weights
#     ↓
# Better prediction
# Loss
# loss="binary_crossentropy"

# Because your target has two classes:

# 0 = Fail
# 1 = Pass

# Binary cross-entropy measures how wrong the prediction is.

# Metric
# metrics=["accuracy"]

# You want TensorFlow to report accuracy while training.

# 9. Train the model
# history = model.fit(
#     x_train,
#     y_train,
#     epochs=50,
#     batch_size=16,
#     validation_split=0.2
# )

# This is where the actual learning happens.

# epochs=50

# The model goes through the training data 50 times.

# Epoch 1
#    ↓
# Epoch 2
#    ↓
# Epoch 3
#    ↓
# ...
# Epoch 50

# During each epoch, the model:

# Input
#  ↓
# Forward propagation
#  ↓
# Prediction
#  ↓
# Loss calculation
#  ↓
# Backpropagation
#  ↓
# Weight update
# batch_size=16

# The model processes up to 16 training examples at a time before updating the weights.

# Since your dataset is extremely small, you effectively have only about one batch per epoch.

# That's why your output showed:

# 1/1
# validation_split=0.2

# You're taking 20% of the training data and using it for validation.

# So your already-small dataset is roughly:

# 15 total
# │
# ├── 3 test
# │
# └── 12 training
#       │
#       ├── ~10 actual training
#       └── ~2 validation

# This is why your accuracy numbers should not be interpreted as highly reliable.

# 10. Evaluate
# test_loss, test_accuracy = model.evaluate(x_test, y_test)

# After training, you give the model the previously unseen test data.

# Your result:

# Test loss: 0.3182
# Test Accuracy: 1.0

# 1.0 means:

# 100%

# On your 3 test samples, the model predicted all of them correctly.

# Again, because you only have 3 test samples, this isn't enough evidence to claim the model is genuinely 100%-accurate.

# 11. Plot accuracy
# plt.plot(history.history["accuracy"])
# plt.plot(history.history["val_accuracy"])

# plt.xlabel("Epoch")
# plt.ylabel("Accuracy")
# plt.title("Training and Validation Accuracy")

# plt.show()

# This plots:

# Training Accuracy
#         vs
# Validation Accuracy

# against the number of epochs.

# You'll be able to visually see how the model's performance changes as training progresses.

# ⭐ The most important concept

# Your entire program can be remembered as:

#         CSV
#          ↓
#     Select X and y
#          ↓
#    Train/Test Split
#          ↓
#     StandardScaler
#          ↓
#    Neural Network
#          ↓
#       Compile
#          ↓
#        Train
#          ↓
#     Prediction
#          ↓
#       Evaluate
#          ↓
#        Plot

# And internally:

#              DATA
#                ↓
#        ┌───────────────┐
#        │ Forward Pass  │
#        └───────┬───────┘
#                ↓
#           Prediction
#                ↓
#         Calculate Loss
#                ↓
#        Backpropagation
#                ↓
#          Gradients
#                ↓
#       Adam updates weights
#                ↓
#        Next training step

# This is the core Deep Learning training cycle.