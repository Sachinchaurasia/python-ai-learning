#Step 1-Create  dataset heart.csv

#Step 2-Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 3- Load Dataset
df=pd.read_csv("heart.csv",sep="\t")
print(df)

print(df.head())
print(df.info())
print(df.describe())

#Step 4- EDA(Exploratory Data Analysis)
#Missing Values
print(df.duplicated().sum())
df=df.drop_duplicates()

#Target Distribution
sns.countplot(
    x="Disease",
    data=df
)
plt.title("Heart Disease Distribution")
#plt.show()

#Age Distribution
plt.hist(df["Age"])
plt.title("Age Distribution")
#plt.show()

#Cholesterol Distribution
plt.hist(df["Cholesterol"])
plt.title("Cholesterol Distribution")
#plt.show()

#Blood Pressure Vs Disease
sns.boxplot(
    x="Disease",
    y="BP",
    data=df
)
#plt.show()

#Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.show()

#Step 5-Features & Target
X=df.drop("Disease",axis=1)
Y=df["Disease"]

#Step 6-Train/Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
    
)

#Step 7-Train Multiple Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

models={
    "LogisticRegression":LogisticRegression(max_iter=1000),
    "Decision Tree":DecisionTreeClassifier(random_state=42),
    "Random Forest":RandomForestClassifier(random_state=42),
    "KNN":KNeighborsClassifier()
}

#Step 8-Compare models
from sklearn.metrics import accuracy_score
for name,model in models.items():
    
    model.fit(X_train,Y_train)
    predictions=model.predict(X_test)
    print(name)
    
    print("ACcuracy:",
          accuracy_score(Y_test,predictions))
    
    print("-"*30)
    
    #Step 9- Professional Evaluation
    from sklearn.metrics import (
                                confusion_matrix,
                                classification_report,
                                roc_auc_score
                                
    )
    
    best_model=RandomForestClassifier(random_state=42)
    best_model.fit(X_train,Y_train)
    
    Y_pred=best_model.predict(X_test)
    Y_prob=best_model.predict_proba(X_test)[:,1]
    
    print(confusion_matrix(Y_test,Y_pred))
    print(classification_report(Y_test,Y_pred))
    
    print("ROC-AUC",
          roc_auc_score(Y_test,Y_prob))
    
    #Step 10- Feature Importance
    importance=pd.DataFrame({
        "Feature":X.columns,
        "Importance":best_model.feature_importances_
    
    })
    
    importance=importance.sort_values(
        by="Importance",
        ascending=False
    )
    
    print(importance)
    #think about 1-which feature contributes the most?
    #2-Does that nake medical sense?
    
    #STep 11- Save the model
    import joblib
    joblib.dump(
        best_model,
        "heart_model.pkl"
    )
    print("Heart Disease Model Saved!...")
    
    #Step 12-Prediction Program
    
    import joblib
    model=joblib.load("heart_model.pkl")
    age=int(input("Age:"))
    sex=int(input("Sex(1=Male,0=Female):"))
    bp=float(input("Blood Pressure:"))
    chol=float(input("Cholesterol:"))
    max_hr=float(input("Max Heart Rate"))
    chest_pain=int(input("Chestpain(1=yes,0=No):"))
    
    prediction=model.predict([[
        age,
        sex,
        bp,
        chol,
        max_hr,
        chest_pain
    ]])
    
    if prediction[0]==1:
        print("Heart Disease Predicted")
    else:
        print("No Heart Disease")
        
        
        
# AI Thinking Task

# Question: Why is Accuracy alone not enough when building a medical diagnosis model?

# Answer:

# Accuracy alone is not enough because a model can have high accuracy but still miss patients who actually have the disease. These missed cases are called False Negatives, and they can delay treatment and put patients' lives at risk. False Positives are also important because they may cause unnecessary tests, stress, and medical costs. In medical diagnosis, Recall is often prioritized to detect as many actual patients as possible, while Precision helps reduce incorrect positive diagnoses. Therefore, evaluating both Precision and Recall provides a safer and more reliable assessment than accuracy alone.