# TASK 2 — Train/Test Split

# Perform:

# train_test_split()

# Use:

# test_size = 0.2
# random_state = 42

# Print:

# X_train.shape
# X_test.shape
# y_train.shape
# y_test.shape

# Understand the shapes.


import pandas as pd
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("student_data.csv")

# Features
X = df[["Study_Hours", "Attendance", "Previous_Score"]]

# Target
y = df["Pass"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Print shapes
print("X_train.shape:", X_train.shape)
print("X_test.shape:", X_test.shape)
print("y_train.shape:", y_train.shape)
print("y_test.shape:", y_test.shape)


# Expected output

# Because you have 12 rows:

# 80% → training data = 9 rows
# 20% → testing data = 3 rows

# So you should get:

# X_train.shape: (9, 3)
# X_test.shape: (3, 3)
# y_train.shape: (9,)
# y_test.shape: (3,)
# 🧠 Understand the shapes

# X_train.shape = (9, 3)

# Means:

# 9 students
# 3 features

# The 3 features are:

# Study_Hours
# Attendance
# Previous_Score

# X_test.shape = (3, 3)

# Means:

# 3 students
# 3 features

# y_train.shape = (9,)

# Means:

# 9 target values

# y_test.shape = (3,)

# Means:

# 3 target values
# Why do we split?

# Think of it like an exam:

#               12 Students
#                    │
#           ┌────────┴────────┐
#           │                 │
#      Training Data      Testing Data
#        9 students         3 students
#           │                 │
#      Learn patterns      Check performance

# The model learns from X_train + y_train and then we use X_test to see whether it can correctly predict y_test.

# Important: random_state=42 makes the split reproducible. If you run the code again, you get the same 9 training rows and 3 testing rows.