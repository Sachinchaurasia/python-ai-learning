import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

data={
    "Experience":[1,2,4,6,8,10],
    "Promotion":[0,0,0,1,1,1]
}

df=pd.DataFrame(data)

#Features and Target
X=df[["Experience"]]
Y=df["Promotion"]

#models
models={
    "LogisticRegression":LogisticRegression(),
    "DecisionTree":DecisionTreeClassifier(random_state=42),
    "RandomForest":RandomForestClassifier(random_state=42),
    "KNN":KNeighborsClassifier(n_neighbors=3)
}

print("Model Comparison\n")

for name,model in models.items():
    scores=cross_val_score(model,X,Y,cv=3)
    print(f"{name}")
    print("CV scores",scores)
    print("Average Accuracy",scores.mean())
    
    print("-"*40)
    
#Create Comparison Table

results=[]
for name,model in models.items():
    scores=cross_val_score(model,X,Y,cv=3)
    results.append([
        name,
        round(scores.mean(),2)
    ])
comparison_df=pd.DataFrame(results,
                           columns=["Model","CV Accuracy"])
print(comparison_df)

#############------------OUTPUT--------------------

# Model Comparison

# LogisticRegression
# CV scores [0.5 1.  1. ]
# Average Accuracy 0.8333333333333334
# ----------------------------------------
# DecisionTree
# CV scores [0.5 1.  1. ]
# Average Accuracy 0.8333333333333334
# ----------------------------------------
# RandomForest
# CV scores [0.5 1.  1. ]
# Average Accuracy 0.8333333333333334
# ----------------------------------------
# KNN
# CV scores [0.5 1.  1. ]
# Average Accuracy 0.8333333333333334
# ----------------------------------------
#                 Model  CV Accuracy
# 0  LogisticRegression         0.83
# 1        DecisionTree         0.83
# 2        RandomForest         0.83
# 3                 KNN         0.83




# 🎯 What You Learn
# LogisticRegression → Linear classification model.
# DecisionTreeClassifier → Rule-based classification.
# RandomForestClassifier → Ensemble of many decision trees.
# KNeighborsClassifier → Predicts using nearest neighbors.
# cross_val_score() → Evaluates each model fairly using multiple folds.

#  Interview Tip

# You should not choose a model just because it performs well on one train-test split. Comparing multiple models with cross-validation helps identify which model generalizes best to unseen data. This is a standard practice used by AI Engineers before selecting a final model for deployment. 🚀