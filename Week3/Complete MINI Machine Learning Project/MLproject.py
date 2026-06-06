import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = {
    "Experience": [1, 2, 3, 4, 5],
    "Skills": [2, 3, 5, 7, 9],
    "Salary": [30000, 40000, 50000, 65000, 80000]
}

df = pd.DataFrame(data)

# Create CSV file
df.to_csv("employee.csv", index=False)

print("CSV file created successfully")
print(df.head())


print(df.columns)


#Features and target
X=df[["Experience","Skills"]]
Y=df["Salary"]

#Train test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                                   random_state=42
)

#Train Model
model=LinearRegression()
model.fit(X_train,Y_train)

#Evaluate Model
score=model.score(X_test,Y_test)
print("R^2 score:",score)

#Make Prediction
prediction=model.predict([[7,12]])
print("predicted salary:",prediction[0])

#Compare Actual Vs Predicted
predictions=model.predict(X_test)

comparison=pd.DataFrame({
    "Actual":Y_test,
    "predicted":predictions
})
print(comparison)

#Visualization
import matplotlib.pyplot as plt
plt.scatter(df["Experience"],df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")       
plt.show()

#Save Model
import pickle
with open("Salary_model.pkl","wb") as file:
    pickle.dump(model,file)
print("Model saved successfully")

#Load Model
with open("Salary_model.pkl.load","rb") as file:
    loaded_model=pickle.load(file)
    #Predict using loaded model 
    result=loaded_model.predict([[8,14]])
print("Predicted salary using loaded model:",result[0])

#Project Enhancement Tasks
#task 1: Add new Feature -Education_Level
df["Education_Level"]=[1,1,2,3,3,3] 
X=df[["Experience","Skills","Education_Level"]]
Y=df["Salary"]

