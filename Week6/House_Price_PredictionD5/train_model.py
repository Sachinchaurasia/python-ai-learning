#Step 1-Create house_prices.csv
#Step 2-import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 3- Load Dataset
df=pd.read_csv("house_prices.csv", sep ="\t")
print(df)

#Step 4-Exploratory Data Analysis
#Missing Values
print(df.isnull().sum())

#Duplicate Rows
print(df.duplicated().sum())
df=df.drop_duplicates()

#Price Distribution

# plt.hist(df["Price"])
# plt.title("House Price Distribution")
# plt.show()

#Area Vs Price
# plt.scatter(df["Area"],df["Price"])
# plt.xlabel("Area")
# plt.ylabel("Price")
# plt.show()

#Correlation Heatmap
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.show()

#Step 5-Feature Engineering
#Create two new Feature

#Price per Square foot
df["Price_Per_SqFt"]=df["Price"]/df["Area"]

#Total Rooms
df["Total_ROoms"]=(
    df["Bedrooms"]+df["Area"]
    
)

#For training ,do not include Price_per_sqFt in the featureset because it is calculated using the target (Price) and would leak information

#Step 6-Features and Target

X=df[
    [
        "Area",
        "Bedrooms",
        "Age",
        "Parking",
        "Total_ROoms",
        
    ]
]

Y=df["Price"]

#Step 7-Train/Test Split

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

#Step 8-Train Multiple Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

models={
    "Linear Regression":LinearRegression(),
    "DecisionTree":DecisionTreeRegressor(random_state=42),
    "RandomForest":RandomForestRegressor(random_state=42)
}

#Step 9- Compare models
from sklearn.metrics import r2_score
for name,model in models.items():
    model.fit(X_train,Y_train)
    
    predictions=model.predict(X_test)
    print(name)
    
    print(
        "R2 score:",
        r2_score(Y_test,predictions)
    )
    
    print("-"*30)
    
    #Step 10- Evaluate the Best Model
    
    from sklearn.metrics import (mean_absolute_error,
                                 mean_squared_error,
                                 r2_score)
    best_model=RandomForestRegressor(random_state=42)
    best_model.fit(X_train,Y_train)
    predictions=best_model.predict(X_test)
    
    print("MAE",mean_absolute_error(Y_test,predictions))
    
    print("MSE",mean_squared_error(Y_test,predictions))
    
    rmse=np.sqrt(mean_squared_error(Y_test,predictions))
    
    print("RMSE",rmse)
    
    print("R2",r2_score(Y_test,predictions))
    
    #Step 11- Save the best model
    import joblib
    joblib.dump(
        best_model,
        "house_price_model.pkl"
    )
    
print("House Price model saved successfully!..")

#Step 12- Prediction Program

import joblib
model=joblib.load("house_price_model.pkl")
area=float(input("Area(Sq.Ft.)"))
bedrooms=int(input("Bedrooms"))
bathrooms=int(input("Bathrooms:"))
age=int(input("House age"))
parking=int(input("Parking Spaces"))

total_rooms=bedrooms+bathrooms
predictions=model.predict([[
    area,bedrooms,bathrooms,age,parking,total_rooms
]])

print(f"Estimated House Price: {predictions[0]:,.2f}")






# Price_Per_SqFt should not be used as an input feature because it directly depends on the target variable (Price).

# Since:

# Price_Per_SqFt = Price ÷ Area

# it already contains information about the value we are trying to predict. This causes target leakage, where the model gets access to the answer during training and appears unrealistically accurate. In real-world prediction, the actual Price is unknown, so Price_Per_SqFt cannot be calculated beforehand. To build a fair and reliable model, only features that are available before making the prediction should be used.
