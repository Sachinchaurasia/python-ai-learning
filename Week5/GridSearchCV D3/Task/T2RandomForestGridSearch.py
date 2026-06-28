#  TASK 3 — Random Forest Grid Search

# Search:

# n_estimators

# 10
# 50
# 100

# and

# max_depth

# 2
# 4
# 6

# Find the best combination.

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

#Create Dataset

data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
    
}
df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Create RandomForest model
model=RandomForestClassifier(random_state=42)

#Hyperparameter Grid
param_grid={
    "n_estimators":[10,50,100],
    "max_depth":[2,4,6]
}

#Grid Search
grid=GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=3,
    scoring="accuracy"
)

#Train Grid Search

grid.fit(X,Y)

#Best Parameters
print("Best parameters:",grid.best_params_)
print("Best Score",grid.best_score_)

#Best Model
best_model=grid.best_estimator_
print("\n Best model")
print(best_model)
