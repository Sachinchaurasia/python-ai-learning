import pandas as pd
# Load the dataset

df=pd.read_csv("employee.csv")
print(df)

# DataSet info
# print(df.info())
# print(df.describe())
#output of describe() method:
#              Age  Experience       Salary
# count   5.000000    5.000000      5.00000
# mean   25.800000    3.400000  57000.00000
# std     3.193744    2.073644  23345.23506
# min    22.000000    1.000000  30000.00000
# 25%    24.000000    2.000000  45000.00000
# 50%    25.000000    3.000000  50000.00000
# 75%    28.000000    5.000000  70000.00000
# max    30.000000    6.000000  90000.00000

# Basic Analysis
# Average Salary
# average_salary=df["Salary"].mean()
# print("Average Salary", average_salary)

# #Highest Salary
# highest_salary=df["Salary"].max()
# print("Highest Salary",highest_salary)

# #Employee with salary >50000

# high_salary_employee=df[df["Salary"]>50000]
# print("Employees with salary greater than 50000")
# print(high_salary_employee)

# Salary Bar chart 
import matplotlib.pyplot as plt

# plt.bar(df["Name"],df["Salary"])
# plt.title("Employee Salary")
# plt.xlabel("Employee Name")
# plt.ylabel("Salary")
# plt.show()

import seaborn as sns

# sns.scatterplot(x="Experience",y="Salary", data=df)
# plt.title("Experience vs Salary")
# plt.xlabel("Experience (Years)")
# plt.ylabel("Salary")

# plt.show()

# numeric_df=df[["Age","Experience","Salary"]]
# sns.heatmap(numeric_df.corr(),annot=True)
# plt.title("Correlation Heatmap")
# plt.show()

#Task 1--- Add bonus Column to the dataset
df["Bonus"]=df["Salary"]*0.10
print(df)


#Task 2--- find Highest experience salary
Highest_experience_Salary=df["Experience"].max()
print("Highest_Experience_Salary",Highest_experience_Salary)

#Save updated dataset

df.to_csv("updated_employee.csv", index=False)
print("Updated dataset saved to 'updated_employee.csv'")
