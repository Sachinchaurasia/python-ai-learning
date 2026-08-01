#Build a pipeline
#Dataset

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}

df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train/Test Split

X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.33,
    random_state=42
)

#Create Pipeline
Pipeline=Pipeline([
    ("Scaler",StandardScaler()),
    ("knn",KNeighborsClassifier(n_neighbors=3))
])

#Train the pipeline

Pipeline.fit(X_train,Y_train)

#predict test data
predictions=Pipeline.predict(X_test)

#Print results
print("Actual Values")
print(Y_test.values)

print("\n Predicted Values")
print(predictions)

#Accuracy
accuracy=Pipeline.score(X_test,Y_test)
print("\n Accuracy",accuracy)

#Predict new Data
new_prediction=Pipeline.predict([[5]])
print("\n Prediction for 5 hours:",new_prediction)


