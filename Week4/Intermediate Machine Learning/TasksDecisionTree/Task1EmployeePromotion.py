import pandas as pd
data={
    "Experience":[1,2,4,6,8],
    "Promotion":[0,0,1,1,1]
     
 }

df=pd.DataFrame(data)
print(df)

#Train Decision Tree
from sklearn.tree import DecisionTreeClassifier

#Features and Target
X=df[["Experience"]]
Y=df["Promotion"]

# Create model
model=DecisionTreeClassifier(random_state=42)
# Train model
model.fit(X,Y)

#Make Prediction for Experience having 5 years
prediction=model.predict([[5]])

if prediction[0]==1:
    print("Promotion Likely")
else:
    print("No Promotion")
    


