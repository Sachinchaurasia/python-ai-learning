import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

#create Dataset
data={
    "Income":[20000,30000,50000,70000],
    "Approval":[0,0,1,1]
}
df=pd.DataFrame(data)

#Features and target
X=df[["Income"]]
Y=df["Approval"]

#create model
model=KNeighborsClassifier(n_neighbors=3)

#train model
model.fit(X,Y)

#Make prediction for Income=60000
prediction=model.predict([[60000]])
print("prediction :",prediction)

