# 🔥 TASK 3 — Pipeline + GridSearchCV

# Tune:

# n_neighbors

# 1
# 3
# 5
# 7

# using:

# GridSearchCV

# Print:

# grid.best_params_

# grid.best_score_

import pandas as pd
from sklearn.model_selection import train_test_split ,GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)
    

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train/test Split

X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.33,
                                               random_state=42)

#Create Pipeline
pipeline=Pipeline([
    ("Scaler",StandardScaler()),
    ("knn",KNeighborsClassifier())
    
])

#Parameters to tune

param_grid={
    "knn__n_neighbors":[1,3,5,7]
}

#GridSearchCV

grid=GridSearchCV(
    pipeline,
    param_grid,
    cv=3
)

#Train Grid Search
grid.fit(X_train,Y_train)

#Best parameters
print("Best Parameters")
print(grid.best_params_)

#Best cross Validation Score
print("\n Best CV Score")
print(grid.best_score_)
