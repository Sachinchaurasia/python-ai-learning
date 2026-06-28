import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6,7,8],
    "Pass":[0,0,0,1,1,1,1,1]
}
df=pd.DataFrame(data)
print(df)

#Features and Target

X=df[["Hours"]]
Y=df["Pass"]

#Create Model
model=LogisticRegression()

#Apply Cross Validation

scores=cross_val_score(model,
                       X,
                       Y,
                       cv=5
                       )
#Print Scores
print(scores)

#Average Score
print(scores.mean())

#Compare Multiple Algorithms
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


#Create Models
models={
    "LogisticRegression":LogisticRegression(),
    "DecisionTree":DecisionTreeClassifier(),
    "RandomForest":RandomForestClassifier(),
    "KNN":KNeighborsClassifier()
}

#Evaluate All Models

for name,model in models.items():
    scores=cross_val_score(model,
                           X,
                           Y,
                           cv=5)
    print(name)
    print("Scores:",
          scores)
    print("average:",
          scores.mean()
          )
    print("-"*30)
    