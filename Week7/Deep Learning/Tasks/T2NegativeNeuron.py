# # 🔥 TASK 2 — Negative Neuron

# Given:

# ```
# ```

# ```
# x₁ = 2
# x₂ = 4

# w₁ = -0.5
# w₂ = -0.2

# b = 0.1
# ```

# Find:

# ```
# ```

# ```
# Weighted sum
# ReLU output
# ```




# Given:

# x
# 1
# 	​

# =2
# x
# 2
# 	​

# =4
# w
# 1
# 	​

# =−0.5
# w
# 2
# 	​

# =−0.2
# b=0.1
# 1. Calculate each weighted input
# x
# 1
# 	​

# w
# 1
# 	​

# =2×(−0.5)=−1.0
# x
# 2
# 	​

# w
# 2
# 	​

# =4×(−0.2)=−0.8
# 2. Calculate the weighted sum
# −1.0+(−0.8)=−1.8
# 3. Add the bias
# −1.8+0.1=−1.7

# So the neuron's value before ReLU is:

# −1.7
# 4. Apply ReLU

# ReLU follows a very simple rule:

# ReLU(x)=max(0,x)

# Since −1.7 is negative:

# ReLU(−1.7)=0
# ✅ Final Answer
# Step	Result
# x
# 1
# 	​

# w
# 1
# 	​

# 	-1.0
# x
# 2
# 	​

# w
# 2
# 	​

# 	-0.8
# Weighted sum	-1.8
# Add bias	-1.7
# ReLU output	0
# 🧠 The important idea

# Notice what happened:

# Input 1 ──► -1.0 ──┐
#                    │
# Input 2 ──► -0.8 ──┤──► -1.8 ──► + 0.1 ──► -1.7 ──► ReLU ──► 0
#                    │

# So the bias changed -1.8 to -1.7, but it wasn't enough to make the neuron positive.

# That's why ReLU finally produced 0.

# Your mental rule:

# Negative before ReLU → 0
# Positive before ReLU → same value.