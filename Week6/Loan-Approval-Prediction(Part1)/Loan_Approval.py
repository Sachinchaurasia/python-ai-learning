#Step 1 Create CSV File
#Step 2- Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 3- Load the dataset
df = pd.read_csv("loan_data.csv", sep="\t")
print(df.head())

#Step 4-understand the dataset
#Checking the shape of the dataset
print(df.shape)

#Columns name
print(df.columns)

#Data types of the columns
print(df.dtypes)

#Understand which columns are categorical and which are numerical

#Dataset information
print(df.info())
#this tells you  1- missing values, 2- data types, 3- memory usage, 4- number of non-null values in each column

#Statstical summary of the dataset
print(df.describe())

#Observe Mean minimum maximum and standard deviation of the numerical columns

#Step 5 -Missing Values
print(df.isnull().sum())

#Step 6
#Handle missing values
 #For numeric Columns:
df["LoanAmount"]=df["LoanAmount"].fillna(df["LoanAmount"].mean())

#For categorical columns:
df["Gender"]=df["Gender"].fillna(df["Gender"].mode()[0])

#Step 7 -Check for duplicate Rows
print(df.duplicated().sum())

#Removes duplicates

df=df.drop_duplicates()

#Step 8-Explore Target Variable
#Count Approvals
print(df["Loan_Status"].value_counts())

#Visualize:

sns.countplot(x="Loan_Status",data=df)
plt.show()

#Step 9-Explore Numerical Features
#Income Distribution

plt.hist(df["Income"])
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

#Loan Amount Distribution

plt.hist(df["LoanAmount"])
plt.title("Loan Amount Distribution")
plt.show()

#Step 10 -Explore relationship between Income and Loan Amount

plt.scatter(df["Income"],
            df["LoanAmount"])

plt.xlabel("Income")
plt.ylabel("LoanAmount")
plt.show()

#Step 11-Correlation (Numeric Features)
#First Select ojnly numeric features

numeric_df=df.select_dtypes(include=[np.number])

#Correlation matrix
print(numeric_df.corr())

#HeatMap of Correlation Matrix
sns.heatmap(numeric_df.corr(),annot=True,cmap="coolwarm"
            
    )
plt.show()


# OUTPUT____

#    Gender Married  Income  LoanAmount  CreditHistory Education Loan_Status
# 0    Male     Yes    5000         150              1  Graduate           Y
# 1  Female      No    3000          90              1  Graduate           Y
# 2    Male     Yes    2500         120              0  Graduate           N
# 3  Female      No    4500         130              1  Graduate           Y
# 4    Male     Yes    6000         200              1  Graduate           Y
# (10, 7)
# Index(['Gender', 'Married', 'Income', 'LoanAmount', 'CreditHistory',
#        'Education', 'Loan_Status'],
#       dtype='str')
# Gender             str
# Married            str
# Income           int64
# LoanAmount       int64
# CreditHistory    int64
# Education          str
# Loan_Status        str
# dtype: object
# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 7 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   Gender         10 non-null     str  
#  1   Married        10 non-null     str  
#  2   Income         10 non-null     int64
#  3   LoanAmount     10 non-null     int64
#  4   CreditHistory  10 non-null     int64
#  5   Education      10 non-null     str  
#  6   Loan_Status    10 non-null     str  
# dtypes: int64(3), str(4)
# memory usage: 692.0 bytes
# None
#             Income  LoanAmount  CreditHistory
# count    10.000000   10.000000      10.000000
# mean   4350.000000  142.000000       0.700000
# std    1468.370223   42.110965       0.483046
# min    2500.000000   90.000000       0.000000
# 25%    3125.000000  112.500000       0.250000
# 50%    4250.000000  135.000000       1.000000
# 75%    5150.000000  157.500000       1.000000
# max    7000.000000  220.000000       1.000000
# Gender           0
# Married          0
# Income           0
# LoanAmount       0
# CreditHistory    0
# Education        0
# Loan_Status      0
# dtype: int64
# 0
# Loan_Status
# Y        7
# N        2
# N        1
# Name: count, dtype: int64
