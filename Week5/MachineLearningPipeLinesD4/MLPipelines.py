import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6,7,8],
    "Pass":[0,0,0,1,1,1,1,1]
}
df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train /Test Split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)
#Create PipeLines
pipeline=Pipeline([
    ("scaler",StandardScaler()),
    ("model",KNeighborsClassifier(n_neighbors=3))
    
])

#Train Pipeline
pipeline.fit(X_train,Y_train)

#Make Predictions
Y_pred=pipeline.predict(X_test)
print(Y_pred)

#Calculate Accuracy
print(pipeline.score(X_test,Y_test))

################################################################################
#Pipeline with Logisitic Regression
from sklearn.linear_model import LogisticRegression

pipeline=Pipeline([
    ("Scaler",StandardScaler()),
    ("model",LogisticRegression())
])

pipeline.fit(X_train,Y_train)

print(pipeline.score(X_test,Y_test))

#################################################################################
#Pipeline +Cross Validation
from sklearn.model_selection import cross_val_score
scores=cross_val_score(
    pipeline,
    X,
    Y,
    cv=5
)
print(scores)
print(scores.mean())

#####################################################################################
# Pipeline +GridSearchCV

from sklearn.model_selection import GridSearchCV
params={
    "model__n_neighbors":[1,3,5,7]

}

grid=GridSearchCV(
    pipeline,
    param_grid=params,
    cv=5
)

grid.fit(X,Y)

print(grid.best_params_)               
print(grid.best_score_)
