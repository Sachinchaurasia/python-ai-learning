#Step 1-import libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#Step 2-create dataset
data={
    "Hours":[1,2,3,4,5],
    "Pass":[0,0,1,1,1]
}
df=pd.DataFrame(data)
print(df)

#Step 3--Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train/Test split
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

#Train Logistic model
model=LogisticRegression()
model.fit(X_train,Y_train)

#Make Prediction
Y_pred=model.predict(X_test)
print("Actual Values")
print(Y_test.values)
print("Predicted values")
print(Y_pred)

#Create Confusion matrix
cm=confusion_matrix(Y_test,Y_pred)
print(cm)

# 0      1     0
# 1      2     0
# 2      3     1
# 3      4     1
# 4      5     1
# Actual Values
# [0]
# Predicted values
# [1]
# [[0 1]
#  [0 0]]