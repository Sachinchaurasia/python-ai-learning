import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6,7,8],
    "Pass":[0,0,0,1,1,1,1,1]
}
df= pd.DataFrame(data)
print(df)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Try Different K values
for k in [1,3,5,7]:
    model=KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(model,X,Y,cv=4)
    print("k=",k)
    print("Average Accuracy",scores.mean())
    print("-"*30)


#Decision Tree HyperParameters
from sklearn.tree import(DecisionTreeClassifier)

for depth in [1,2,3,4,5]:
    model=DecisionTreeClassifier(max_depth=depth,
                                 random_state=42)
    scores=cross_val_score(model,
                           X,
                           Y,
                           cv=4)
    print("Depth:",depth)
    print("CV Accuracy",scores.mean())
    
    
#RandomForestTuning
from sklearn.ensemble import (RandomForestClassifier)
for trees in [10,50,100,200]:
    model=RandomForestClassifier(n_estimators=trees,
                                 random_state=42)
    scores=cross_val_score(model,
                           X,
                           Y,
                           cv=4)
    print("Trees",trees)
    print("CV Accuracy",scores.mean())
    
     