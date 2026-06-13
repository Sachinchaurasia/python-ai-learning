#Scale Employee Dataset
import pandas as pd
from sklearn.preprocessing import StandardScaler

#Create Dataset
data={
    "Experience":[1,2,3,4,5],
    "Skills":[2,3,5,7,9]
}
df=pd.DataFrame(data)
print(df)

#create scale
scaler=StandardScaler()

#Scale Features
X=df[["Experience"]]
scaled_data=scaler.fit_transform(X)

print(scaled_data)

