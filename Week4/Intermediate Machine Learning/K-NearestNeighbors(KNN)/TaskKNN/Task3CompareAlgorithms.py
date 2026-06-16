# Train:

# Logistic Regression
# Decision Tree
# Random Forest
# KNN

# Compare accuracy scores.

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "Income": [20000,30000,40000,50000,60000,70000,80000,90000],
    "Approved": [0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Income"]]
y = df["Approved"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)

# Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_acc = accuracy_score(y_test, dt_pred)

# Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
knn_acc = accuracy_score(y_test, knn_pred)

# Result Table
print("\nAlgorithm\t\t\tAccuracy")
print("-" * 40)
print(f"Logistic Regression\t\t{lr_acc:.2f}")
print(f"Decision Tree\t\t\t{dt_acc:.2f}")
print(f"Random Forest\t\t\t{rf_acc:.2f}")
print(f"KNN\t\t\t\t{knn_acc:.2f}")