# Step ---1---import Libraries

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#Step---2--Create dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

#Step -3----Features and Target

X=df[["Hours"]]
Y=df["Pass"]

#Step-4---Train/test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)
# Step-5---Create KNN Model
model=KNeighborsClassifier(n_neighbors=3)

#K=numbers of neighbors considered--Look at 3 closest data points

#Step-6---Train Model
model.fit(X_train,Y_train)

#Step--7---Make prediction for Hours=5
predictions=model.predict([[5]])
print(predictions)

#Step-8--Accuracy
score=model.score(X_test,Y_test)
print(score)