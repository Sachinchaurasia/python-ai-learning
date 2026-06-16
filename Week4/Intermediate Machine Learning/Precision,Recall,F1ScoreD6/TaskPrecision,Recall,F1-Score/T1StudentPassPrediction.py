#Import Libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
    
)

#Create dataset
data={
    "Hours":[1,2,3,4,5],
    "Pass":[0,0,1,1,1]
}
df=pd.DataFrame(data)
print(df)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train\test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)
#Create model
model=LogisticRegression()

#Train model
model.fit(X_train,Y_train)

#Make predictions
Y_pred=model.predict(X_test)
print(Y_pred)

#Precision
precision=precision_score(Y_test,Y_pred)
print(precision)

#Recall
recall=recall_score(Y_test,Y_pred)
print(recall)

#F1 score
f1=f1_score(Y_test,Y_pred)
print(f1)

 ####################################################################################
 
# Dataset:

# data = {
#     "Hours":[1,2,3,4,5],
#     "Pass":[0,0,1,1,1]
# }

# Let's assume the model predicts:

# Actual    = [0,0,1,1,1]
# Predicted = [0,1,1,1,1]
# Step 1: Confusion Matrix Values
# Actual	Predicted	Result
# 0	0	TN
# 0	1	FP
# 1	1	TP
# 1	1	TP
# 1	1	TP

# Therefore:

# TP = 3
# TN = 1
# FP = 1
# FN = 0
# Step 2: Precision

# Formula:

# Precision=
# TP+FP
# TP
# 	​


# Calculation:

# Precision=
# 3+1
# 3
# 	​

# Precision=
# 4
# 3
# 	​

# Precision=0.75

# Precision = 75%

# Step 3: Recall

# Formula:

# Recall=
# TP+FN
# TP
# 	​


# Calculation:

# Recall=
# 3+0
# 3
# 	​

# Recall=1.0

# Recall = 100%

# Step 4: F1 Score

# Formula:

# F1=
# Precision+Recall
# 2×Precision×Recall
# 	​


# Calculation:

# F1=
# 0.75+1.0
# 2×0.75×1.0
# 	​

# F1=
# 1.75
# 1.5
# 	​

# F1=0.857

# F1 Score ≈ 85.7%

# 
from sklearn.metrics import precision_score, recall_score, f1_score

y_true = [0,0,1,1,1]
y_pred = [0,1,1,1,1]

print("Precision =", precision_score(y_true, y_pred))
print("Recall =", recall_score(y_true, y_pred))
print("F1 Score =", f1_score(y_true, y_pred))
# Output
# Precision = 0.75
# Recall = 1.0
# F1 Score = 0.8571
