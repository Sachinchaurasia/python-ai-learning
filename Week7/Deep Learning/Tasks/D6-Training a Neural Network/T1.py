# Create student_data.csv:

# Study_Hours,Attendance,Previous_Score,Pass
# 2,60,45,0
# 3,65,50,0
# 4,70,55,0
# 5,75,65,1
# 6,80,70,1
# 7,85,75,1
# 8,90,85,1
# 9,95,90,1
# 3,62,48,0
# 5,78,68,1
# 4,68,52,0
# 7,88,80,1

# Load it using Pandas.

import pandas as pd

df = pd.read_csv("student_data.csv")

print(df)