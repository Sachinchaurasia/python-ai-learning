# import tensorflow as tf
# #Weight
# w=tf.Variable(0.5)

# #Input
# x=tf.constant(2.0)

# #Target
# y_true=tf.constant(10.0)

# with tf.GradientTape() as tape:
#     y_pred=w*x
    
#     loss=(y_true - y_pred)**2
#     gradient=tape.gradient(loss,w)
    
#     print("Prediction",y_pred.numpy())
#     print("loss",loss.numpy())
#     print("Gradient",gradient.numpy())
    
    
    
import tensorflow as tf
w=tf.Variable(0.5)
x=tf.constant(2.0)

y_true=tf.constant(10.0)
learning_rate=0.01

for step in range(10):
    with tf.GradientTape() as tape:
        y_pred=w*x
        loss=(y_true - y_pred)**2
        
    gradient=tape.gradient(loss,w)
    
    print(
        f"Step{step+1}:"
        f"weight={w.numpy(): .4f}",
        f"Loss={loss.numpy(): .4f}"
    )
    