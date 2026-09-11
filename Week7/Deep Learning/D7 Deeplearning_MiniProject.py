import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#Load Dataset
df=pd.read_csv(Student_data.csv)
print(df)

print(df.head())
print(df.info())
print(df.describe())

#Check missing Values
print(df.isnull().sum())

#Separate Features and Target
X=df[[
    "Study_Hours",
    "Attendance",
    "Previous_Score"
]]

Y=df["Pass"]

print("X:",X)
print("Y:",Y)

#Train /test split
X_train,X_test,Y_train,Y_test=train_test_split(X,
                                               Y,
                                               test_szie=0.2,
                                               random_state=42)

print("Training data:",X_train.shape)
print("Testing data:",X_test.shape)

#Feature Scaling
scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_test=scaler.trandform(X_test)

#Build Neural Network
model=tf.keras.Sequential([
    tf.keras.layers.dense(8,activation="relu"),
    tf.keras.layers.dense(4,activation="relu"),
    tf.keras.layers.dense(1,activation="sigmoid")
])

#Model Summary
model.summary()

#Compile the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

#Train the model
history=model.fit(
    X_train,
    Y_train,
    epochs=100,
    batch_size=4,
    validation_split=0.2,
    verbose=1
)

#Check training accuracy

print(history.history.keys())

#print final values
print("Final Training Accuracy:",history.history["accuracy"][-1])

print("Final Validation Accuracy:",history.history["val_accuracy"][-1])

#Plot Training Loss

plt.plot(history.history["loss"],label="Training Loss")
plt.plot(history.history["val_loss"],label="validation Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Vs Validation Loss")
plt.legend()
plt.show()

#plot Accuracy
plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
    
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training Vs Validation Accuracy")

plt.legend()
plt.show()


#Evaluate on Test data
test_loss,test_accuracy=model.evaluate(X_test,Y_test)

print("Test Loss",test_loss)
print("Test Accuracy",test_accuracy)

#Make Predictions
predictions=model.predict(X_test)
print(predictions)


#Convert Probability to class
predicted_classes=(predictions>=0.5).astype(int)

print(predicted_classes)


#Compare Actual Vs Predicted
print("Actual")
print(Y_test.values)

print("Predicted")
print(predicted_classes.flatten())


#Confusion Matrix
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay(
    confusion_matrix=cm).plot()

plt.title("Confusion Matrix")
plt.show()

#Predict a Completely New Student
new_Student=np.array([
    [8,91,87]
])

new_Student_Scaled=scaler.transform(new_Student)

probability=model.predict(new_Student_Scaled)
print("Pass Probability:",probability[0][0])

if probability[0][0]>=0.5:
    print("Prediction:PASS")
else:
    print("Prediction:FAIL")
    

#Save Your Neural Network
model.save("Student_pass_model.keras")

#Save the scaler
import joblib
joblib.dump(scaler,
            "Student_scaler.pkl")


#Load the model Again
loaded_model=tf.keras.models.load_model(
    "Student_pass_model.keras"
    
)

#Load Scaler
loaded_scaler=joblib.load("Student_scaler.pkl")

new_student=np.array([
    [8,91,87]
])

new_Student_Scaled=loaded_scaler.transform(new_student)

prediction=loaded_model.predict(new_Student_Scaled)
print(prediction)

