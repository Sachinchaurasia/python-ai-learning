#Import Libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import( confusion_matrix,
                            precision_score,
                            recall_score,
                            f1_score)

#Create Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train/Test Split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)
#Train  model
model=LogisticRegression()
model.fit(X_train,Y_train)

#Make Prediction
Y_pred=model.predict(X_test)

#Precision 
precision=precision_score(Y_test,Y_pred)

print("Precision",precision)

#Recall
recall=recall_score(Y_test,Y_pred)
print("Recall:",recall)

#F1-Score
f1=f1_score(Y_test,Y_pred)
print("f1_score:",f1)


