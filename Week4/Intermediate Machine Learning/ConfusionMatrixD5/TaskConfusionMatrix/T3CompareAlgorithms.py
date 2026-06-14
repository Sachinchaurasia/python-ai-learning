#  TASK 3 — Compare Algorithms (Accuracy + Confusion Matrix)

# This task compares four popular classification algorithms:

# Logistic Regression
# Decision Tree
# Random Forest
# KNN
# Complete Code
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Dataset
data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Promotion": [0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Promotion"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

results = []

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

lr_acc = accuracy_score(y_test, lr_pred)
lr_cm = confusion_matrix(y_test, lr_pred)

results.append(["Logistic Regression", lr_acc])

# Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

dt_acc = accuracy_score(y_test, dt_pred)
dt_cm = confusion_matrix(y_test, dt_pred)

results.append(["Decision Tree", dt_acc])

# Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_acc = accuracy_score(y_test, rf_pred)
rf_cm = confusion_matrix(y_test, rf_pred)

results.append(["Random Forest", rf_acc])

# KNN
knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

knn_acc = accuracy_score(y_test, knn_pred)
knn_cm = confusion_matrix(y_test, knn_pred)

results.append(["KNN", knn_acc])

# Results Table
print("\nAlgorithm Comparison")
print("-" * 40)

print("Algorithm\t\t\tAccuracy")

for algo, acc in results:
    print(f"{algo:<25} {acc:.2f}")

# Confusion Matrices
print("\nLogistic Regression CM:")
print(lr_cm)

print("\nDecision Tree CM:")
print(dt_cm)

print("\nRandom Forest CM:")
print(rf_cm)

print("\nKNN CM:")
print(knn_cm)
# Example Output
# Algorithm Comparison
# ----------------------------------------

# Algorithm                   Accuracy

# Logistic Regression         1.00
# Decision Tree               1.00
# Random Forest               1.00
# KNN                         1.00
# Logistic Regression CM
# [[1 0]
#  [0 2]]
# Decision Tree CM
# [[1 0]
#  [0 2]]
# Random Forest CM
# [[1 0]
#  [0 2]]
# KNN CM
# [[1 0]
#  [0 2]]
# Better Table Using Pandas
result_df = pd.DataFrame(
    results,
    columns=["Algorithm", "Accuracy"]
)

print(result_df)

# Output:

# Algorithm	Accuracy
# Logistic Regression	1.00
# Decision Tree	1.00
# Random Forest	1.00
# KNN	1.00
# AI Engineer Thinking
# Logistic Regression
# Fast
# Simple
# Good for linear decision boundaries
# Decision Tree
# Easy to explain
# Rule-based
# Can overfit
# Random Forest
# Multiple trees
# Voting mechanism
# Reduces overfitting
# KNN
# Uses nearest neighbors
# No real training phase
# Can become slow on large datasets
# Interview Answer

# Accuracy tells us how many predictions are correct, while the confusion matrix shows the types of errors made by the model. Comparing multiple algorithms helps identify which model generalizes best for the given dataset rather than relying on a single technique.