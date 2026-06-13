#complete code
#Step 1: Import Libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

#Step 2: Create Dataset
data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Salary": [20000,25000,30000,35000,40000,
               45000,50000,55000,60000,65000],
    "Promotion": [0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

#Step 3: Features and Target
X = df[["Experience", "Salary"]]
y = df["Promotion"]

#Step 4: Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#KNN WITHOUT SCALING
knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

pred1 = knn.predict(X_test)

acc1 = accuracy_score(y_test, pred1)

print("Accuracy Without Scaling:", acc1)

#KNN WITH SCALING
#Scale Data
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

#Train KNN
knn_scaled = KNeighborsClassifier(n_neighbors=3)

knn_scaled.fit(X_train_scaled, y_train)

pred2 = knn_scaled.predict(X_test_scaled)

acc2 = accuracy_score(y_test, pred2)

print("Accuracy With Scaling:", acc2)

#Compare Results
print("\nComparison")

print("Without Scaling :", acc1)
print("With Scaling    :", acc2)