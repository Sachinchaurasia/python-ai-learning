# 🔥 TASK 1 — Manual Neuron

# Given:

# x₁ = 4
# x₂ = 5

# w₁ = 0.3
# w₂ = 0.2

# b = 0.1

# Calculate:

# x₁ × w₁
# x₂ × w₂
# Weighted sum
# Add bias
# ReLU output

# Absolutely. Let's calculate it step by step, exactly like a neuron does.

# Given:

# x
# 1
# 	​

# =4
# x
# 2
# 	​

# =5
# w
# 1
# 	​

# =0.3
# w
# 2
# 	​

# =0.2
# b=0.1

# The neuron first calculates:

# 1. x
# 1
# 	​

# ×w
# 1
# 	​

# 4×0.3=1.2

# Answer: 1.2

# 2. x
# 2
# 	​

# ×w
# 2
# 	​

# 5×0.2=1.0

# Answer: 1.0

# 3. Weighted Sum

# Add the two weighted inputs:

# 1.2+1.0=2.2

# Weighted sum = 2.2

# 4. Add Bias

# Bias is:

# b=0.1

# Therefore:

# 2.2+0.1=2.3

# Weighted sum + bias = 2.3

# 5. ReLU Output

# ReLU means:

# If the value is positive → keep it.
# If the value is negative → make it 0.

# Here:

# 2.3>0

# Therefore:

# ReLU(2.3)=2.3

# ✅ Final Answer
# Step	Calculation	Result
# 1	4×0.3	1.2
# 2	5×0.2	1.0
# 3	1.2+1.0	2.2
# 4	2.2+0.1	2.3
# 5	ReLU(2.3)	2.3


# 🧠 Remember the flow
# x₁ = 4 ──× 0.3 ──► 1.2 ──┐
#                            │
# x₂ = 5 ──× 0.2 ──► 1.0 ──┤──► 2.2 ──► + 0.1 ──► 2.3 ──► ReLU ──► 2.3
#                            │

# Neuron's final output = 2.3