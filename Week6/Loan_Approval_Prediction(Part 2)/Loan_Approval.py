import pandas as pd
df=pd.read_csv("loan_data.csv",sep="\t")
print(df)

#Step 2 Encode Categorical Variables
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
df["Gender"]=encoder.fit_transform(df["Gender"])
df["Married"]=encoder.fit_transform(df["Married"])
df["Education"]=encoder.fit_transform(df["Education"])
df["Loan_Status"]=encoder.fit_transform(df["Loan_Status"])

#Step 3-Features and Target
X=df.drop("Loan_Status",axis=1)
Y=df["Loan_Status"]

#Step 4-Train/Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)

#Step 5-Build Multiple Models
#import models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

#Create Models
models={
    "LogisticRegression":LogisticRegression(),
    "DecisionTree":DecisionTreeClassifier(random_state=42),
    "RandomForest":RandomForestClassifier(random_state=42),
    "KNN":KNeighborsClassifier()
    
}

#Step 6-Train and Compare Models

from sklearn.metrics import accuracy_score

for name,model in models.items():
    model.fit(X_train,Y_train)
    predictions=model.predict(X_test)
    accuracy=accuracy_score(Y_test,predictions)
    print(name)
    print("Accuracy:",accuracy)
    print("-"*30)
    
    #Step 7-Cross Validation
    
    from sklearn.model_selection import cross_val_score
    for name,model in models.items():
        scores=cross_val_score(model,
                               X,
                               Y,
                               cv=5)
        print(name)
        print("Cross Validation Accuracy:",scores.mean())
        print(scores)
        print("-"*30)
        
        #step 8-Hyperparameter Tuning
        from sklearn.model_selection import GridSearchCV
        
        params={
            "n_estimators":[50,100,200],
            "max_depth":[2,4,6,8],
        }
        
        grid=GridSearchCV(
            RandomForestClassifier(random_state=42),
            params,
            cv=5
        )
        
        grid.fit(X_train,Y_train)
        print(grid.best_params_)
        print(grid.best_score_)
        
#Step 9-Evaluate the best model
from sklearn.metrics import (confusion_matrix,classification_report,roc_auc_score)

best_model=grid.best_estimator_
Y_pred=best_model.predict(X_test)
Y_prob=best_model.predict_proba(X_test)[:,1]

print(confusion_matrix(Y_test,Y_pred))
print("ROC_AUC:",roc_auc_score(Y_test,Y_prob))

#Step 10-Save the model
import joblib
joblib.dump(best_model,"loan_model.pkl")

print("Loan model saved Successfully!")

#Step 11-Prediction Program

import joblib
model=joblib.load("Loan_model.pkl")
gender=int(input("Gender(male=1,Female=0):"))
married=int(input("Married(Yes=1,No=0"))
income=float(input("Income"))
loan_amount=float(input("Loan Amount"))
credit_history=int(input("Credit History(1=Good,0=Bad):"))
education=int(input("Education(Graduate=1,Not Graduate=0):"))

prediction=model.predict([[gender,
                           married,
                           income,
                           loan_amount,
                           credit_history,
                           education]])

if prediction[0]==1:
    print("Loan approved")
else:
    print( "Loan rejected")
    
    
        