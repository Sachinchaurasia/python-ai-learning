import tensorflow as tf

#print(tf.__version__)

x=tf.constant([10,20,30])
print(x)

print(x.shape)
print(x.dtype)

#Tensor Operations

a=tf.constant([1,2,3])
b=tf.constant([4,5,6])

print(a+b)

print(a*b)

#Create your First neural network

model=tf.keras.Sequential([
    tf.keras.layers.Dense(16,activation="relu"),
    tf.keras.layers.Dense(8,activation="relu"),
    tf.keras.layers.Dense(1,activation="sigmoid")
])




# 🧠 1. What is Deep Learning?

# Deep Learning is a part of Machine Learning that uses neural networks with multiple layers to learn patterns from data.

# Think of the progression:

# Artificial Intelligence
#         ↓
# Machine Learning
#         ↓
# Deep Learning
#         ↓
# Neural Networks
# Simple example

# Suppose we want to predict whether a person has heart disease.

# We give the model:

# Age
# Blood Pressure
# Cholesterol
# Maximum Heart Rate
# Chest Pain

# A traditional ML model might directly learn relationships between these features and:

# Disease = 0 or 1

# A deep neural network instead processes the information through multiple layers:

# Input Data
#     ↓
# Input Layer
#     ↓
# Hidden Layer 1
#     ↓
# Hidden Layer 2
#     ↓
# Output Layer
#     ↓
# Prediction

# The important idea is:

# Deep Learning automatically learns increasingly complex patterns through multiple layers of neurons.

# 🧠 2. What is a neuron?

# A neuron is the basic processing unit of a neural network.

# Think of a neuron as a small decision-making unit.

# Suppose we have:

# Age = 50
# BP = 140
# Cholesterol = 250

# A neuron receives these values and performs calculations.

# Conceptually:

# Age ─────────┐
#              │
# BP ──────────┼──→ 🧠 Neuron ──→ Output
#              │
# Cholesterol ─┘

# Inside the neuron, values are combined using weights and a bias, and then an activation function is applied.

# Conceptually:

# Inputs
#    ↓
# Weighted calculation
#    ↓
# Activation function
#    ↓
# Neuron output

# You don't need to memorize the mathematics yet.

# For now remember:

# Neuron = a small computational unit that receives inputs, processes them, and produces an output.

# 🧠 3. Input Layer vs Hidden Layer

# This is very important.

# Imagine:

# Age
# BP
# Cholesterol
#    ↓
# ┌──────────────────┐
# │   INPUT LAYER    │
# └──────────────────┘
#           ↓
# ┌──────────────────┐
# │   HIDDEN LAYER   │
# │ 🧠 🧠 🧠 🧠      │
# │ 🧠 🧠 🧠 🧠      │
# └──────────────────┘
#           ↓
# ┌──────────────────┐
# │  OUTPUT LAYER    │
# └──────────────────┘
# Input Layer

# The input layer receives the original features.

# For our heart disease example:

# Age
# Sex
# BP
# Cholesterol
# MaxHR
# ChestPain

# These are the inputs.

# So if we have 6 features, the input layer generally receives 6 input values.

# Hidden Layer

# The hidden layer is where the neural network learns patterns and relationships.

# For example, it might learn combinations such as:

# High BP + High Cholesterol

# or

# Age + Chest Pain + Low MaxHR

# These aren't manually programmed by us. The network learns useful representations during training.

# Easy memory trick
# INPUT  = What we give the network

# HIDDEN = Where the network learns patterns

# OUTPUT = What the network predicts
# 🧠 4. Why does a neural network have multiple neurons?

# Because one neuron cannot learn all the different patterns in complicated data.

# Imagine 4 neurons:

#              ┌── 🧠 Neuron 1
# Inputs ──────┼── 🧠 Neuron 2
#              ├── 🧠 Neuron 3
#              └── 🧠 Neuron 4

# Each neuron can learn a different pattern.

# For example:

# Neuron 1 → learns relationship involving Age

# Neuron 2 → learns relationship involving BP

# Neuron 3 → learns relationship involving Cholesterol

# Neuron 4 → learns combination of several features

# The next layer can then combine those learned patterns.

# Features
#    ↓
# 🧠 🧠 🧠 🧠
#    ↓
# 🧠 🧠 🧠 🧠
#    ↓
# Prediction
# Very important idea

