
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

#dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}

#Create Dataframe
df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train/Test Split
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)   

#Train the model
model=LogisticRegression()
model.fit(X_train, Y_train)

#Predict
Y_pred=model.predict(X_test)

#Print Actual And predicted values
print("Actual Values:",Y_test.values)

print("Predicted Values:",Y_pred)

#Print Classification Report
print("\nClassification Report:")
print(classification_report(Y_test, Y_pred))

