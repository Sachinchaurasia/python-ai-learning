#Decision Tree Hyperparameter Tuning(max_depth)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

#Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

#Featured And Target
X=df[["Hours"]]
Y=df["Pass"]

#Depth Values to test
depth_values=[1,2,3,4,5]
best_depth=None
best_score=0

print("Decision Tree Hyperparameter Tuning/n")

for depth in depth_values:
    model=DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

scores=cross_val_score(model,X,Y,cv=3)
print(f" max_depth={depth}")
print("CV scores:",scores)
print("Average Accuracy:",scores.mean())
print("-"*40)

if scores.mean()>best_score:
    best_score=scores.mean()
    best_depth=depth
    
print("\n Best max depth:",best_depth)
print("Best Average Accuracy:",best_score)

