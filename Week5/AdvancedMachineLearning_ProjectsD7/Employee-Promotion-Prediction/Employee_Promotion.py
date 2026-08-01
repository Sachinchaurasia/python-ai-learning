#Step 1 create CSV File

#Step 2: Importing Libraries
import pandas as pd
df=pd.read_csv("employee-promotion.csv")
print(df.head())

#Step 3: Feature Engineering
#Create A new Feature

df["Experience_Skills"]=df["Experience"]*df["Skills"]   

#Step 4 Features & Target
X=df[
    ["Experience",
     "Skills",
     "Education",
     "Performance",
     "Training",
     "Experience_Skills"]
]

Y=df["Promotion"]

#Step 5: Train /Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Step 6:Create Pipeline

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(random_state=42))
])

#Step 7:Hyperparameter Tuning

from sklearn.model_selection import GridSearchCV

params={
    
    "model__n_estimators":[50,100,200],
    "model__max_depth":[2,4,6,8]    

}

grid=GridSearchCV(
    pipeline,
    params,
    cv=5
)
grid.fit(X_train,Y_train)

#Step 8 Best model
print(grid.best_params_)
print(grid.best_score_)

#Step 9: Cross Validation 

from sklearn.model_selection import cross_val_score
scores=cross_val_score(grid.best_estimator_,
                          X,
                          Y,
                          cv=5)

print(scores)
print(scores.mean())

#Step 10:Predictions

best_model=grid.best_estimator_
predictions=best_model.predict(X_test)
Y_prob=best_model.predict_proba(X_test)[:,1]

#Step 11:Model Evaluation
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,classification_report,confusion_matrix,roc_auc_score)

print("Accuracy:", accuracy_score(Y_test, predictions))
print("Precision:", precision_score(Y_test, predictions))
print("Recall:", recall_score(Y_test, predictions))
print("F1-Score:", f1_score(Y_test, predictions))
print("Classification Report:")
print(classification_report(Y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(Y_test, predictions))
print("ROC AUC Score:", roc_auc_score(Y_test, Y_prob))

#Step 12:Save the model
import joblib
joblib.dump(best_model,"promotion_model.pkl")
print("Model saved as promotion_model.pkl Successfully!")

#Step 13:Prediction Script

import joblib   
model=joblib.load("promotion_model.pkl")
experience=float(input("Enter Experience: "))
skills=float(input("Enter Skills: "))
education=float(input("Enter Education: "))
performance=float(input("Enter Performance: "))
training=float(input("Enter Training: "))
experience_skills=experience*skills

prediction=model.predict([[experience,skills,education,performance,training,experience_skills]])

print("Promotion Prediction:",prediction[0])

