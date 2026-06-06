import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#Create Dataset

data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
    
}

df=pd.DataFrame(data)
print(df)

#Features and Target

X=df[["Hours"]]
Y=df["Pass"]

#Train/Test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42
                                               )
#Train Decision Tree

model=DecisionTreeClassifier()
model.fit(X_train,Y_train)

#Predict
#Predict for 4 or 7 hours of study
prediction=model.predict([[7]])
print(prediction)

#Accuracy
score=model.score(X_test,Y_test)
print("Accuracy",score)


