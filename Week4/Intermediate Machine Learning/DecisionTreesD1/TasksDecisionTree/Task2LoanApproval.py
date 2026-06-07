#Loan approval
import pandas as pd

data={
    "Income":[20000,30000,50000,70000],
    "Approved":[0,0,1,1]
}

df=pd.DataFrame(data)
print(df)

#Features and Target
X=df[["Income"]]
Y=df["Approved"]

#Create Model
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(random_state=42)
#Train Model
model.fit(X,Y)

#Make prediction for income =60000
prediction=model.predict([[60000]])

print("prediction",prediction[0])
if prediction[0]==1:
    print("Loan Approved")
else:
    print("Loan Not Approved")
    