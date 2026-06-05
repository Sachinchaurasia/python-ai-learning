###########################################################################################
# # import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LinearRegression


# # data = {
# #     "Experience": [1, 2, 3, 4, 5,6],
# #     "Skills": [2, 3, 5, 7, 9,10],
# #     "Salary": [30000, 40000, 50000, 65000, 80000,95000]
# # }

# # df = pd.DataFrame(data)

# # # Create CSV file
# # df.to_csv("employee.csv", index=False)

# # print("CSV file created successfully")
# # print(df.head())


# # print(df.columns)
 

# # #Features and target
# # X=df[["Experience","Skills"]]
# # Y=df["Salary"]

# # #Train test split
# # X_train,X_test,Y_train,Y_test=train_test_split(X,
# #                                                Y,
# #                                                test_size=0.2,
# #                                                    random_state=42
# # )

# # #Create Model
# # model=LinearRegression()

# # #Train Model
# # model.fit(X_train,Y_train)

# # #Evaluate Model
# # score=model.score(X_test,Y_test)
# # print("R^2 score:",score)

# # #Make Prediction
# # prediction=model.predict([[7,12]])
# # print("predicted salary:",prediction[0])

# # #Compare Actual Vs Predicted
# # predictions=model.predict(X_test)

# # comparison=pd.DataFrame({
# #     "Actual":Y_test,
# #     "predicted":predictions
# # })
# # print(comparison)

# # # Visulaization
# # import matplotlib.pyplot as plt
# # plt.scatter(df["Experience"],df["Salary"])
# # plt.title("Experience VS Salary")
# # plt.xlabel("Experience")
# # plt.ylabel("Salary")

# # plt.show()

# # #Save Model
# # import pickle
# # with open("Salary_model.pkl","wb") as file:
# #     pickle.dump(model,file)

# # #Load Trained model
# # with open("Salary_model.pkl","rb") as file:
# #     loaded_model=pickle.load(file)

# # #Predict using loaded model
# # result=loaded_model.predict([[8,14]])
# # print(result)

# ##Project Enhancement Tasks
###########################################################################################
# #Task 1--Add new Feature :Education_Level

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# import joblib
# data = {
#     "Experience": [1, 2, 3, 4, 5,6],
#     "Skills": [2, 3, 5, 7, 9,10],
#     "Salary": [30000, 40000, 50000, 65000, 80000,95000]
# }

# df = pd.DataFrame(data)

# # Add new features Education_Level
# df["Education_Level"]=[1,1,1,3,3,3]

# # Save CSV file
# df.to_csv("employee.csv", index=False)

# #Load csv file
# df=pd.read_csv("employee.csv")
# print(df)

# #Save model using joblib
# import joblib
# X=df[["Experience","Skills","Education_Level"]]
# Y=df["Salary"]

# #Create model
# model=LinearRegression()

# # Train model
# model.fit(X,Y)

# #Save model

# model=joblib.dump(model,"Salary_model.pkl")
# print("Model trained and saved successfully")

# ##Updated prediction Code
# import joblib

# #Load model
# model=joblib.load("Salary_model.pkl")

# experience=float(input("Enter experience"))
# skills=float(input("Enter skills Rating"))
# education=int(input("Enter Education Level(1=Graduate,2=Postgraduate,3=phD):"))


# prediction=model.predict([[experience,skills,education]])
# print(f"\nPrediction Salary:{prediction[0]:,.2f}")


##Task 2-- Create a csv file with 10+ records Train again observe accuracy changes
###########################################################################################
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib


Salary_data={
    "Experience":[1,2,3,4,5,6,2,3,4,5,7,8],
    "Skills":[2,3,5,7,9,10,4,6,8,8,10,9],
    "Education_Level":[1,1,2,2,3,3,1,2,2,3,3,3],
    "Salary":[30000,40000,50000,65000,80000,95000,42000,55000,70000,78000,105000,110000]
}

