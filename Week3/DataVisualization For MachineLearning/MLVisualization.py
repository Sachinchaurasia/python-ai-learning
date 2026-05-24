# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # from sklearn.linear_model import LinearRegression

# # # Create Dataset
# # data={
# #     "Experience":[1,2,3,4,5],
# #     "Salary":[30000,40000,50000,60000,70000]
# # }
# # df=pd.DataFrame(data)

# # # Features and Target
# # X=df[["Experience"]]
# # Y=df["Salary"]

# # #Train Model

# # model=LinearRegression()
# # model.fit(X,Y)

# # # Predict Values
# # predictions=model.predict(X)

# # #Scatter Plot
# # # plt.scatter(df["Experience"],df["Salary"])
# # # plt.xlabel("Experince")
# # # plt.ylabel("Salary")
# # # plt.title("Experience Vs Salary")
# # # plt.show()

# # # Regression Line

# # # plt.scatter(df["Experience"],df["Salary"])
# # # plt.plot(df["Experience"],predictions)

# # # plt.xlabel("Experience")
# # # plt.ylabel("salary")

# # # plt.title("ML Regression")
# # # plt.show()

# # #Actual Vs Predicted Comparison
# # comparison=pd.DataFrame({
# #     "Actual":Y,
# #     "predicted":predictions
# # })
# # print(predictions)
# # print(comparison)
# # #    Actual  predicted
# # # 0   30000    30000.0
# # # 1   40000    40000.0
# # # 2   50000    50000.0
# # # 3   60000    60000.0
# # # 4   70000    70000.0


# # #Residual Errors:  Actual-Predicted
# # comparison["Erors"]=comparison["Actual"]-comparison["predicted"]
# # print(comparison)

# # #    Actual  predicted  Erors
# # # 0   30000    30000.0    0.0
# # # 1   40000    40000.0    0.0
# # # 2   50000    50000.0    0.0
# # # 3   60000    60000.0    0.0
# # # 4   70000    70000.0    0.0

# #Task 1-- Student Marks Visulaization

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression

# #Create Dataset
# data={
#     "Hours":[1,2,3,4],
#     "Marks":[20,40,60,80]
# }

# df=pd.DataFrame(data)
# print(df)

# #Features (input)

# X=df[["Hours"]]


# #Target(output)

# Y=df["Marks"]


# #Train Model
# model=LinearRegression()
# model.fit(X,Y)

# #Make predictions
# predictions=model.predict(X)
# print(predictions)

# #Plot scatter graph
# # plt.scatter(df["Hours"],df["Marks"])
# # plt.xlabel("Hours")
# # plt.ylabel("Marks")
# # plt.title("Student Marks Visualization")
# # plt.show()

# #Regression line
# plt.scatter(df["Hours"],df["Marks"])
# plt.plot(df["Marks"],predictions)
# plt.xlabel("Hours")
# plt.ylabel("Marks")
# plt.title("Student Marks Visulaization")

# plt.show()

#Task 2-- House Price Visulaization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#Create Dataset

data={
    "Size":[500,700,900],
    "Price":[10,15,20]
}
df=pd.DataFrame(data)
#Features(Input)
X=df[["Size"]]

#Target(output)
Y=df["Price"]

#Train Model
model=LinearRegression()
model.fit(X,Y)

#Make Predictions
predictions=model.predict(X)

print(predictions)

#Scatter plot--Actual points

# plt.scatter(df["Size"],df["Price"])
# plt.xlabel("Size")
# plt.ylabel("Price")
# plt.title("House Price Prediction")
# plt.show()

#Regression line

# plt.scatter(df["Size"],df["Price"])
# plt.plot(df["Size"],predictions)
# plt.xlabel("Size")
# plt.ylabel("Price")
# plt.title("House Price Visulaization")
# plt.show()


# # What This Visualization Shows
# #Scatter Plot
# #plt.scatter()

# #Shows:

## actual house data points
## Regression Line
## plt.plot()

# Shows:

## ML model prediction trend
## AI Understanding

## The regression line represents the relationship learned by the model:

## Where:

## x = house size
## y = predicted price
##  Why Visualization Matters

## This helps AI engineers:

## see patterns
## understand trends
## detect outliers
## verify whether the model fits data correctly

## Visualization is one of the most important parts of machine learning workflows

# #Task 3--Error analysis
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# #create Data

# data={
#     "Size":[500,700,900],
#     "Price":[10,15,20]
# }
# df=pd.DataFrame(data)

# #Features and Target
# X=df[["Size"]]
# Y=df["Price"]

# # create and Train Model

# model=LinearRegression()
# model.fit(X,Y)

# #Make predictions
# predictions=model.predict(X)

# #Error Calculations
# error=Y-predictions

# #create result table
# result=pd.DataFrame({
#     "Actual":Y,
#     "Predicted":predictions,
#     "Error":error
# })

# print(result)

#Task 4--AI Thinking Task 
#Why is Visulaization useful for ML Engineers
#Think of:
#1-Debugging
#2-Understanding  patterns
#3-Identifying bad patterns

#_____ANSWERS_______

# Visualization is extremely useful for ML engineers because it helps them see what is happening inside the data and model instead of blindly trusting numbers.

# Machine learning becomes much easier to understand when data is visualized.

# 1- Debugging Models

# Visualization helps engineers quickly detect problems.

# Examples:

# wrong predictions
# missing values
# incorrect labels
# strange distributions
# feature mistakes

# A graph often exposes issues faster than reading raw tables.

# 2-Understanding Patterns

# ML models learn patterns from data.

# Visualization helps engineers identify:

# trends
# relationships
# clusters
# correlations

# Example:
# Study Hours vs Marks:

# Study Hours vs Marks

# Relationship between study hours and student marks.

# 0
# 50
# 100
# 150
# 1
# 2
# 3
# 4
# 5

# The engineer immediately sees:

# more hours → higher marks
# 3-Identifying Bad Predictions

# Visualization makes prediction errors easier to spot.

# Example:

# actual value = 80
# predicted value = 30

# A chart quickly reveals where the model is failing.

# This helps improve:

# accuracy
# feature selection
# training quality
# 4-Detecting Outliers

# Outliers are abnormal values.

# Example:
# Most salaries:

# 30000–70000

# One salary:

# 5000000

# Visualization instantly highlights unusual points that may damage model training.

# 5-Understanding Model Performance

# Charts help compare:

# actual vs predicted values
# training vs testing accuracy
# error distribution

# This helps engineers decide whether the model is:

# good
# overfitting
# underfitting
#  Error Analysis Visualization
# Actual vs Predicted Values

# Comparison of real values and model predictions to analyze prediction quality.

# Actual
# Predicted
# 0
# 20
# 40
# 60
# 80
# S1
# S2
# S3
# S4

# This helps engineers visually identify:

# accurate predictions
# weak predictions
# prediction gaps

#  Final Idea

# Visualization is useful because:

# “Humans understand patterns visually much faster than through raw numbers.”

# ML engineers use visualization to:

# debug models
# understand data
# detect errors
# improve predictions
# build reliable AI systems