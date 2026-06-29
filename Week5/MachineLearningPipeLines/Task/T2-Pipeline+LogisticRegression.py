# TASK 2 — Pipeline + Logistic Regression

# Build a pipeline using:

# StandardScaler
# LogisticRegression

# Print:

# pipeline.score(
#     X_test,
#     y_test
# )
###################################################
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

#Create  Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}
df=pd.DataFrame(data)

#Features and Target
X=df[["Hours"]]
Y=df["Pass"]

#Train/Test Split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.33,
                                               random_state=42)

#Create Pipeline
pipeline=Pipeline([
    ("scaler",StandardScaler()),
    ("Logistic",LogisticRegression())
])

#Train Pipeline
pipeline.fit(X_train,Y_train)

#Predict
predictions=pipeline.predict(X_test)
print("\n actual Values")
print(Y_test.values)

print("\n predictions values")
print(predictions)

#Accuracy
print("\n pipeline acccuracy")
print(pipeline.score(X_test,Y_test))


