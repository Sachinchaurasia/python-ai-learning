#GridSearchCV->Hyperparameter->CrossValidation->AverageScore->Compare->Best Model

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6,7,8],
    "Pass":[0,0,0,1,1,1,1,1]
}

df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Create model
model=KNeighborsClassifier()

#Create Parameter Grid
params={
    "n_neighbors":[1,3,5,7]
}

#Create GridSearchCV
grid=GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=5
)

#Train Grid Search
grid.fit(X,Y)

#Best Hyperparameter
print(grid.best_params_)

#Best Accuracy
print(grid.best_score_)

#Best Model
best_model=grid.best_estimator_
print(best_model)

#Decision Tree Example
from sklearn.tree import DecisionTreeClassifier

model=DecisionTreeClassifier()

params={
    "max_depth":[1,2,3,4,5]
}

grid=GridSearchCV(model,
                  params,
                  cv=5)
grid.fit(X,Y)
print(grid.best_params_)
print(grid.best_score_)

#RandomForest Example

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(
    random_state=42
)

params={
    "n_estimators":[10,50,100],
    "max_depth":[2,4,6]
}
grid=GridSearchCV(
    model,
    params,
    cv=5
    
)

grid.fit(X,Y)
print(grid.best_params_)
print(grid.best_score_)
