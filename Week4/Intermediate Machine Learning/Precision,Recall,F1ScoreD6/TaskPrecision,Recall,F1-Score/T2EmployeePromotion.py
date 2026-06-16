# TASK 2 — Employee Promotion

# Dataset:

# data = {
#     "Experience":[1,2,4,6,8],
#     "Promotion":[0,0,1,1,1]
# }

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score,recall_score,f1_score

#Dataset
data={
    "Experience":[1,2,4,6,8],
    "Promotion":[0,0,1,1,1]
}
df=pd.DataFrame(data)

#Features and Target
X=df[["Experience"]]
Y=df["Promotion"]

#Train Model
model=LogisticRegression()
model.fit(X,Y)

#Predictions
Y_pred=model.predict(X)

#Metrics
print("Precision=",precision_score(Y,Y_pred))
print("Recall=",recall_score(Y,Y_pred))
print("f1 SCore=",f1_score(Y,Y_pred))