# Multiple neurons allow the network to learn multiple patterns simultaneously.

# This is one reason neural networks can handle complex relationships.

# 🧠 5. What is a Tensor?

# This one looks scary initially, but the basic idea is actually simple.

# A tensor is a data structure used to store numerical data, often as an array with one or more dimensions.

# You've already seen similar structures in NumPy.

# 0-dimensional tensor

# A single number:

# 5

# Conceptually:

# Scalar
# 1-dimensional tensor

# A list:

# [10, 20, 30]

# Conceptually:

# Vector
# 2-dimensional tensor

# A table:

# [
#  [10, 20, 30],
#  [40, 50, 60]
# ]

# Conceptually:

# Matrix
# 3-dimensional tensor

# Think of multiple tables stacked together:

# Table 1
# Table 2
# Table 3

# So:

# 0D → Scalar
# 1D → Vector
# 2D → Matrix
# 3D → Tensor
# 4D → Tensor
# ...

# Technically, tensor is the general term that includes scalars, vectors, matrices, and higher-dimensional arrays.

# Why does Deep Learning use tensors?

# Because neural networks process numerical data in batches.

# For example:

# 10 employees
# 6 features each

# could be represented as:

# 10 × 6

# That is a 2D tensor.

# TensorFlow performs mathematical operations on these tensors very efficiently.

# Easy memory trick

# Tensor = a container for numerical data arranged in one or more dimensions.

# 🧠 6. What does Dense(16) mean?

# This is extremely important because you'll see it constantly in TensorFlow/Keras.

# Suppose we write:

# from tensorflow.keras import Sequential
# from tensorflow.keras.layers import Dense

# model = Sequential([
#     Dense(16)
# ])

# Dense(16) means:

# Create a fully connected layer containing 16 neurons.

# So:

# Dense(16)

# means:

# 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠
# 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠

#        16 neurons
# Why is it called Dense?

# Because every neuron in this layer is connected to the neurons in the previous layer.

# For example:

# Input
#   ↓
# 🧠 ─────┐
# 🧠 ─────┼────→ 🧠
# 🧠 ─────┼────→ 🧠
# 🧠 ─────┘      🧠
#                🧠
#              Dense(16)

# The exact number 16 is called the number of units/neurons in that layer.

# 🔥 Put everything together

# Suppose we build:

# model = Sequential([
#     Dense(16, activation="relu"),
#     Dense(8, activation="relu"),
#     Dense(1, activation="sigmoid")
# ])

# Read it like this:

# Input
#   ↓
# Dense(16)
# 16 neurons
#   ↓
# Dense(8)
# 8 neurons
#   ↓
# Dense(1)
# 1 neuron
#   ↓
# Prediction

# So:

# Dense(16) → 16 neurons
# Dense(8)  → 8 neurons
# Dense(1)  → 1 neuron

# And:

# activation="relu"

# means we're using the ReLU activation function in that layer.

# We'll learn activation functions separately, so don't worry about the mathematics yet.

# 🎯 The mental model I want you to remember

# Whenever you see a neural-network diagram or code, ask these 5 questions:

# ① What goes IN?
# INPUT FEATURES
# ② How many neurons are processing it?
# Dense(16)
#         ↑
#      16 neurons
# ③ How many hidden layers are there?
# Input
#  ↓
# Hidden 1
#  ↓
# Hidden 2
#  ↓
# Output
# ④ What comes OUT?
# Prediction
# ⑤ What type of problem is it?
# Classification → categories
# Regression    → continuous number
# 🧩 Quick example

# If you see:

# model = Sequential([
#     Dense(16, activation="relu"),
#     Dense(8, activation="relu"),
#     Dense(1, activation="sigmoid")
# ])

# You should immediately be able to say:

# "This neural network has a hidden layer with 16 neurons, another hidden layer with 8 neurons, and an output layer with 1 neuron."

# That's the level of understanding we're aiming for in Week 7.

# Your 6 answers in one line each
# Question	Easy answer
# Deep Learning	ML using neural networks with multiple layers
# Neuron	A computational unit that processes inputs
# Input vs Hidden	Input receives features; hidden layers learn patterns
# Multiple neurons	Different neurons can learn different patterns
# Tensor	A structure for storing numerical data in multiple dimensions
# Dense(16)	A fully connected layer containing 16 neurons