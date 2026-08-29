# import numpy as np
# # #Input
# # x=np.array([2,3])

# # #Weights
# # w=np.array([0.5,0.4])

# # #Bias
# # b=0.2

# # #Weighted sum
# # z=np.dot(x,w)+b

# # print("Weighted sum:",z)

# # #Now ReLU
# # output=max(0,z)

# # print("Neuron Output:",output)


# ##input 
# x=np.array([2,3])

# #Weights:
# w=np.array([
#     [0.5,0.4],
#     [0.2,0.7]
    
# ])

# #Bias
# b=np.array([0.2,0.1])

# z=np.dot(x,w)+b
# print(z)

# output=np.maximum(0,z)
# print("Layer output:",output)

import tensorflow as tf
import numpy as np

model=tf.keras.sequential([
    tf.keras.layers.Dense(4,activation="relu"),
    tf.keras.layers.Dense(1,activation="Sigmoid")
    
])

x=np.array([[5,80,70]], dtype=np.float32)

prediction=model(x)

print("prediction")
print(prediction)

