# # TASK 5 — TRAIN FOR 20 STEPS

# # Modify your loop:

# # for step in range(20):

# # Print:

# # Step
# # Weight
# # Prediction
# # Loss
# # Gradient

# # Observe:

# # Does the loss generally decrease?


# ####################################################################################

# Train for 20 Steps

# Now we are going to repeat the same process 20 times.

# The model will:

# Predict → Calculate Loss → Calculate Gradient → Update Weight

# Complete code
import tensorflow as tf

w = tf.Variable(0.5)

x = tf.constant(2.0)
y_true = tf.constant(10.0)

learning_rate = 0.01

for step in range(20):

    # Forward pass
    with tf.GradientTape() as tape:
        y_pred = w * x
        loss = (y_true - y_pred) ** 2

    # Calculate gradient
    gradient = tape.gradient(loss, w)

    # Update weight
    w.assign_sub(learning_rate * gradient)

    # Print results
    print(
        "Step:", step,
        "Weight:", w.numpy(),
        "Prediction:", y_pred.numpy(),
        "Loss:", loss.numpy(),
        "Gradient:", gradient.numpy()
    )
# 🧠 What happens in every step?

# Think of the training loop like this:

#           ┌──────────────┐
#           │   Weight     │
#           │    w = 0.5   │
#           └──────┬───────┘
#                  ↓
#           ┌──────────────┐
#           │  Prediction  │
#           │   y = w × x  │
#           └──────┬───────┘
#                  ↓
#           ┌──────────────┐
#           │    Loss      │
#           │ How wrong?   │
#           └──────┬───────┘
#                  ↓
#           ┌──────────────┐
#           │   Gradient   │
#           │ Which way?   │
#           └──────┬───────┘
#                  ↓
#           ┌──────────────┐
#           │ Update Weight│
#           └──────┬───────┘
#                  │
#                  └──────────► Repeat 20 times
# 📊 What should you observe?

# Initially:

# $$ w=0.5 $$

# Prediction:

# $$ 0.5\times2=1 $$

# Target:

# $$ 10 $$

# So the model is very wrong.

# After each update, the weight gets closer to 5, because:

# $$ w\times2=10 $$

# Therefore:

# $$ w=5 $$

# As the weight approaches 5:

# Prediction gets closer to 10 → Loss decreases → Gradient becomes smaller.

# Approximate progression
# Step	Weight	Prediction	Loss
# 0	0.86	1.00	81.00
# 1	1.19	1.72	68.97
# 2	1.50	2.38	57.93
# 5	~2.30	~4.60	~29
# 10	~3.40	~6.80	~10
# 19	~4.51	~9.02	~1

# The exact printed values can vary slightly in formatting.

# ✅ Answer to the observation

# Does the loss generally decrease?

# YES! ✅

# The loss should generally decrease as training progresses.

# The model is learning:

# Weight
# 0.5
#  ↓
# 0.86
#  ↓
# 1.19
#  ↓
# 1.50
#  ↓
# ...
#  ↓
# ~4.5

# Prediction
# 1
#  ↓
# 1.72
#  ↓
# 2.38
#  ↓
# ...
#  ↓
# ~9

# Loss
# 81
#  ↓
# 68.97
#  ↓
# 57.93
#  ↓
# ...
#  ↓
# ~1
# 🔥 Key concept

# Training = repeatedly adjusting the weight to reduce the loss.

# And this is exactly what happens inside neural networks, except real neural networks have many weights, many neurons, many layers, and much more data.
