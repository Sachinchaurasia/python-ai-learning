# TASK 5 — Keras Model

# Create:

# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(8, activation="relu"),
#     tf.keras.layers.Dense(4, activation="relu"),
#     tf.keras.layers.Dense(1, activation="sigmoid")
# ])

# Compile it:

# model.compile(
#     loss="binary_crossentropy",
#     optimizer="adam",
#     metrics=["accuracy"]
# )

# Then:

# model.summary()



import tensorflow as tf

# Create the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# Compile the model
model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

# Display model architecture
model.summary()