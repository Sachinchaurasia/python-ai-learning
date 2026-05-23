# # # # # Train /Test Split---Model Evaluation

# # # # import pandas as pd
# # # # from pandas import test
# # # # from sklearn.linear_model  import LinearRegression
# # # # from sklearn.model_selection import train_test_split

# # # # # Create dataset
# # # # data={
# # # #     "Experience":[1,2,3,4,5,6,7,8],
# # # #     "Salary":[300000,400000,500000,600000,700000,800000,900000,1000000]
    
# # # # }

# # # # df=pd.DataFrame(data)

# # # # # features and Target
# # # # x=df[["Experience"]]
# # # # y=df["Salary"]

# # # # #Split dataset

# # # # x_train,x_test,y_train,y_test=train_test_split(x,
# # # #                                                y,
# # # #                                                test_size=0.2,
# # # #                                                random_state=42)
# # # # #Train Model
# # # # model=LinearRegression()
# # # # model.fit(x_train,y_train)

# # # # #Make predictions

# # # # predictions=model.predict(x_test)
# # # # print(predictions)

# # # # #Comparison Actual Vs Predicted

# # # # comparison=pd.DataFrame({
# # # #     "Actual":y_test,
# # # #     "predicted":predictions
    
# # # # })

# # # # print(comparison)

# # # #Task 1--Student Marks Prediction

# # # import pandas as pd
# # # from pandas import test
# # # from sklearn.linear_model import LinearRegression
# # # from sklearn.model_selection import train_test_split

# # # #create Dataset
# # # data={
# # #      "Hours":[1,2,3,4,5],
# # #      "Marks":[20,40,60,80,100]
          
# # #  }

# # # df=pd.DataFrame(data)

# # # #features and Target
# # # Hours=df[["Hours"]]
# # # Marks=df["Marks"]

# # # #split dataset
# # # Hours_train,Hours_test,Marks_train,Marks_test=train_test_split(Hours,Marks,test_size=0.2,random_state=42)

# # # #Train Model
# # # model=LinearRegression()

# # # model.fit(Hours_train,Marks_train)

# # # #make predictions
# # # predictions=model.predict(Hours_test)

# # # print(predictions)

# # # #comparison between actual and predicted
# # # comparison=pd.DataFrame({
# # #     "actual":Marks_test,
# # #     "predicted":predictions
# # # })
# # # print(comparison)

# # # #calculate score of the model

# # # score=model.score(Hours_test,Marks_test)
# # # print(score)


# # # #Task 2-- Predicts House prices

# # import pandas as pd
# # from pandas import test
# # from sklearn.linear_model import LinearRegression
# # from sklearn.model_selection import train_test_split

# # #create data set
# # data={
# #     "Size":[500,700,900,1100],
# #     "Price":[10,15,20,25]
    
# # }

# # df=pd.DataFrame(data)

# # #features and Target

# # X=df[["Size"]]
# # Y=df["Price"]

# # #Train_test_Split

# # X_train,X_test,Y_train,Y_test=train_test_split(X,
# #                                               Y,
# #                                               test_size=0.2,
# #                                               random_state=42)

# # #Train model
# # model=LinearRegression()
# # model.fit(X_train,Y_train)

# # #make predictions

# # predictions=model.predict(X_test)
# # print(predictions)

# # #Comparison
# # comparison=pd.DataFrame({
# #     "Actual":Y_test,
# #     "Predicted":predictions
# # })

# # print(comparison)

# # # calculate Score

# # score=model.score(X_test,Y_test)
# # print(score)

# # #task-3 AI Thinking

#  TASK 3 — AI THINKING TASK

# Why should we NOT test on training data?

# Think:

# memorization
# cheating
# real-world prediction

# We should NOT test on training data because the model has already seen that data during learning.

# Testing on the same data gives a false impression of performance.

# 1- Memorization Instead of Learning

# A model may simply memorize the training data instead of understanding real patterns.

# Example:

# It remembers exact answers
# But fails on new unseen data

# This is called:

#  Overfitting
# 2- It Becomes Like Cheating

# Testing on training data is similar to:

# practicing exam questions and then taking the exact same exam.

# The score may look very high, but it does not prove true understanding.

# The model already knows the answers.

# 3- Real-World Data Is New

# In real life, AI models face unseen data.

# Examples:

# new customers
# new emails
# new images
# new market conditions

# The goal is not:

# remember old data

# The goal is:

# predict correctly on new data

# That’s why testing must happen on unseen examples.

# 4- Detect True Model Quality

# Separate test data helps measure:

# generalization
# real prediction ability
# robustness

# If performance is good on unseen data,
# the model has actually learned useful patterns.

# 5- Prevent False Confidence

# A model can score:

# 100%

# on training data but perform badly in production.

# Without proper testing:

# engineers may trust a weak model
# businesses may make wrong decisions
# AI systems may fail in real-world use