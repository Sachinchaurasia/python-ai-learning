# TASK 1 — KNN Tuning

# Dataset:

# data = {
#     "Hours":[1,2,3,4,5,6],
#     "Pass":[0,0,0,1,1,1]
# }

# Try:

# K = 1
# K = 3
# K = 5

# Print:

# Cross Validation Scores
# Average Accuracy

# Find best K.

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Values of K to test
k_values=[1,3]
best_k=None
best_accuracy=0

for k in k_values:
    model=KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(model,X,Y,cv=3)
    
print(f"\n K={k}")
print("Cross Validation Scores:",scores)
print("Average Accuracy:",scores.mean())
if scores.mean()>best_accuracy:
    best_accuracy=scores.mean()
    best_k=k
print("\n Best k=",best_k)

print("Best Average Accuracy",best_accuracy)
