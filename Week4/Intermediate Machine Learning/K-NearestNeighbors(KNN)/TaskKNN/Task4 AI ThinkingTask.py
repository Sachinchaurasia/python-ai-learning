# #  TASK 4 — AI THINKING TASK

# # Why might KNN become slow on very large datasets?

# # Think about:

# # finding neighbors
# # distance calculations
# # dataset size

# Why might KNN become slow on very large datasets?

# KNN (K-Nearest Neighbors) does not learn a mathematical formula during training. Instead, it stores all the training data and uses it when making predictions.

# 1. Finding Neighbors

# When a new data point arrives, KNN must find the nearest neighbors.

# Example:

# New Income = 60000

# KNN checks which existing data points are closest to 60000.

# 2. Distance Calculations

# To find the nearest neighbors, KNN calculates the distance between the new point and every training example.

# For example:

# Distance(60000, 20000)
# Distance(60000, 30000)
# Distance(60000, 50000)
# Distance(60000, 70000)
# ...

# With a small dataset, this is fast.

# 3. Dataset Size Matters

# Suppose:

# 100 records → 100 distance calculations
# 10,000 records → 10,000 distance calculations
# 1,000,000 records → 1,000,000 distance calculations

# As the dataset grows, prediction takes longer because KNN must compare the new point with many existing records.

# Example

# Imagine finding the three people closest to your age:

# In a room of 10 people → quick
# In a stadium of 50,000 people → much slower

# KNN faces the same challenge.

# Conclusion

# KNN can become slow on very large datasets because it must calculate distances to many data points every time a prediction is made. More records mean more distance calculations and more time required to find the nearest neighbors.

# Interview Answer

# KNN may become slow on large datasets because it needs to calculate the distance between the new data point and many training examples to find the nearest neighbors. As the dataset size increases, the number of distance calculations increases, making prediction slower and more computationally expensive.