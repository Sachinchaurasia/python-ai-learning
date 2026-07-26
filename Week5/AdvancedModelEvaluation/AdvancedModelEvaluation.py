import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (classification_report)

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
    test_size=0.2,
    random_state=42
)

#Train the emodel
model=LogisticRegression()
model.fit(X_train,Y_train)

#Predict

Y_pred=model.predict(X_test)

#Classification report
print(
    classification_report(Y_test,Y_pred)
    )
from sklearn.metrics import (
    roc_curve
)
#Generate Probablity Scores
Y_prob=model.predict_proba(X_test)[:,1]

#Compute ROC values
fpr,tpr,thresholds=roc_curve(
    Y_test,
    Y_prob
)

print(fpr)
print(tpr)

from sklearn.metrics import (roc_auc_score)

auc=roc_auc_score(Y_test,Y_prob)
print("AUC: ",auc)

