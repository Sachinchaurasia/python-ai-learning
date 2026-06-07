##Different algorithms can produce diffrenet accuracies on the same datasets

#Importing the libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Creating the dataset
data={
    "Income":[20000,30000,50000,70000,80000,90000,100000],
    "Approved":[0,0,0,1,1,1,1]
}
df=pd.DataFrame(data)

#Features and Target
X=df[["Income"]]
Y=df["Approved"]

#Train test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42
)


#Train Logistic Regression
LR=LogisticRegression()
LR.fit(X_train,Y_train)

#Predict and evaluate Logistic Regression
LR_predictions=LR.predict(X_test)

LR_accuracy=accuracy_score(Y_test,LR_predictions)
print("Logistic Regression Accuracy:",LR_accuracy)

#Train Decision Tree
DT=DecisionTreeClassifier(random_state=42)
DT.fit(X_train,Y_train)

#Predict and evaluate Decision Tree
DT_predictions=DT.predict(X_test)

DT_accuracy=accuracy_score(Y_test,DT_predictions)
print("Decision Tree Accuracy:",DT_accuracy)

#Train RandomForest
RF=RandomForestClassifier(n_estimators=100,random_state=42)
RF.fit(X_train,Y_train)

#Predict and evaluate RandomForest
RF_predictions=RF.predict(X_test)
RF_accuracy=accuracy_score(Y_test,RF_predictions)
print("Random Forest Accuracy:",RF_accuracy)

#Compare Results
print("\nComparison of Algorithms:")
print(f"Logistic Regression: {LR_accuracy}")
print(f"Decision Tree: {DT_accuracy}")
print(f"Random Forest: {RF_accuracy}")


# Important Interview Question
# Which algorithm is best?

# Wrong answer:

# The one with the highest accuracy.

# Better answer:

# The best algorithm depends on the dataset. We compare models using metrics such as accuracy, precision, recall, F1-score, training time, and how well they generalize to unseen data.

# AI Engineer Thinking
# Logistic Regression
# Simple
# Fast
# Works well when classes are linearly separable
# Decision Tree
# Easy to understand
# Learns rule-based decisions
# Can overfit
# Random Forest
# Collection of many Decision Trees
# Usually more accurate
# Reduces overfitting
# One of the most widely used classical ML algorithms

# For many real-world tabular datasets, Random Forest often performs better than a single Decision Tree, though the actual result depends on the data.