# # # # # import  pandas as pd
# # # # # from sklearn.linear_model import LogisticRegression
# # # # # from sklearn.model_selection import train_test_split

# # # # # #Create Dataset

# # # # # #Student StudyHours vs Pass/fail
# # # # # data={
# # # # #     "Hours":[1,2,3,4,5,6],
# # # # #     "Pass":[0,0,0,1,1,1]
    
# # # # # }

# # # # # df=pd.DataFrame(data)

# # # # # #Features and Target
# # # # # X=df[["Hours"]]

# # # # # Y=df["Pass"]

# # # # # #Train/Test split
# # # # # X_train,X_test,Y_train,Y_test=train_test_split(
# # # # #     X,
# # # # #     Y,
# # # # #     test_size=0.2,
# # # # #     random_state=42
# # # # # )

# # # # # #Train Classification model
# # # # # model=LogisticRegression()
# # # # # model.fit(X_train,Y_train)

# # # # # #Make Prediction

# # # # # #will student Pass if studying for 5 hours?

# # # # # prediction=model.predict([[5]])
# # # # # print(prediction)

# # # # # #  Output Meaning
# # # # # # [1] → Pass
# # # # # # [0] → Fail

# # # # # #Check accuracy

# # # # # Score=model.score(X_test,Y_test)
# # # # # print(Score)

# # # # # #Visulaize Classification
# # # # # import matplotlib.pyplot as plt

# # # # # plt.scatter(df["Hours"],df["Pass"])
# # # # # plt.xlabel("Study Hours")
# # # # # plt.ylabel("Pass/Fail")
# # # # # plt.show()

# # # ##Task--1
# # # # #Exam Pass Prediction

# # # # import pandas as pd
# # # # from sklearn.linear_model import LogisticRegression

# # # # #Create dataset
# # # # data={
# # # #     "Hours":[1,2,3,4],
# # # #     "Pass":[0,0,1,1]
# # # # }
# # # # df=pd.DataFrame(data)
# # # # print(df)

# # # # #Features and Target
# # # # X=df[["Hours"]]
# # # # Y=df["Pass"]

# # # # #Train classification model

# # # # model=LogisticRegression()
# # # # model.fit(X,Y)

# # # # #Make prediction

# # # # predictions=model.predict(
# # # #                           pd.DataFrame(
# # # #                           [[5]],columns=["Hours"]    
                          
# # # #  ) )

# # # # print("predictions",predictions[0])

# # # # #optional 
# # # # if (predictions[0]==1):
# # # #     print("Pass")
# # # # else:
# # # #     print("Fail")
# #    #OUTPUT-- 
# # #        Hours  Pass
# # # 0      1     0
# # # 1      2     0
# # # 2      3     1
# # # 3      4     1
# # # predictions 1
# # # Pass

# # #Task--2 EMployee Proomotion Prediction

# # import pandas as pd
# # from sklearn.linear_model import LogisticRegression

# # #Create Dataset
# # data={
# #     "Experience":[1,3,5,7],
# #     "Promotion":[0,0,1,1]
# # }
# # df=pd.DataFrame(data)

# # #Features and Target
# # X=df[["Experience"]]

# # Y=df["Promotion"]

# # #Train Model
# # model=LogisticRegression()
# # model.fit(X,Y)

# # #Make predictions
# # predictions=model.predict(
# #     pd.DataFrame([[6]],columns=["Experience"]
# #                  )
# # )

# # print("predictions",predictions[0])


# #Task --3 Accuracy Checking

# # import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LogisticRegression

# # #create Dataset

# # data={
# #     "Experience":[1,3,5,7],
# #     "Promotion":[0,0,1,1]
# # }
# # df=pd.DataFrame(data)

# # #Features and Target
# # X=df[["Experience"]]
# # Y=df["Promotion"]

# # #Train/test split
# # X_train,X_test,Y_train,Y_test=train_test_split(X,
# #                                                Y,
# #                                                test_size=0.2,
# #                                                random_state=42)
# # #Train model
# # model=LogisticRegression()
# # model.fit(X_train,Y_train)

# # #Make Predictions
# # predictions=model.predict(X_test)
# # print(predictions)

# # #predict Accuracy
# # score=model.score(X_test,Y_test)
# # print(score)


# # TASK 4 — AI THINKING TASK

# # Why is classification important in real AI systems?

# # Think:

# # fraud detection
# # spam filters
# # medical diagnosis
# # security systems

# #______________________________
# Classification is extremely important in real AI systems because many real-world problems involve deciding between categories or classes.

# AI systems often need to answer questions like:

# Yes or No?
# Spam or Not Spam?
# Fraud or Genuine?
# Disease or Healthy?

# That is exactly what classification models do.

# 1 Fraud Detection

# Banks use classification models to detect suspicious transactions.

# The AI learns patterns from old transaction data and classifies new transactions as:

# Output	Meaning
# 0	Genuine
# 1	Fraud

# This helps:

# prevent financial loss
# detect cybercrime
# protect customers in real time
# 2 Spam Filters

# Email systems use classification to identify spam messages.

# The AI analyzes:

# keywords
# links
# sender behavior
# message patterns

# Then classifies emails as:

# Output	Meaning
# Spam	Dangerous/unwanted
# Not Spam	Safe email

# This protects users from:

# phishing
# scams
# malware
# 3 Medical Diagnosis

# AI classification models help doctors detect diseases.

# Example:

# tumor = benign or malignant
# patient = diabetic or non-diabetic
# scan = normal or abnormal

# The model learns from historical medical records and predicts disease categories.

# This helps:

# faster diagnosis
# early detection
# improved healthcare decisions
# 4 Security Systems

# Security AI uses classification for:

# face recognition
# fingerprint authentication
# intrusion detection
# suspicious activity detection

# Example:
# A security camera AI may classify:

# authorized person
# unknown intruder

# This improves safety and automation.

# 5 Fast Automated Decision Making

# Classification allows AI systems to make decisions instantly.

# Instead of humans checking thousands of cases manually, AI can quickly classify data automatically.

# This enables:

# scalability
# speed
# real-time monitoring
#  Binary Classification Concept

# Many systems use:

# Where:

# 0 = negative class
# 1 = positive class

# Examples:

# no fraud / fraud
# fail / pass
# safe / dangerous
#  Final Idea

# Classification is important because it helps AI systems:

# make decisions
# detect risks
# automate screening
# improve security
# support healthcare
# filter harmful content