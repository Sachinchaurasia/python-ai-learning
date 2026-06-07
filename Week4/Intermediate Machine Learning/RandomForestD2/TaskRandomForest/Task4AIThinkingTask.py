# Why can Random Forest perform better than a single Decision Tree?

# A Decision Tree makes predictions using only one tree.

# If that tree learns some wrong patterns from the training data (overfitting), its predictions can be inaccurate.

# A Random Forest solves this problem by creating many Decision Trees and combining their predictions.

# 1. Multiple Trees

# Instead of relying on one tree:

# Tree 1
# Tree 2
# Tree 3
# ...
# Tree 100

# Random Forest trains many trees using different subsets of data.

# This allows different trees to learn different patterns.

# 2. Voting

# Suppose we want to predict loan approval.

# Predictions from trees:

# Tree 1 → Approved
# Tree 2 → Approved
# Tree 3 → Not Approved
# Tree 4 → Approved
# Tree 5 → Approved

# Votes:

# Approved      = 4
# Not Approved  = 1

# Final Prediction:

# Approved

# The forest chooses the majority vote.

# 3. Reducing Mistakes

# A single tree may make a wrong decision because:

# Training data is small
# Noise exists in data
# Tree overfits

# Random Forest reduces this risk because:

# One tree can be wrong.
# Many trees are less likely to be wrong together.

# Individual mistakes tend to cancel out.

# Real-Life Example

# Imagine asking one doctor for a diagnosis.

# The doctor might make a mistake.

# Now imagine asking 100 experienced doctors and taking the majority opinion.

# Usually, the group decision is more reliable.

# Decision Tree = One doctor

# Random Forest = Many doctors voting

# Interview Answer

# Random Forest often performs better than a single Decision Tree because it combines predictions from multiple trees. Each tree learns different patterns from the data, and the final prediction is made using majority voting. This reduces overfitting, lowers the impact of individual tree mistakes, and generally improves accuracy and generalization on unseen data.