#Step 1-Create Salary_data.csv

#Step 2-Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 3-Load the dataset
df=pd.read_csv("Salary_data.csv",sep="\t")

print(df.head())
print(df.info())
print(df.describe())

#Step 4-Exploratory Data Analysis
#check for missing values
print(df.isnull().sum())

#check duplicate rows
print(df.duplicated().sum())

#Remove duplicates if any

df=df.drop_duplicates()

#Step 5-Visualizations
#Salary Distribution
plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.show()

#Experience vs Salary
plt.scatter(
    df["Experience"],
    df["Salary"]
)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()

#Skills vs Salary
plt.scatter(
    df["Skills"],
    df["Salary"]
)
plt.xlabel("Skills")
plt.ylabel("Salary")
plt.title("Skills vs Salary")
plt.show()

#Correlation map
sns.heatmap(df.corr(),
            annot=True,
            cmap="coolwarm")
plt.show()

#Step 6-Feature Engineering
#Create A new Feature
df["Experience_Skills"]=(df["Experience"]*df["Skills"])


#Step 7- Features and Target
X=df.drop("Salary",axis=1)
Y=df["Salary"]

#Step 8-Train/Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42)

#Step 9-Train multiple Regression Models
#Import Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

#Create Models
models={
    "LinearRegression":LinearRegression(),
    "DecisionTree":DecisionTreeRegressor(random_state=42),
    "RandomForest":RandomForestRegressor(random_state=42)
}

#Step 10-Compare Models
from sklearn.metrics import r2_score
for name,model in models.items():
    model.fit(X_train,Y_train)
    predictions=model.predict(X_test)
    print(name)
    print("R2 Score:",r2_score(Y_test,predictions))
    print("-"*30)
    
#Step 11-Evaluate Regression Models
from sklearn.metrics import (mean_absolute_error,
                             mean_squared_error,
                             r2_score)
best_model=LinearRegression()
best_model.fit(X_train,Y_train)
predictions=best_model.predict(X_test)

print("MAE:",
      mean_absolute_error(Y_test,predictions))

print("MSE:",
      mean_squared_error(Y_test,predictions))

rmse=np.sqrt(mean_squared_error(Y_test,predictions))

print("RMSE:",rmse)

print("R2 Score:",
      r2_score(Y_test,predictions)) 


#Save the best model
import joblib
joblib.dump(best_model,"salary_model.pkl")
print("Model saved successfully as salary_model.pkl"
      )

#Step 13- Prediction Program

import joblib
model=joblib.load("salary_model.pkl")
experience=float(input("Experience:"))
skills=float(input("Skills:"))
education=int(input("Education:"))
certifications=int(input("Certifications:"))
age=int(input("Age:"))
experience_skills=experience*skills

prediction=model.predict([[experience,skills,education,certifications,age,experience_skills]])
print("Predicted Salary:", prediction[0])



# AI Thinking Task

# Question: Why is R² Score generally more informative than accuracy for regression problems?

# Answer:

# R² Score is more informative for regression because regression predicts continuous values rather than categories. Accuracy only checks whether a prediction is exactly correct, which is not suitable for continuous outputs like salary or house price. R² measures how much of the variation in the target variable is explained by the model, giving a better understanding of its performance. It also reflects how close the predictions are to the actual values by considering prediction errors. Therefore, R² provides a more meaningful evaluation of regression models than accuracy.