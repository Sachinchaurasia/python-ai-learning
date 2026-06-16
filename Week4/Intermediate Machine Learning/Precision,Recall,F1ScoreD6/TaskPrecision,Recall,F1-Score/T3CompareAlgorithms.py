import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

#Dataset
data={
    "Experience":[1,2,4,6,8],
    "Promotion":[0,0,1,1,1]
    
}
df=pd.DataFrame(data)
print(df)
#Feature and Target
X=df[["Experience"]]
Y=df["Promotion"]

#Models creation
models={
    "Logistic Regression":LogisticRegression(),
    "Decision Tree":DecisionTreeClassifier(),
    "RandomForest":RandomForestClassifier(n_estimators=100),
    "KNN":KNeighborsClassifier(n_neighbors=3)
}

results=[]

#Train models
for name,model in  models.items():
    model.fit(X,Y)
   
#Make Prediction
Y_pred=model.predict(X)
    
acc=accuracy_score(Y,Y_pred)

prec=precision_score(Y,Y_pred)
rec=recall_score(Y,Y_pred)
f1=f1_score(Y,Y_pred)
results.append([name,acc,prec,rec,f1])
results_df=pd.DataFrame(results,
                        columns=["Model","Accuracy","Precision","Recall","F1"])
print(results_df)
