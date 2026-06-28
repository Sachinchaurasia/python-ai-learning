#  TASK 1 — KNN Grid Search

# Dataset:

# data = {
#     "Hours":[1,2,3,4,5,6],
#     "Pass":[0,0,0,1,1,1]
# }

# Try:

# n_neighbors

# 1
# 3
# 5
# 7

# Print:

# grid.best_params_

# grid.best_score_


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

#Features and target
X=df[["Hours"]]
Y=df["Pass"]

#Create KNN Model
model=KNeighborsClassifier()

#Hyperparameter to search
param_grid={
    "n_neighbors":[1,3,5,7]
}

#Grid Search
grid=GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=3
)

#Train
grid.fit(X,Y)

#Best Parameters
print("Best parameters",grid.best_params_)

#Best Score
print("Best Score",grid.best_score_)

