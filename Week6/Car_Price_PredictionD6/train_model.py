#Step 1-Create car_prices.csv

#Step 2-import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 3- Load Dataset
df=pd.read_csv("car_prices.csv")
print(df.head())
print(df.info())
print(df.describe())

#Step 4-Exploratory Data Analysis(EDA)

#Missing Values
print(df.isnull().sum())

#Duplicate Rows
print(df.duplicated().sum())
df.drop_duplicates()

#Price Distribution
plt.hist(df["Price"])
plt.title("Car distribution")
plt.show()

#Brand Distribution
sns.countplot(
    x="Brand",
    data=df
)
plt.xticks(rotation=45)
plt.show()

#Correlation(NUmeric Features)
numeric_df=df.select_dtypes(include=np.number)
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

#Step 5-Feature Engineering
#Create Car Age:
current_year=2026
df["car_Age"]=current_year - df["year"]

#Step 6-One-Hot Encoding
#Convert Categorical variables into numerical columns

df=pd.get_dummies(
    df,
    columns=["Brand","Fuel","Transmission"],
    drop_first=True
)

#Step 7-Features & Target

X=df.drop(
    ["Price","Year"],
    axis=1
)

Y=df["Price"]

#Step 8-Train/Test split

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

#Step 9- train multiple models

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

models={
    "LinearRegression":LinearRegression(),
    "DecisionTree":DecisionTreeRegressor(random_state=42),
    "RandomForest":RandomForestRegressor(random_state=42)
}

#Compare them
from sklearn.metrics import r2_score
for name, model in models.items():
    model.fit(X_train,Y_train)
    predictions=model.predict(X_test)
    print(name)
    print("R2:",r2_score(Y_test,predictions))
    print("-"*30)
    
#Step 10-EValuate the best model

from sklearn.metrics import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

best_model=RandomForestRegressor(random_state=42)
best_model.fit(X_train,Y_train)
predictions=best_model.predict(X_test)
print("MAE",mean_absolute_error(Y_test,predictions))
print("MSE",mean_squared_error(Y_test,predictions))

rmse=np.sqrt(mean_squared_error(Y_test,predictions))

print("RMSE",rmse)
print("R2:",r2_score(Y_test,predictions))

#Step 11: Save the best Model
import joblib 
joblib.dump(best_model,
            "car_price_model.pkl")

print("Car Price Model Saved!...")

#Step 12-Prediction Program

import joblib
import pandas as pd
model=joblib.load("car_price_model.pkl")
#Create a dataframe with the same column as X
#Fill in the encoded feature values

sample=pd.DataFrame([
    {
        #Add all required column features here
        prediction=model.predict(sample)
        print(f"Estimated Price:${prediction[0]:,.2f}")
        
    }
])
