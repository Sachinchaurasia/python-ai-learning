 # install pandas library
 # pip install pandas
 
import pandas as pd

# data={
#     "Name":["Sachin","Rahul","Aman"],
#     "Age":[22,24,21],
#     "Salary":[50000,40000,45000]
    
# }
# df=pd.DataFrame(data)
#print(df)

#first rows
#print(df.head(1))

# Last rows
#print(df.tail(1))  # last rows one rows
#print(df.tail(2))  # last rows two rows

#print(df["Name"])
#print(df[["Name","Salary"]])  # Multiple columns
#print(df["Salary"])

## Basic Statistics
#print(df["Salary"].mean())
#print(df["Salary"].max())
#print(df["Salary"].min())

# Add New Column

# df["Bonus"]=df["Salary"]*0.10
# print(df)

#print(df[df["Salary"]>=45000])


# data={
#     "Name":["A","B","C"],
#     "Marks":[80,75,90]
    
# }
# df=pd.DataFrame(data)
# print(df)


# average=df["Marks"].mean()
# print("Average :",average)

# data={
#     "Salary":[25000,40000,50000]
    
# }
# df=pd.DataFrame(data)
# print(df)

# df["Bonus"]=df["Salary"]*0.20

# print(df)


# data={
#     "Student":["A","B","C"],
#     "Marks":[80,70,90]
    
# }

# df=pd.DataFrame(data)
# print(df)

# filtered_students=df[df["Marks"]>80]
# print(filtered_students)

# DataSet={
#     "Age" :[20,25,30]
    
    
# }
# df=pd.DataFrame(DataSet)

# df["Age_after_5_Years"]=df["Age"]+5
# print(df)
