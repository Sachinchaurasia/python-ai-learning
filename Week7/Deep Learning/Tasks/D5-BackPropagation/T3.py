# # TASK 3 — TensorFlow GradientTape

# # Write:

# # import tensorflow as tf

# # w = tf.Variable(0.5)

# # x = tf.constant(2.0)
# # y_true = tf.constant(10.0)

# # with tf.GradientTape() as tape:

# #     y_pred = w * x
# #     loss = (y_true - y_pred) ** 2

# # gradient = tape.gradient(loss, w)

# # print("Prediction:", y_pred.numpy())
# # print("Loss:", loss.numpy())
# # print("Gradient:", gradient.numpy())

# ############################################################################################

# TensorFlow GradientTape 🧠

# This code teaches you how TensorFlow automatically calculates the gradient of the loss with respect to the weight.

# Step 1 — Create the weight
# w = tf.Variable(0.5)

# We start with:

#  w = 0.5

# Step 2 — Input and true value
# x = tf.constant(2.0)
# y_true = tf.constant(10.0)

# So:

#  x=2, y_{true}=10 
# Step 3 — Forward propagation

# Inside GradientTape:

# y_pred = w * x

# Therefore:

#  y_{pred}=0.5\times2=1.0 

# So the model predicts 1.0, but the correct answer is 10.0.

# Step 4 — Calculate Loss
# loss = (y_true - y_pred) ** 2
# $$ Loss=(10-1)^2 $$ $$ Loss=9^2=81 $$

# So the loss is 81.0.

# Step 5 — TensorFlow calculates the gradient
# gradient = tape.gradient(loss, w)

# Mathematically:

# $$ Loss=(10-2w)^2 $$

# The derivative with respect to \(w\) is:

# $$ \frac{dLoss}{dw}=-4(10-2w) $$

# At \(w=0.5\):

# $$ \frac{dLoss}{dw}=-4(10-1) $$ $$ =-36 $$

# So:

# Gradient = -36.0

# Step 6 — Expected output
# Prediction: 1.0
# Loss: 81.0
# Gradient: -36.0
# 🔥 Most important connection

# You just saw the exact reason we learned the previous task:

# Gradient = -36

# Since the gradient is negative, Gradient Descent will increase the weight.

# For example, with learning rate \(0.1\):

# $$ w_{new}=0.5-(0.1\times-36) $$ $$ w_{new}=4.1 $$

# So the weight makes a big jump from 0.5 → 4.1, because the model's prediction (1) is very far from the target (10).

# GradientTape is basically TensorFlow's automatic mathematician—it watches the calculation and then tells you how the loss changes when the weight changes.