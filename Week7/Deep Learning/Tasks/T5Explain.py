# 1. What does a weight represent?

# A weight tells the neuron how important an input is.

# For example:

# x₁ = 4
# w₁ = 0.3

# The contribution of x₁ is:

# 4 × 0.3 = 1.2

# If the weight is large and positive → the input has a stronger positive influence.

# If the weight is negative → the input pushes the neuron toward a negative result.

# So I think of weight = importance/influence of an input.

# 2. Why do we need bias?

# Bias gives the neuron extra flexibility.

# First the neuron calculates:

# Weighted Sum = x₁w₁ + x₂w₂ + ...

# Then:

# z = Weighted Sum + Bias

# The bias can shift the final result before the activation function is applied.

# For example:

# Weighted Sum = -0.2
# Bias = 0.5

# z = -0.2 + 0.5
# z = 0.3

# Without bias:

# z = -0.2

# With bias:

# z = 0.3

# So I think of bias = an adjustment/shift that helps the neuron make better decisions.

# 3. What is a weighted sum?

# A weighted sum is when the neuron:

# Takes each input
# Multiplies it by its weight
# Adds all the results

# For example:

# x₁ = 4     w₁ = 0.3
# x₂ = 5     w₂ = 0.2

# Then:

# 4 × 0.3 = 1.2
# 5 × 0.2 = 1.0

# Therefore:

# Weighted Sum = 1.2 + 1.0
#              = 2.2

# Then bias can be added:

# z = 2.2 + 0.1
#   = 2.3
# 4. What does ReLU do to a negative value?

# ReLU basically says:

# If the value is negative, make it 0. If it is positive, keep it.

# ReLU(x) = max(0, x)

# Examples:

# ReLU(5)  → 5
# ReLU(2)  → 2
# ReLU(0)  → 0
# ReLU(-3) → 0
# ReLU(-10) → 0

# So:

# Negative → 0
# Positive → unchanged
# 5. Why is sigmoid useful for binary classification?

# Sigmoid converts a number into a value between 0 and 1.

# For example:

# sigmoid(5)  ≈ 0.993
# sigmoid(0)  = 0.5
# sigmoid(-5) ≈ 0.007

# This is useful when we have two classes:

# 0 = No disease
# 1 = Disease

# The model can produce something like:

# 0.90

# We can interpret that as approximately 90% predicted probability of class 1.

# For example:

# Probability = 0.90
#         ↓
# Prediction = 1

# while:

# Probability = 0.10
#         ↓
# Prediction = 0

# So sigmoid is useful because it converts the neuron's output into a probability-like value between 0 and 1, making it suitable for binary classification.

# 6. What happens inside a neuron?

# I would explain the whole process like this:

#              Inputs
#           x₁       x₂
#            ↓       ↓
#           w₁       w₂
#            ↓       ↓
#         x₁×w₁    x₂×w₂
#              \    /
#               \  /
#                ↓
#           Weighted Sum
#                +
#              Bias
#                ↓
#               z
#                ↓
#          Activation
#         (ReLU/Sigmoid)
#                ↓
#             Output

# Mathematically:

# z = x₁w₁ + x₂w₂ + b

# Then:

# output = activation(z)

# For example, with ReLU:

# x₁ = 4
# x₂ = 5

# w₁ = 0.3
# w₂ = 0.2

# b = 0.1

# The neuron does:

# 4 × 0.3 = 1.2
# 5 × 0.2 = 1.0

# 1.2 + 1.0 = 2.2

# 2.2 + 0.1 = 2.3

# ReLU(2.3) = 2.3
# 🧠 The most important thing to remember

# You can remember a neuron using just 4 steps:

# Input → Weight → Bias → Activation

# Or more precisely:

# Inputs
#   ↓
# Multiply by weights
#   ↓
# Add everything
#   ↓
# Add bias
#   ↓
# Activation function
#   ↓
# Output

# And this is the foundation of what happens repeatedly inside a neural network.