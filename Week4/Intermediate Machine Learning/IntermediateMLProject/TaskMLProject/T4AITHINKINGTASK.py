#  TASK 4 — AI THINKING TASK
# Why Might Random Forest Outperform a Single Decision Tree?

# A Decision Tree makes predictions using only one tree. While it is easy to understand, it can sometimes overfit the training data and perform poorly on new data.

# A Random Forest solves this problem by creating many Decision Trees instead of just one.

# 1. Multiple Trees

# Random Forest trains multiple decision trees on different random subsets of the data.

# Each tree learns slightly different patterns.

# This allows the model to capture more information than a single tree.

# 2. Voting Mechanism

# For classification problems, every tree makes a prediction.

# The final prediction is decided by majority voting.

# Example:

# Tree 1 → Promotion
# Tree 2 → Promotion
# Tree 3 → No Promotion
# Tree 4 → Promotion
# Tree 5 → Promotion

# Most trees vote for:

# Promotion

# So the final prediction is:

# Promotion

# This reduces the impact of mistakes made by individual trees.

# 3. Reduces Overfitting

# A single Decision Tree can memorize the training data.

# This may lead to excellent training accuracy but poor performance on unseen data.

# Random Forest averages the predictions of many trees, reducing overfitting and improving generalization.

# 4. More Robust

# If one tree makes a wrong prediction because of noise or unusual data, other trees can correct it through voting.

# Therefore Random Forest is usually more stable and reliable than a single Decision Tree.

# Interview Answer

# Random Forest often performs better than a single Decision Tree because it combines predictions from multiple trees using a voting mechanism. This reduces the impact of errors made by individual trees, lowers overfitting, and improves robustness. As a result, Random Forest generally provides more accurate and reliable predictions on unseen data than a single Decision Tree.