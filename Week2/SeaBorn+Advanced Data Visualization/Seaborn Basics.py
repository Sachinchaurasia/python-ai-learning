import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data={
#     "Name":["A","B","C","D"],
#     "Marks":[80,90,75,95]
    
# }
# df=pd.DataFrame(data)
# print(df)

# cleaner than normal matplotlib charts
# sns.barplot(x="Name", y="Marks", data=df)
# plt.show()


#scatter plot
# sns.scatterplot(x="Name", y="Marks", data=df)
# plt.show()

# histogram with seaborn

# sns.histplot(df["Marks"])

# plt.show()

#Heatmap

# data={
#     "Marks":[80,90,75,95],
#     "Hours":[2,3,1,4]
# }

# df=pd.DataFrame(data)
# numeric_df=df[["Marks", "Hours"]]

# sns.heatmap(numeric_df.corr(), annot=True)
# plt.show()

## Task 1---Employee Dataset

# employee_data={ 
#     "Name":["A","B","C"],
#     "Salary":[30000,50000,70000],
#     "Experience":[1,3,5]
    
# }

# df=pd.DataFrame(employee_data)

# # Bar plot for Salary
# sns.barplot(x="Name", y="Salary", data=df)
# plt.title("Employee Salary")
# plt.xlabel("Employee Name")
# plt.ylabel("Salary")
# plt.show()

# sns.barplot(x="Name", y="Experience", data=df)
# plt.title("Employee Experience")
# plt.xlabel("Employee Name")
# plt.ylabel("Experience (Years)")
# plt.show()

# sns.barplot(x="Salary",y="Experience", data=df)
# plt.title("Salary Vs Experience")
# plt.xlabel("Salary")
# plt.ylabel("Experience in (YearS)")
# plt.show()

 
 ##Scatterplot for Salary vs Experience
# sns.scatterplot(x="Salary", y="Experience", data=df)
# plt.title("Salary vs Experience")
# plt.xlabel("Salary")
# plt.ylabel("Experience(Years)")
# plt.show()


 # task 2-- Histogram practice 
# data={
    
#     "marks":[10,20,30,40,40,40]
    
     
#  }

# df=pd.DataFrame(data)

# sns.histplot(df["marks"])
# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")
# plt.show()

## Task 3-- Heatmap Practice

# data={
#     "Math":[80,90,70,100],
#     "Science":[85,95,75,90],
#     "english":[78,88,68,92
#                ]
# }

# df=pd.DataFrame(data)

# sns.heatmap(df.corr(), annot=True)
# plt.title("Correlation Heatmap")
# plt.show()


