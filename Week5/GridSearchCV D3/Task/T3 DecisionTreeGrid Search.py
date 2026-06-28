# TASK 2 — Decision Tree Grid Search

# Try:

# max_depth

# 1
# 2
# 3
# 4
# 5

# Print:

# best_params

# best_score

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

#Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

#Features And target
X=df[["Hours"]]
Y=df["Pass"]

#create model
model=DecisionTreeClassifier(random_state=42)

#Hyperparameter Grid
param_grid={
    "max_depth":[1,2,3,4,5]
}

#GridSearch
grid=GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=3,
    scoring="accuracy"
)

#Train model
grid.fit(X,Y)

#Best Results
print("best Parameter:",grid.best_params_)
print("Best Score:",grid.best_score_)

#best model
print("\n best model")
print(grid.best_estimator_)
