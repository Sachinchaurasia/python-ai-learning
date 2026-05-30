# # # import pandas as pd
# # # import pickle
# # # from sklearn.linear_model import LinearRegression

# # # #Create Dataset

# # # data={
# # #     "Experience":[1,2,3,4,5],
# # #     "Salary":[30000,40000,50000,60000,70000]
    
# # # }

# # # df=pd.DataFrame(data)

# # # #Features and Target
# # # X=df[["Experience"]]
# # # Y=df["Salary"]

# # # #Train Model
# # # model=LinearRegression()
# # # model.fit(X,Y)

# # # #Save Model

# # # with open("Salary_model.pkl","wb") as file:
# # #     pickle.dump(model,file)
    
# # #     #.pkl file stores 1-learned AI Patterns 2-trained model weights 3-prediction Logic
    
# # # #Load saved model

# # # with open("Salary_model.pkl", "rb") as file:
# # #     loaded_model=pickle.load(file)
    
# # # #Make prediction using loaded model

# # # prediction=loaded_model.predict([[6]])
# # # print(prediction)

# # # #Another Method Joblib
# # # #Alternative library
# # # import joblib

# # # #Save
# # # joblib.dump(model,"Salary_model.joblib")

# # # #Load
# # # loaded_model=joblib.load("Salary_model.joblib")
# # #Task 1-- Student Marks Model

# # import pandas as pd
# # import pickle
# # from sklearn.linear_model import LinearRegression
# # #Dataset

# # data={
# #     "Hours":[1,2,3,4],
# #     "Marks":[20,40,60,80]
    
# # }

# # df=pd.DataFrame(data)

# # #Features and Target
# # X=df[["Hours"]]
# # Y=df["Marks"]

# # #Train model
# # model=LinearRegression()
# # model.fit(X,Y)

# # #Save Model
# # with open("Marks_model.pkl","wb") as file:
# #     pickle.dump(model,file)

# # #Load Saved model
# # with open("Marks_model.pkl","rb") as file:
# #     loaded_model=pickle.load(file)
    
# # #Make Prediction

# # prediction=loaded_model.predict([[5]])
# # print(prediction)

# #Task 2--House Price Model
# import pandas as pd
# import pickle
# from sklearn.linear_model import LinearRegression
# import joblib


# #Create Dataset
# data={
#     "Size":[500,700,900],
#     "Price":[10,15,20]
# }
# df=pd.DataFrame(data)

# #Features and Target
# X=df[["Size"]]
# Y=df["Price"]

# #Train model
# model=LinearRegression()
# model.fit(X,Y)

# #Save model
# joblib.dump(model,"house_price_model.pkl")
# print("Model saved successfully")
    
# #reload saved model
# loaded_model=joblib.load("house_price_model.pkl")
# print("model loaded successfully")

# #Prediction using loaded model
# prediction=loaded_model.predict(pd.DataFrame([[1000]],columns=["Size"]))
# print(prediction)

#Task 3-- Classification Model Saving
#Use Logistic Regression
#train passs/fail model
#Save it
#reload it
#predict result

# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# import joblib

# #Create Dataset
# data={
#     "Hours":[1,2,3,4],
#     "Pass":[0,0,1,1]
# }

# df=pd.DataFrame(data)

# #Features and Target
# X=df[["Hours"]]
# Y=df["Pass"]

# #Create Model
# model=LogisticRegression()

# #Train model
# model.fit(X,Y)

# #save model
# joblib.dump(model,"Pass_Fail_model.pkl")
# print("Model saved successfully")

# #Reload Model
# loaded_model=joblib.load("Pass_Fail_model.pkl")
# print("model reloaded successfully")

# #Make prediction
# prediction=loaded_model.predict(
#     pd.DataFrame([[5]],columns=["Hours"])
# )

# print("prediction:",prediction[0])

# if prediction[0]==1:
#     print("PASS")
# else:
#     print("FAIL")
    
    
# TASK 4 — AI THINKING TASK

# Why is model saving important in real applications?

# Think:

# speed
# deployment
# scalability
# APIs                                                                                                                                                                                                                                                                                     

# Model saving is very important because real AI applications cannot afford to train models every time a prediction is needed.

# A saved model can be loaded instantly and used for predictions.

# 1- Speed

# Training can be expensive.

# Examples:

# A small model may take seconds.
# A large AI model may take hours or days.

# Without model saving:

# Request → Train Model → Predict

# With model saving:

# Request → Load Model → Predict

# This makes applications much faster.

# 2- Deployment

# When an AI model is moved to a production server, the server usually receives a pre-trained model file.

# Example:

# house_price_model.pkl
# pass_fail_model.pkl

# The deployed application simply loads the model and serves predictions.

# This is how most production ML systems work.

# 3-Scalability

# Imagine a website receiving:

# 10,000 predictions per minute

# Retraining for every request would be impossible.

# By saving the model:

# one trained model can serve thousands of users
# server resources are reduced
# response times stay low
# 4- APIs

# Many AI systems expose predictions through APIs.

# Example flow:

# User
#   ↓
# API Request
#   ↓
# Load Trained Model
#   ↓
# Predict
#   ↓
# Return Result

# The API does not retrain the model.

# It simply loads the saved model and predicts.

# This is common in:

# fraud detection systems
# recommendation engines
# medical prediction tools
# chatbot backends
# 5- Consistency

# Saving a model preserves:

# learned parameters
# coefficients
# training results

# Every server uses the same trained model, ensuring consistent predictions.

#  Real-World Example

# A bank's fraud detection system may train a model once and save it.

# Then:

# Customer Transaction
#         ↓
# Saved Model
#         ↓
# Fraud / Not Fraud

# The prediction happens in milliseconds.

#  Final Idea

# Model saving is important because it enables:

# Speed → no retraining every time
# Deployment → easy use in production
# Scalability → supports many users and requests
# APIs → instant predictions through services
# Consistency → same model behavior everywhere

# In real AI systems, the workflow is typically:

# Train → Save → Deploy → Load → Predict