df=pd.DataFrame(Salary_data)

##Train and check accuracy


#Save CSV
df.to_csv("Salary_data.csv",index=False)

print(df)
#Load CSV
df=pd.read_csv("Salary_data.csv")

#Features and Target

X=df[["Experience","Skills","Education_Level"]]
Y=df["Salary"]

#Split Data
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                                Y,
                                                test_size=0.2,
                                                random_state=42)
#create model
model=LinearRegression()

#Train model
model.fit(X_train,Y_train)

#Predictions
Y_pred=model.predict(X_test)

#Accuracy
accuracy=r2_score(Y_test,Y_pred)
print(f"R2 Score:{accuracy:.4f}")

# Save model 
joblib.dump(model,"Salary_model.pkl")
print("model saved successfully")


##MINI Project Observation
#READ ME----------------------------
#Initially the model was trained on 6 records After expanding the dataset to 12 records and retraining ,the model achieved a more stable R2 score and produced better salary predictions .This demonstrates the importance of having suffiecient training data in machine learning project

##Task 3--Save model using Joblib instead of pickle

##Before (Using Pickle)
#############################################
#Save model
import pickle 
with open("Salary_model.pkl","wb") as file:
    pickle.dump(model,file)

#Load Model
import pickle 
with open("Salary_model.pkl","rb") as file:
    model=pickle.load(file)
    
##After using joblib
#################################################
import joblib
joblib.dump(model,"Salary_model.pkl")
print("model saved successfully")

#Load model
model=joblib.load("Salary_model.pkl")
print("model loaded Successfully")

## Complete Training Example
################################################################
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

#Load Dataset
df=pd.read_csv("Salary_data.csv")

#Features And Target

X=df[["Experience","Skills","Education_Level"]]
Y=df["Salary"]

#Create Model
model=LinearRegression()

# Train Model
model.fit(X,Y)

#Save Model

joblib.dump(model,"Salary_model.pkl")
print("model trained And saved using joblib")


##COMPLETE PREDICTION EXAMPLES
import joblib 

#Load Model
model=joblib.load("Salary_model.pkl")
Experience=float(input("Enter Experience"))
Skills=float(input("Enter skills "))
Education=int(input("Enter education level(1-3)"))
prediction=model.predict(
    [[Experience,Skills,Education]]
)
print(f"Predicted Salary:${prediction[0]:,.2f}")


## Task 4 -AI Thinking Task
##Why is train /test split necessary before deployment
#Think about 1-Memorization 2-Unseen Data 3-Real-world Data

# A train/test split is important because it helps us know whether a machine learning model can perform well on new data, not just the data it has already seen.

# 1. Memorization

# If we train and test a model on the same dataset, the model may simply memorize the training examples instead of learning real patterns.

# Example:

# A student memorizes answers from a practice test.
# They score 100% on that same test.
# But when given new questions, they may perform poorly.

# Similarly, a model that memorizes training data may appear highly accurate but fail in practice.

# 2. Unseen Data

# The test dataset contains data that the model has never seen during training.

# Testing on unseen data helps answer:

# "Can the model make correct predictions on new examples?"

# If the model performs well on unseen data, it is more likely to generalize well.

# 3. Real-World Data

# After deployment, users will provide completely new data every day.

# The test set simulates this real-world situation before deployment.

# For example:

# Training data: Past employee salary records.
# Real-world data: Information about a new employee joining tomorrow.

# A good model should predict accurately for both.

# Conclusion

# Train/test split is necessary because it:

# Prevents false confidence caused by memorization.
# Measures performance on unseen data.
# Simulates real-world usage before deployment.
# Helps ensure the model can generalize rather than just remember training examples.

# One-line interview answer:

# Train/test split is used to evaluate how well a machine learning model generalizes to unseen real-world data and to prevent misleading results caused by memorization of the training dataset.


