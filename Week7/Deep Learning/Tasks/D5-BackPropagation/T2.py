# # TASK 2 — Negative Gradient

# # Given:

# # Old weight = 0.8
# # Gradient = -0.3
# # Learning rate = 0.1

# # Calculate the new weight.

# # Ask yourself:

# # Did the weight increase or decrease?

# #########################################################################

# Negative Gradient (Step-by-Step, Beginner Friendly)

# This is part of Week 7 (Deep Learning - Gradient Descent), so let's solve it visually and intuitively.

# Given

# Old Weight

# 0.8

# Gradient

# -0.3

# Learning Rate

# 0.1
# Step 1: Formula

# Gradient Descent updates the weight using:

# New Weight=Old Weight−(Learning Rate×Gradient)
# Step 2: Put the values into the formula
# New Weight=0.8−(0.1×−0.3)
# Step 3: Multiply Learning Rate × Gradient
# 0.1×−0.3=−0.03

# So now:

# 0.8−(−0.03)
# Step 4: Double negative becomes plus
# 0.8+0.03=0.83
# ✅ Final Answer

# New Weight

# 0.83

# The weight increased.

# It changed from 0.80 → 0.83.

# 📈 Visual Understanding (Very Important)
# 4

# Imagine you're standing in a valley.

# Positive gradient (+0.3) → Slope goes upward, so you move left/downhill and the weight decreases.

# Negative gradient (-0.3) → Slope goes downward, so you move right/downhill and the weight increases.

# Weight Movement

# The arrow shows the weight moving forward (increasing) because the gradient is negative.

# 🧠 Intuition (Easy to Remember)

# Gradient

	

# Weight Update




# +0.3

	

# Weight decreases (move opposite to positive slope).




# −0.3

	

# Weight increases (subtracting a negative adds to the weight).

# Memory Trick: Positive gradient → subtract → weight goes down. Negative gradient → subtract a negative → weight goes up.

# ✅ Your Answer for Notebook

# New Weight = 0.83

# Did the weight increase or decrease?

# Answer: The weight increased from 0.80 to 0.83 because the gradient was negative (-0.3).

# Next: We’ll continue with TASK 3 — Zero Gradient in the same visual step-by-step style.