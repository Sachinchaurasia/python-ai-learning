# # TASK 6 — CHANGE THE LEARNING RATE

# # Try:

# # 0.001
# # 0.01
# # 0.1

# # Compare the learning behavior.

# # Think:

# # Which is slower?
# # Which is faster?
# # Does a larger learning rate always mean better?

# #################################################################################
# Change the Learning Rate

# Now we will see how the learning rate affects training speed.

# We will test:

# 0.001
# 0.01
# 0.1
# Step 1 — Try all three learning rates

# Use this code:

# import tensorflow as tf

# learning_rates = [0.001, 0.01, 0.1]

# for learning_rate in learning_rates:

#     print("\n==============================")
#     print("Learning Rate:", learning_rate)
#     print("==============================")

#     w = tf.Variable(0.5)

#     x = tf.constant(2.0)
#     y_true = tf.constant(10.0)

#     for step in range(20):

#         with tf.GradientTape() as tape:
#             y_pred = w * x
#             loss = (y_true - y_pred) ** 2

#         gradient = tape.gradient(loss, w)

#         w.assign_sub(learning_rate * gradient)

#         print(
#             "Step:", step,
#             "Weight:", round(float(w.numpy()), 4),
#             "Prediction:", round(float(y_pred.numpy()), 4),
#             "Loss:", round(float(loss.numpy()), 4)
#         )
# 🧠 What is actually changing?

# Only this:

# learning_rate = ?

# The learning rate controls how big a step the weight takes.

# Think of it like walking toward a target:

# Target
#   🎯
#    |
#    |
#    |
#    ●  ← You
# Learning rate = 0.001

# Very tiny steps:

# ● → ● → ● → ● → ● → ● → 🎯

# 🐢 Slow learning

# Learning rate = 0.01

# Reasonable-sized steps:

# ● ──→ ● ──→ ● ──→ ● ──→ 🎯

# 🚶 Good/steady learning

# Learning rate = 0.1

# Much larger steps:

# ● ───────→ ● ───────→ 🎯

# 🏃 Fast learning

# But there's an important problem...

# 📊 Compare the three
# Learning Rate	Step Size	Learning Behavior
# 0.001	Very small	🐢 Slow
# 0.01	Moderate	🚶 Stable/steady
# 0.1	Large	🏃 Fast, potentially unstable
# 🔥 The important question
# Which is slower?

# 0.001 🐢

# The weight changes very slowly, so the loss decreases slowly.

# Which is faster?

# Usually 0.1 🏃

# It takes much larger updates and can reach the target region much faster for this simple example.

# Does a larger learning rate always mean better?
# ❌ NO!

# This is one of the most important concepts in gradient descent.

# A learning rate that is too small:

# Learning is extremely slow
# ↓
# May take many iterations

# A good learning rate:

# Fast enough
# +
# Stable
# =
# Good training

# A learning rate that is too large:

# Overshoots the minimum
#         ↓
#      ↗     ↘
#    ↗         ↘
#  ↗             ↘

# The model can jump back and forth, fail to converge, or even make the loss explode.

# 🧠 Real-world analogy

# Imagine you're trying to reach the bottom of a valley.

# 5
# 🐢 LR = 0.001

# Tiny steps.

# You eventually reach the bottom, but it takes a long time.

# 🚶 LR = 0.01

# Good-sized steps.

# You move toward the bottom efficiently and steadily.

# 🏃 LR = 0.1

# Large steps.

# You may get there quickly, but if the steps are too large, you can jump over the bottom.

# ⭐ Your TASK 6 answers

# Write these in your notes:

# 1. Which is slower?
#    → 0.001

# 2. Which is faster?
#    → 0.1 (in this simple example)

# 3. Does a larger learning rate always mean better?
#    → No.

# 4. Why?
#    → A very large learning rate can overshoot the minimum
#      and make training unstable.

# 5. A good learning rate should:
#    → Reduce the loss efficiently while keeping training stable.
# 🔑 Remember this

# Learning rate controls how big a step the model takes when updating its weights.

# Small → slow 🐢 | Good → stable 🚶 | Too large → unstable 🏃💨

