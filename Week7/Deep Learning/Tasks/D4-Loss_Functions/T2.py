# TASK 3 — Binary Cross-Entropy

# Use:

# import tensorflow as tf

# loss_fn = tf.keras.losses.BinaryCrossentropy()

# actual = tf.constant([1.0])

# prediction1 = tf.constant([0.9])
# prediction2 = tf.constant([0.1])

# loss1 = loss_fn(actual, prediction1)
# loss2 = loss_fn(actual, prediction2)

# print("Loss 1:", loss1.numpy())
# print("Loss 2:", loss2.numpy())

# Answer:

# Which prediction should have the larger loss?

import tensorflow as tf
import numpy as np
loss_fn=tf.keras.losses.BinaryCrossentropy()


actual=tf.constant([1.0])

prediction1=tf.constant([0.9])
prediction2=tf.constant([0.1])

loss1=loss_fn(actual,prediction1)
loss2=loss_fn(actual,prediction2)

print("Loss1:",loss1.numpy())
print("Loss2:",loss2.numpy())
