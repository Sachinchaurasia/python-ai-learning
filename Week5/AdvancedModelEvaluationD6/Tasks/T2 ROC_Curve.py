import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve

data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}

df=pd.DataFrame(data)

X=df[["Hours"]]
Y=df["Pass"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=42,stratify=Y)

model=LogisticRegression()
model.fit(X_train, Y_train)

Y_pred_proba=model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds=roc_curve(Y_test, Y_pred_proba)

print("False Positive Rate:", fpr)
print("True Positive Rate:", tpr)

print("Thresholds:", thresholds)


# Interview Answer (2 lines)
#Why do we use stratify=y in train_test_split?

# stratify=y ensures that the class distribution remains the same in both the training and testing datasets. It prevents one class from being missing in either split, making model evaluation more reliable, especially for small or imbalanced datasets.