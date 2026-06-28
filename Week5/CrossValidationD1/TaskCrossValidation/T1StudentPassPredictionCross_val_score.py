# TASK 1 — Student Pass Prediction

# Dataset:

# data = {
#     "Hours":[1,2,3,4,5,6],
#     "Pass":[0,0,0,1,1,1]
# }

# Apply:

# cross_val_score()

# Print:

# Fold scores
# Average score


import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}

df=pd.DataFrame(data)

print(df)

#Features And Taget
X=df[["Hours"]]
Y=df["Pass"]

#Create Model
model=LogisticRegression()

#Cross validation
scores=cross_val_score(model,
                 X,
                 Y,
                 cv=3
)

print(scores)
print(scores.mean())


# 📌 Explanation
# cross_val_score() splits the dataset into multiple folds.
# The model is trained on some folds and tested on the remaining fold.
# This process repeats for each fold.
# The returned scores show the accuracy for each fold.
# scores.mean() gives the average accuracy across all folds.
# Example Output
# Fold Scores: [1. 1. 1.]
# Average Score: 1.0

# (The exact values may vary depending on the dataset and folds.)

# 🎯 What You Learn
# Model validation
# Avoiding overfitting
# Evaluating model stability
# Cross-validation, which is widely used by AI Engineers before deploying models

# Interview Tip: Cross-validation gives a more reliable estimate of model performance than a single train-test split because the model is tested on multiple subsets of the data.