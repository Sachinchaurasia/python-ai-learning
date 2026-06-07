#Step 1-Import Libraries

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#Step 2-Create Dataset

data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
    
}
df=pd.DataFrame(data)

#Step 3- Features and Target

X=df[["Hours"]]
Y=df["Pass"]

#Step 4- Train test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42
)

#step 5-Create Random Forest Model
model=RandomForestClassifier(n_estimators=100,
                             random_state=42
)

#Step 6-Train the model
model.fit(X_train,Y_train)

#Step 7-Prediction
#make prediction for hour=5
prediction=model.predict([[5]])
print("Prediction for hour=5:",prediction[0])

#Step 8- Accuracy
score=model.score(X_test,Y_test)
print("model Accuracy",score)


#Featur Importance
importances=model.feature_importances_
feature_names=X.columns
feature_importance_dict=dict(zip(feature_names,importances))
print("Feature Importance:",feature_importance_dict)
