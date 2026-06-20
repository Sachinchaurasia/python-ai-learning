#  TASK 3 — Feature Importance

# For Random Forest:

# print(
#     rf_model.feature_importances_
# )

# Interpret:

# Which feature contributes most?

# Experience
# Skills
# Performance

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#Dataset
df=pd.read_csv("employee_promotion.csv")

X=df[["Experience","Skills","Performance"]]
Y=df["Promotion"]

#Train Random Forest

rf_model=RandomForestClassifier(random_state=42)
rf_model.fit(X,Y)

#Feature Importance
print(rf_model.feature_importances_)

