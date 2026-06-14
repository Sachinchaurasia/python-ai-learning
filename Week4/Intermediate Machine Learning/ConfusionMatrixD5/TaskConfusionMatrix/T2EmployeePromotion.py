#Employee Promotion
#import libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


#create dataset
data={
    "Experience":[1,2,4,6,8],
    "Promotion":[0,0,1,1,1]
    
}
df=pd.DataFrame(data)
print(df)

#Features and Target
X=df[["Experience"]]
Y=df["Promotion"]

#Train /test split=split data
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.4,
                                               random_state=42)
#Train classification model
model=DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

#Make prediction
Y_pred=model.predict(X_test)
print("Actual values")
print(Y_test)
print("predicted values")
print(Y_pred)

#Generate confusion matrix
cm=confusion_matrix(Y_test,Y_pred)
print(cm)


#    Experience  Promotion
# 0           1          0
# 1           2          0
# 2           4          1
# 3           6          1
# 4           8          1
# Actual values
# 1    0
# 4    1
# Name: Promotion, dtype: int64
# predicted values
# [0 1]
# [[1 0]
#  [0 1]]