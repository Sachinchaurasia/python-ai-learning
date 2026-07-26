import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
roc_auc_score
)

#create Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}

df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train/Test Split
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.33,
    random_state=42,
    stratify=Y)

#Train the model
model=LogisticRegression()
model.fit(X_train, Y_train)

#Predict probabilities
y_pred_proba=model.predict_proba(X_test)[:, 1]

#Calculate AUC Score
auc_score=roc_auc_score(Y_test, y_pred_proba)
print(f"AUC Score: {auc_score}")    

#Interpretation
if auc_score > 0.90:
    print("Excellent model performance")
elif auc_score > 0.80:
    print("Good model performance") 
elif auc_score > 0.70:
    print("Fair model performance")
else:
    print("Poor model performance")
    
    