#MInMaxScaler
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#Create dataset
data={
    "Experience":[1,2,3,4,5],
    "Skills":[2,3,5,7,9]
}

df=pd.DataFrame(data)
print(df)

#create minmaxsclaer
scaler=MinMaxScaler()

#Transform data
scaled_data=scaler.fit_transform(df)

#Print Transformed data
print("\n Transformed data")

print(scaled_data)

##OutPut
#    Experience  Skills
# 0           1       2
# 1           2       3
# 2           3       5
# 3           4       7
# 4           5       9

#  Transformed data
# [[0.         0.        ]
#  [0.25       0.14285714]
#  [0.5        0.42857143]
#  [0.75       0.71428571]