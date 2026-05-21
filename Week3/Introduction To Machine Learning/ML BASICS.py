# # import pandas as pd 
# # from sklearn.linear_model import LinearRegression

# # # Create DataFrame

# # data={
# #     "Experience":[1,2,3,4,5],
# #     "Salary":[30000,40000,50000,60000,70000]
    
# # }

# # df=pd.DataFrame(data)

# # #Features and Target Variable

# # #Features/input
# # X=df[["Experience"]]

# # #Target Variable/output
# # Y=df[["Salary"]]

# # #Create Linear Regression Model
# # model=LinearRegression()

# # #Fit the model to the data/Train the model
# # model.fit(X,Y)

# # #Make Prediction
# # #Predict salary for 6 years experience

# # prediction =model.predict([[6]])

# # print(prediction)



# import pandas as pd 
# from sklearn.linear_model import LinearRegression

# # create dataFrame
# data={
#     "Hours":[1,2,3,4],
#     "marks":[20,40,60,80]
# }

# df=pd.DataFrame(data)

# #features and Target variables
# x=df[["Hours"]]
# y=df["marks"]

# #create linear regression model
# model=LinearRegression()

# #fit the model to the data/Train the model
# model.fit(x,y)

# #marks prediction for 5 hours 

# prediction=model.predict([[5]])
# print(prediction)

# Task 2 House price prediction

import pandas as pd
from sklearn.linear_model import LinearRegression

#create dataFrame
data={
    "size":[500,700,900],
    "price":[10,15,20]
    
}

df=pd.DataFrame(data)

#features and target variables
x=df[["size"]]
y=df["price"]

#create linearRegression model
model=LinearRegression()

#fir or train the model

model.fit(x,y)

# predict the price of house with size 1000

prediction=model.predict([[1000]])

print(prediction)

