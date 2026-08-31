# TASK 5 — THINKING
# 1. What is forward propagation?

# Forward propagation is the process of passing input data through the neural network from the first layer to the last layer to produce a prediction.

# For example:

# Input → Hidden Layer → Hidden Layer → Output

# Each neuron calculates something like:

# weighted inputs → add bias → activation → output

# So, forward propagation is basically how the network uses its current weights to make a prediction.

# 2. Why does each neuron have different weights?

# Each neuron learns to detect a different pattern or relationship in the data.

# For example, suppose we have:

# Experience
# Education
# Skills

# One neuron might become more sensitive to experience, while another might focus more on education.

# Therefore, different weights allow different neurons to learn different aspects of the input.

# 👉 Different weights = different importance given to different inputs.

# 3. What does the output of one layer become for the next layer?

# The output of one layer becomes the input to the next layer.

# For example:

# Input
#   ↓
# Layer 1
#   ↓
# Layer 1 output
#   ↓
# Layer 2 input
#   ↓
# Layer 2
#   ↓
# Output

# So information flows forward through the network.

# 4. Why is a Dense layer called fully connected?

# A Dense layer is called fully connected because every neuron in that layer is connected to every output of the previous layer.

# For example:

# Previous Layer       Dense Layer

#   ○ ───────────────→ ○
#   ○ ───────────────→ ○
#   ○ ───────────────→ ○
#   ○ ───────────────→ ○

# Every neuron receives information from all neurons in the previous layer.

# That's why Keras uses:

# tf.keras.layers.Dense(8)
# 5. Is forward propagation the same as learning?

# No.

# Forward propagation and learning are different processes.

# Forward propagation:

# Uses the current weights to make a prediction.

# Learning/training:

# Compares the prediction with the actual answer, calculates the error, computes gradients, and updates the weights.

# The basic training cycle is:

# Input
#   ↓
# Forward Propagation
#   ↓
# Prediction
#   ↓
# Loss
#   ↓
# Backpropagation
#   ↓
# Update Weights
#   ↓
# Repeat

# So:

# Forward propagation = prediction

# Backpropagation + optimizer = weight adjustment/learning

# 6. Why did your untrained Keras model give an arbitrary-looking prediction?

# Because the model had not learned anything yet.

# When you create a new neural network, its weights are generally initialized with small values that are not yet learned from your dataset.

# So when you give it an input:

# Input
#   ↓
# Random/initial weights
#   ↓
# Forward propagation
#   ↓
# Prediction

# the prediction can look almost arbitrary.

# For example, an untrained binary classifier might produce:

# Prediction = 0.53

# That doesn't mean the model has correctly learned that the answer is 53%.

# It simply means the current, untrained weights produced that output.

# After training:

# Training data
#       ↓
# Forward propagation
#       ↓
# Loss
#       ↓
# Backpropagation
#       ↓
# Weight updates
#       ↓
# Repeat many times
#       ↓
# Learned weights
#       ↓
# Better predictions
# 🧠 The key idea to remember

# Forward propagation is the neural network using what it currently knows. Training is the process of changing its weights so that what it knows becomes useful.