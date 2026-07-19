import pandas as pd

# Create Dataset
data = {
    "Hours": [2, 3, 4, 5],
    "Days": [5, 4, 3, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create New Feature
df["Total_Study_Hours"] = df["Hours"] * df["Days"]

# Print Updated DataFrame
print(df)