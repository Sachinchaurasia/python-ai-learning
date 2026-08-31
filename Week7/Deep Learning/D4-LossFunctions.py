# import numpy as np

# actual=np.array([10,20,30])

# prediction=np.array([8,18,33])

# mse=np.mean((actual-prediction)**2)
# print("MSE",mse)


##calculate BinaryCrossentropy Using Keras ,tensorFlow
# import tensorflow as tf
# loss_fn=tf.keras.losses.BinaryCrossentropy()

# actual=tf.constant([1.0])
# prediction=tf.constant([0.1])

# loss=loss_fn(actual,prediction)

# print("loss",loss.numpy())


import tensorflow as tf
import numpy as np

#Create model
model=tf.keras.Sequential([
    tf.keras.layers.Dense(4,activation="relu"),
    tf.keras.layers.Dense(2,activation="relu"),
    tf.keras.layers.Dense(1,activation="sigmoid")
    
])

#Configure model
model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

model.summary()

