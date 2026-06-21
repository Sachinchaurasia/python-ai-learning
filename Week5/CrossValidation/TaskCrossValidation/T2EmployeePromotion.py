# TASK 2 — Employee Promotion

# Dataset:

# data = {
#     "Experience":[1,2,4,6,8,10],
#     "Promotion":[0,0,0,1,1,1]
# }

# Use:

# LogisticRegression

# Calculate:

# cross_val_score()

import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

#create Dataset
data={
    "Experience":[1,2,4,6,8,10],
    "Promotion":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)
print(df)

#Features and Target
X=df[["Experience"]]
Y=df["Promotion"]

#Create Model
model=LogisticRegression()

#Cross Validation
scores=cross_val_score(model,X,Y,cv=3)

#print scores
print("Fold Scores:",scores)

#print average 
print("Average scores:",scores.mean())


# 1           2          0
# 2           4          0
# 3           6          1
# 4           8          1
# 5          10          1

# Fold Scores: [0.5 1.  1. ]
# Average scores: 0.8333333333333334

# 📌 What is happening?

# LogisticRegression() creates a classification model.
# cross_val_score() divides data into 3 folds (cv=3).
# The model trains on 2 folds and tests on 1 fold.
# This repeats 3 times.
# The scores from each fold are returned.
# scores.mean() gives the overall average accuracy.

# 🎯 Why use Cross Validation?

# Uses the entire dataset for both training and testing.
# Gives a more reliable performance estimate.
# Reduces the risk of getting lucky with a single train-test split.
# Helps detect overfitting before deployment.

# AI Thinking

# A model that scores 100% on one train-test split may still perform poorly on new data. Cross-validation checks the model on multiple data splits, making the evaluation more trustworthy.
