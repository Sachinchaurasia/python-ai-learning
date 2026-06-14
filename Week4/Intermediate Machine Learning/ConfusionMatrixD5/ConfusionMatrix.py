#Step 1--Import Libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


#Step 2--create Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)
print(df)

#Step--3 Features and Target

X=df[["Hours"]]
Y=df["Pass"]

#Step 4--Train/Test Split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)

#Step 5--Train Logistic Regression
model=LogisticRegression()
model.fit(X_train,Y_train)

#Step 6--Make Prediction
Y_pred=model.predict(X_test)
print(Y_pred)

#Step 7--Calculate accuracy
accuracy=model.score(X_test,Y_test)
print("Accuracy",accuracy)

#Step 8--Generate confusion matrix
cm=confusion_matrix(Y_test,Y_pred)
print(cm)

#Step 9--Extract TN,FP,FN,TP
TN,FP,FN,TP=confusion_matrix(Y_test,Y_pred).ravel()

print("TN=",TN)
print("FP=",FP)
print("FN=",FN)
print("TP=",TP)
