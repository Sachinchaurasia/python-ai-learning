#Step 1 --Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#Step 2--create Dataset
data={
    "Income":[20000,30000,50000,70000],
    "Approval":[0,0,1,1]
}
df=pd.DataFrame(data)

#Step 3--Features and Target
X=df[["Income"]]
Y=df["Approval"]

#Step 4--Create RandomForestModel
model=RandomForestClassifier(
    n_estimators=1000,
    random_state=42
)

#step 5--Train model
model.fit(X,Y)

#Step 6--Make Prediction
predictions=model.predict([[60000]])
print(predictions)

