#Step--1--Import Libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score,
                             confusion_matrix,
                             precision_score,
                             recall_score,
                             f1_score
                             )

# Step --2--Load Dataset
df=pd.read_csv("employee_promotion.csv")
print(df.head())
print(df)

#Step 3--Features and Target
X=df[["Experience","Skills","Performance"]]
Y=df["Promotion"]

#Features and Target
X=df[["Experience","Skills","Performance"]]
Y=df["Promotion"]

#Train /Test Split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)
#Step 6 Feature Scaling
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

#Step 7--Create Models
models={
    "LogisticRegression":LogisticRegression(),
    "Decision Tree":DecisionTreeClassifier(random_state=42),
    "Random Forest":RandomForestClassifier(random_state=42),
    "KNN":KNeighborsClassifier(n_neighbors=3)
    
}

#Step 8-- Train & Evaluate All Models
results = []

for name, model in models.items():

    if name == "KNN":

        model.fit(
            X_train_scaled,
            Y_train
        )

        Y_pred = model.predict(
            X_test_scaled
        )

    else:

        model.fit(
            X_train,
            Y_train
        )

        Y_pred = model.predict(
            X_test
        )

    # Calculate Metrics
    accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    precision = precision_score(
        Y_test,
        Y_pred
    )

    recall = recall_score(
        Y_test,
        Y_pred
    )

    f1 = f1_score(
        Y_test,
        Y_pred
    )

    # Store Results
    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    # Print Metrics
    print("\n", name)

    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    print("Confusion Matrix:")
    print(
        confusion_matrix(
            Y_test,
            Y_pred
        )
    )
results_df = pd.DataFrame(
    results,
    columns=[
        "Algorithm",
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ]
)

print(results_df)
    #Step 10-- Find Best Model
best_model=results_df.sort_values(by="F1",ascending=False)
print("Best_Model",best_model.head(1))
    