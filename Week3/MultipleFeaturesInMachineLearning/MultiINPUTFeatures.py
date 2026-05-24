# # # #import Libraries

# # # import pandas as pd
# # # from pandas import test
# # # from sklearn.linear_model import LinearRegression
# # # from sklearn.model_selection import train_test_split

# # # #Create Dataset

# # # data={
# # #     "Experience":[1,2,3,4,5],
# # #     "Skills":[2,3,5,7,9],
# # #     "Salary":[30000,40000,50000,65000,80000]
# # # }

# # # df=pd.DataFrame(data)
# # # print(df)

# # # #Features(Multiple Columns)
# # # x=df[["Experience","Skills"]]

# # # #Target Variales
# # # y=df["Salary"]

# # # #Train/Test Split
# # # x_train,x_test,y_train,y_test=train_test_split(x,
# # #                                                y,
# # #                                                test_size=0.2,
# # #                                                random_state=42)

# # #  #train model 
# # # model=LinearRegression()
# # # model.fit(x_train,y_train)

# # #  #Make Prediction
 
# # # predictions=model.predict([[6,8]])
# # # print(predictions)

# # # #Check Accuracy

# # # Score=model.score(x_test,y_test)
# # # print(Score)


# # #Task 1--Student Marks prediction

# # import pandas as pd
# # from sklearn.linear_model import LinearRegression

# # # Create Dataset
# # data = {
# #     "Hours": [1, 2, 3, 4],
# #     "Attendance": [60, 70, 80, 90],
# #     "Marks": [20, 40, 60, 80]
# # }

# # df = pd.DataFrame(data)

# # # Print Dataset
# # print(df)

# # # Features/Input
# # X = df[["Hours", "Attendance"]]

# # # Target/Output
# # Y = df["Marks"]

# # # Create Model
# # model = LinearRegression()

# # # Train Model
# # model.fit(X, Y)

# # # Predict Marks
# # prediction = model.predict(
# #     pd.DataFrame([[5, 95]], columns=["Hours", "Attendance"])
# # )

# # print("\nPredicted Marks:", prediction[0])

# #Task 2--  House price prediction

# import pandas as pd
# from sklearn.linear_model import LinearRegression

# #create Dataset
# data={
#     "Size":[500,700,900,1200],
#     "Bedrooms":[1,2,3,4],
#     "Price":[10,15,20,30]
    
# }

# df=pd.DataFrame(data)
# print(df)

# #Features/input
# x=df[["Size","Bedrooms"]]

# #Target/output
# y=df["Price"]

# #train model
# model=LinearRegression()

# model.fit(x,y)

# #make predictions
# predictions=model.predict(
#     pd.DataFrame([[1000,3]],columns=["Size","Bedrooms"])

# )

# print("\n Predicted price:",predictions[0])

# ##output of 1000 size and 3 Bedrooms
# #    Size  Bedrooms  Price
# # 0   500         1     10
# # 1   700         2     15
# # 2   900         3     20
# # 3  1200         4     30

# #  Predicted price: 24.999999999999993


# #Task 3---AI Thinking Task

# Why are multiple features better than one feature?

# Think:

# more information
# better prediction
# real-world complexity

# Multiple features are better than one feature because real-world problems usually depend on many factors, not just one.

# More useful information helps AI models make smarter and more accurate predictions.

# 1- More Information

# A single feature gives limited understanding.

# Example:
# Predicting student marks using only:

# Hours studied

# is incomplete.

# But adding:

# attendance
# assignments
# sleep
# practice tests

# gives the model a fuller picture.

# More relevant information improves learning.

# 2- Better Prediction Accuracy

# Multiple features help the model detect more patterns and relationships.

# Example:
# House price prediction:

# Using only:

# house size

# may not be enough.

# Adding:

# location
# number of rooms
# age of house
# nearby facilities

# greatly improves prediction quality.

# 3- Real-World Problems Are Complex

# Most real-world outcomes depend on many variables.

# Examples:

# Problem	Important Features
# Salary prediction	experience, skills, education
# Health prediction	age, blood pressure, lifestyle
# Sales forecasting	season, demand, pricing

# One feature alone usually cannot capture full complexity.

# 4-Reduced Oversimplification

# Using only one feature may create unrealistic assumptions.

# Example:
# Two students study 5 hours:

# one attends classes regularly
# one misses classes

# Their marks may differ a lot.

# Multiple features help AI understand such differences.

# 5- Better Generalization

# More meaningful features help models perform better on unseen data.

# The model learns richer patterns instead of relying on one narrow relationship.

# Simple Example

# Predicting marks:

# ❌ One Feature
# Hours studied only
# ✅ Multiple Features
# Hours + Attendance + Practice + Assignments

# The second model usually predicts much more accurately.

# ✅ Final Idea

# Multiple features are better because:

# “Real-world decisions are influenced by many factors.”

# More useful features help AI models:

# understand data better
# capture complex relationships
# improve prediction quality
# make smarter real-world predictions