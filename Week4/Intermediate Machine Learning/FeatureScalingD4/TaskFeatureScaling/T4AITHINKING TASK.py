#  TASK 4 — AI THINKING TASK
# Why is Feature Scaling Especially Important for KNN?

# KNN (K-Nearest Neighbors) makes predictions based on the distance between data points.

# Because distance is the core of the algorithm, feature scaling is very important.

# 1. Distance Calculations

# Suppose we have two features:

# Experience	Salary
# 5	50000

# The ranges are:

# Experience : 1 to 10
# Salary     : 20,000 to 80,000

# Notice that Salary values are much larger.

# When KNN calculates distance, Salary contributes much more than Experience.

# As a result, Experience has very little effect on the prediction.

# 2. Nearest Neighbors Depend on Distance

# KNN finds the closest data points (neighbors).

# If one feature has a much larger scale, the algorithm may choose neighbors based almost entirely on that feature.

# This can lead to incorrect predictions.

# Example:

# Employee A:
# Experience = 5
# Salary = 50000

# Employee B:
# Experience = 6
# Salary = 51000

# Employee C:
# Experience = 10
# Salary = 50010

# Without scaling, Salary may dominate the distance calculation, making KNN focus more on Salary than Experience.

# 3. Feature Dominance

# Feature dominance occurs when one feature has much larger numerical values than others.

# Example:

# Experience = 5
# Salary = 50000

# Since 50000 is much larger than 5, Salary dominates the distance calculation.

# After scaling:

# Experience ≈ 0.5
# Salary ≈ 0.5

# Now both features contribute fairly.

# Conclusion

# Feature scaling is especially important for KNN because KNN relies on distance calculations to find the nearest neighbors. Without scaling, features with larger values can dominate the distance measure and influence predictions unfairly. Scaling ensures that all features contribute equally, helping KNN find more meaningful neighbors and often improving accuracy.

# Interview Answer

# Feature scaling is important for KNN because KNN uses distance calculations to identify the nearest neighbors. If one feature has a much larger scale than another, it can dominate the distance calculation and reduce the influence of other features. Scaling brings features to a similar range, ensuring fair distance measurements and better predictions.