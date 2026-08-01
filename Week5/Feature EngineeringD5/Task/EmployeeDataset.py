#Employee Dataset
import pandas as pd
data={
    "Experience":[1,2,3,4,5],
    "Skills":[2,4,6,8,10]
    
}

#Create DataFrame
df=pd.DataFrame(data)

#Create New Features
df["Experience_skills"]=df["Experience"]* df["Skills"]
print(df)

