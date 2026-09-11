# # ## &#x20;TASK 1 — Manual Gradient Descent

# # Given:

# # ```
# # ```

# # ```
# # Old weight = 0.8
# # Gradient = 0.3
# # Learning rate = 0.1
# # ```

# # Calculate:

# # ```
# # ```

# # ```
# # New weight
# # ```

# # Use:

# # ```
# # ```

# # ```
# # New Weight = Old Weight - Learning Rate × Gradient
# # ```
##################################################################################################


# TASK 1 — Manual Gradient Descent

# Given:

# Old Weight = 0.8
# Gradient = 0.3
# Learning Rate = 0.1

# The formula is:

# {New Weight} = {Old Weight} - {Learning Rate} {Gradient})
 
# Give feedback

# Now substitute the values:

# $$ \text{New Weight} = 0.8 - (0.1 \times 0.3) $$

# First:

# $$ 0.1 \times 0.3 = 0.03 $$

# Then:

# $$ 0.8 - 0.03 = \boxed{0.77} $$
# ✅ Answer

# New Weight = 0.77

# 🧠 Intuition

# The gradient is positive (0.3), so gradient descent moves the weight downward:

# Old Weight
#    0.80
#     ↓
#  subtract 0.03
#     ↓
# New Weight
#    0.77

# This is the basic idea behind how an optimizer such as Adam changes neural-network weights during training.

