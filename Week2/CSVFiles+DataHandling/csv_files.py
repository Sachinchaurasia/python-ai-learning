# import pandas as pd

# df = pd.read_csv("Week2/CSVFiles+DataHandling/employee.csv")

# print(df)
# #Check Dataset information
# print(df.info())

# #find missing values
# print(df.isnull())

# #count missing values in each column
# print(df.isnull().sum())


# #Handle Missing values
# # df["Age"]=df["Age"].fillna(df["Age"].mean())
# # print(df)

# # remove missing rows used only when the data quality is too bad

# df.dropna(inplace=True)
# print(df)

# df.to_csv("cleaned_employee.csv", index=False)
# # Average salary
# print(df["Salary"].mean())

# #Highest Salary
# print(df["Salary"].max())

# #Lowest Salary
# print(df["Salary"].min())

# task 1-- Student CSV file
# import pandas as pd
# # Create a DataFrame with student data
# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
#     "Age": [20, 21, 19, 22, 20],
#     "Grade": ["A", "B", "A", "C", "B"]
# }
# df = pd.DataFrame(data)
# # Save the DataFrame to a CSV file
# df.to_csv("students.csv", index=False)
# # Read the CSV file back into a DataFrame
# df_students = pd.read_csv("students.csv")
# # Display the DataFrame
# print(df_students)
# # Check for missing values
# print(df_students.isnull().sum())
# # Calculate the average age of the students
# average_age = df_students["Age"].mean()
# print(f"Average Age: {average_age}")
# # Count the number of students in each grade
# grade_counts = df_students["Grade"].value_counts()
# print(grade_counts)

#import pandas as pd


# df=pd.read_csv("student.csv")

# print(df)

# df.info()

# #find the missing values
# print(df.isnull())

# # count missing values in each column
# print(df.isnull().sum())

# # fill the missing values with the average marks
# df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
# print(df)


#  Task 2-- Create a DataFrame with product data and perform basic analysis
# import pandas as pd
# data={
#     "Product":["Phone","Laptop","Tablet"],
#     "Price":[50000,70000,30000]
    
# }

# df=pd.DataFrame(data)

# print(df)

# average_price=df["Price"].mean()
# max_price=df["Price"].max()

# print("\n Average Price:",average_price)
# print("Maximum Price:",max_price)



# Task 3-- save cleaned file
import pandas as pd

df=pd.read_csv("student.csv")
print(df)

print(df.isnull())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print(df)
#save cleaned file

df.to_csv("cleaned_student.csv",index=False)
print(df)

# Alternatic=ve way to remove missing values and clean the data
# df.dropna(inplace=True)
# print(df)



