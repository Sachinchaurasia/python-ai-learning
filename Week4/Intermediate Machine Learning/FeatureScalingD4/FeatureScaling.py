#Step 1--import Libraries

import pandas as pd
from sklearn.preprocessing import StandardScaler

#Step 2--create dataset
data={
    "Experience":[1,2,3,4,5],
    "Salary":[30000,40000,50000,60000,70000]
}
df=pd.DataFrame(data)
print(df)

#Step -3  Create Scaler
scaler=StandardScaler()

#Step 4--Scale Features
scaled_data=scaler.fit_transform(df)
print(scaled_data)

#Step-5 Scale only Features
X=df[["Experience"]]
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

########################################################################################
#Step 6--KNN with Scaling
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

X=df[["Hours"]]
Y=df["Pass"]

#Scale:
scaler=StandardScaler()
x_scaled=scaler.fit_transform(X)

#Split:
X_train,X_test,Y_train,Y_test=train_test_split(X_scaled,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)
#Train
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,Y_train)

#Evaluate
print(model.score(X_test,Y_test))

#Common Scaling Methods
#1-Standard Scaler
#2-MinMaxScaler

