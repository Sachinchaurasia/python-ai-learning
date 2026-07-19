import pandas as pd
from sklearn.linear_model import LinearRegression
 #Creater Dataset
data={
    "Experience":[1,2,3,4,5],
    "Skills":[2,3,5,7,9],
    "Salary":[30000,40000,50000,60000,70000]
    
     
 }

#Create DataFrame
df=pd.DataFrame(data)

#Feature Engineering

df["Experience_Skills"]=df["Experience"]*df["Skills"]

#Print Updated DataFrame
print(df)

#Features and Target
X=df[["Experience","Skills","Experience_Skills"]]
Y=df["Salary"]

#Train Model
model=LinearRegression()
model.fit(X,Y)

#Predict Salary
new_data=pd.DataFrame({
    "Experience":[6],
    "Skills":[10],
    "Experience_Skills":[60]
})

prediction=model.predict(new_data)

print("\n preedicted salary",prediction[0])

