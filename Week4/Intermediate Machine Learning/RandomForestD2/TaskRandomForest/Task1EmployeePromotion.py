#Step 1 import Libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#Step 2--Create DataFrame
data={
    "Experience":[1,2,4,6,8],
    "Promotion":[0,0,1,1,1]
}

df=pd.DataFrame(data)

#Step 3--Features and Target
X=df[["Experience"]]
Y=df["Promotion"]

#Step 4-- Train test split data

X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42
)

#Step 5 --Create RandomForest model
model=RandomForestClassifier(n_estimators=100,random_state=42)

#Step 6--Train the model
model.fit(X_train,Y_train)

#Step 7-- Make the prediction
predictions=model.predict([[5]])
print(predictions)

#Step 8--Accuracy of the model
accuracy=model.score(X_test,Y_test)
print(accuracy)

