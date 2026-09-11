# # TASK 8 — Evaluate

# # Run:

# # model.evaluate(X_test, y_test)

# # Record:

# # Test Loss
# # Test Accuracy

# ######################################################################## 

# Evaluate the Model

# Now we test the trained neural network on completely unseen test data.

# Step 1 — Run
# test_loss, test_accuracy = model.evaluate(X_test, y_test)

# You can also directly run:

# model.evaluate(X_test, y_test)

# You should see something similar to:

# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 50ms/step
# loss: 0.25
# accuracy: 1.00

# Your numbers will likely be different.

# Step 2 — Record the results

# Use:

# print("Test Loss:", test_loss)
# print("Test Accuracy:", test_accuracy)

# For example:

# Test Loss: 0.25
# Test Accuracy: 1.00

# So:

# Metric	Meaning
# Test Loss	How much error the model makes on unseen test data
# Test Accuracy	Percentage of test predictions that are correct
# 🧠 Important concept

# So far you've done:

# Training
#    ↓
# X_train + y_train
#    ↓
# Model learns
#    ↓
# Validation
#    ↓
# Monitor learning during training
#    ↓
# X_test + y_test
#    ↓
# FINAL EVALUATION

# Test data is the final exam for your model.

# A high training accuracy alone isn't enough. We want the model to perform well on unseen data too.

