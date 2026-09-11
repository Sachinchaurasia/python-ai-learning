# 🔥 TASK 3 — Build the Model

# Create:

# Dense(8, ReLU)
# Dense(4, ReLU)
# Dense(1, Sigmoid)

# Then:

# model.summary()

# Study the number of parameters.


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(8, activation="relu", input_shape=(3,)),
    Dense(4, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.summary()



# 🧠 What did we create?
# Input
#   │
#   │  3 features
#   ▼
# ┌─────────────┐
# │ Dense(8)    │
# │ ReLU        │
# └─────────────┘
#        │
#        ▼
# ┌─────────────┐
# │ Dense(4)    │
# │ ReLU        │
# └─────────────┘
#        │
#        ▼
# ┌─────────────┐
# │ Dense(1)    │
# │ Sigmoid     │
# └─────────────┘
#        │
#        ▼
#    Pass probability

# Your 3 input features are:

# Study_Hours
# Attendance
# Previous_Score
# 🔢 Study the parameters

# For a Dense layer:

# Parameters = (number of inputs × number of neurons) + number of biases

# Layer 1 — Dense(8)

# 3 inputs → 8 neurons:

# (3 × 8) + 8
# = 24 + 8
# = 32 parameters
# Layer 2 — Dense(4)

# 8 inputs → 4 neurons:

# (8 × 4) + 4
# = 32 + 4
# = 36 parameters
# Layer 3 — Dense(1)

# 4 inputs → 1 neuron:

# (4 × 1) + 1
# = 4 + 1
# = 5 parameters
# ✅ Total
# 32 + 36 + 5 = 73

# So your model should show approximately:

# Total params: 73
# Trainable params: 73
# Non-trainable params: 0
# Important concept

# The 73 parameters are the values the neural network will learn during training.

# They consist of:

# Weights → control the strength of connections
# Biases → allow neurons to shift their activation

# Don't worry if Keras gives an input_shape warning depending on your TensorFlow/Keras version. A newer style is:

# model = Sequential([
#     tf.keras.Input(shape=(3,)),
#     Dense(8, activation="relu"),
#     Dense(4, activation="relu"),
#     Dense(1, activation="sigmoid")
# ])

# model.summary()

# This produces the same 73 trainable parameters.