import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

#Dataset
data={
    "Hours":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1]
}

df=pd.DataFrame(data)

#Features and Target

X=df[["Hours"]]
Y=df["Pass"]

#Number of trees to test
tree_values=[10,50,100,200]
best_trees=None
best_score=0
results=[]

print("Random Forest Hyperparameter Tuning\n")

for trees in tree_values:
    model=RandomForestClassifier(
        n_estimators=trees,
        random_state=42
    )
    scores=cross_val_score(model,X,Y,cv=3)
    avg_score=scores.mean()
    print(f"Trees={trees}")
    print("Cv scores:",scores)
    print("Average Accuracy:",avg_score)
    print("-"*40)
    results.append([trees,avg_score])
if avg_score>best_score:
    best_score=avg_score
    best_trees=trees

#Comparision Table
comparision=pd.DataFrame(results,columns=["Trees","CV Accuracy"])
print("\n Comparision Table")
print(comparision)

print("\n Best number of Trees:",best_trees)
print("Best Average Accuracy:",best_score)

