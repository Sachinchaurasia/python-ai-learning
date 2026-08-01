#Feature Engineering

import pandas as pd

#create Dataset
data={
    "Experience":[1,2,3,4,5],
    "Skills":[2,3,5,7,9],
    "Salary":[30000,40000,50000,60000,70000]
}

df=pd.DataFrame(data)
print(df)

#Create A new feature by combining Experience and Skills
df["Experience_Skills"]=(
    df["Experience"]*df["Skills"]
)
print(df)

#Selecting Features

X=df[
    [
        "Experience",
        "Skills",
        "Experience_Skills"
    ]
]

#Target
Y=df["Salary"]

#Train Linear Regression
from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(X,Y)

#Predict
prediction=model.predict(
    [[6,10,60]]
)

print(prediction)

