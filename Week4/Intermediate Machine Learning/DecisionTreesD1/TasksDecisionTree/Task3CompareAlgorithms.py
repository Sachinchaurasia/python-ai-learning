#Train 
# Logistic Regression
# Decision Tree
#compare Accuracy of both algorithms on the same data set

import pandas as pd

data={
    "Income":[20000,30000,50000,70000],
    "Approved":[0,0,1,1]
    
}

df=pd.DataFrame(data)
print(data)

#Features and Target
X=df[["Income"]]
Y=df["Approved"]

#Train Test Split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)
#Create Model
from sklearn.linear_model import LogisticRegression

LR_model=LogisticRegression()

#Train Model
LR_model.fit(X_train,Y_train)

#Make Prediction
LR_Prediction=LR_model.predict(X_test)

#Accuracy
LR_Accuracy=LR_model.score(X_test,Y_test)
print("LogisticRegression Accuracy",LR_Accuracy)

###################################################################
#Decision Tree
from sklearn.tree import DecisionTreeClassifier
#create model
DT_model=DecisionTreeClassifier(random_state=42)

#Train model
DT_model.fit(X_train,Y_train)

#Make Prediction
DT_prediction=DT_model.predict(X_test)

#Accuracy
DT_Accuracy=accuracy_score(Y_test,DT_prediction)

print("DecisionTree Accuracy",DT_Accuracy)


#Compare Results
print("\n Comparision ")
print("LogisiticRegression",LR_Accuracy)
print("Decision Tree",DT_Accuracy)

if LR_Accuracy>DT_Accuracy:
    print("Logistic Regression is better")
elif DT_Accuracy>LR_Accuracy:
    print("Decision Tree is better")
else:
    print("Both Performed Equally")
    