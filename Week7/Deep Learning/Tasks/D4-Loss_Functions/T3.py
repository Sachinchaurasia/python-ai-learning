# TASK 4 — Compare Predictions

# Actual:

# 1

# Try:

# 0.99
# 0.90
# 0.70
# 0.50
# 0.10
# 0.01

# Use BinaryCrossentropy and observe how the loss changes.




import tensorflow as tf
import numpy as np

loss_fn=tf.keras.losses.BinaryCrossentropy()

actual=tf.constant([1.0])
prediction=[0.99,0.90,0.70,0.50,0.10,0.01]

for prediction in prediction:
    loss=loss_fn(actual,tf.constant([prediction]))
    print("prediction",prediction,"loss",loss.numpy())
    
    