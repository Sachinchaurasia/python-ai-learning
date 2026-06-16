#import libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#create Dataset
data={
    "Experience":[1,2,4,6,8],
    "Promotion":[0,0,1,1,1]
}

df=pd.DataFrame(data)

#Features and Target
X=df[["Experience"]]
Y=df["Promotion"]
#Train Test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_size=0.2,
                                               random_state=42
)
#create model
model=KNeighborsClassifier(n_neighbors=3)

#Train model
model.fit(X_train,Y_train)

#Make Prediction
predictions=model.predict([[5]])
print(predictions)

#Accuracy
score=model.score(X_test,Y_test)
print(score)


# AI Thinking Task Answer

# KNN does not learn rules like Decision Trees.

# Instead, it stores the training data and predicts by looking at the nearest examples. Since most employees near 5 years of experience were promoted, KNN predicts Promotion = 1.