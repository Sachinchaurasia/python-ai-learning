# # TASK 7 — Experiment With Batch Size

# # Try:

# # batch_size = 2
# # batch_size = 4
# # batch_size = 8

# # Ask yourself:

# # Does changing batch size change the training behavior?

# ###############################################################################

# Experiment With Batch Size

# Yes — changing the batch size can change the training behavior.

# The idea is to train the same model architecture with different batch sizes:

# batch_size = 2
# batch_size = 4
# batch_size = 8
# 1️⃣ Batch size = 2
# model_2 = create_model()

# history_2 = model_2.fit(
#     X_train,
#     y_train,
#     epochs=50,
#     batch_size=2,
#     validation_split=0.2
# )
# 2️⃣ Batch size = 4
# model_4 = create_model()

# history_4 = model_4.fit(
#     X_train,
#     y_train,
#     epochs=50,
#     batch_size=4,
#     validation_split=0.2
# )
# 3️⃣ Batch size = 8
# model_8 = create_model()

# history_8 = model_8.fit(
#     X_train,
#     y_train,
#     epochs=50,
#     batch_size=8,
#     validation_split=0.2
# )
# 🧠 What does batch size mean?

# Suppose you have 16 training samples.

# With:

# batch_size = 2

# the model processes:

# 2 → 2 → 2 → 2 → 2 → 2 → 2 → 2

# With:

# batch_size = 4

# it processes:

# 4 → 4 → 4 → 4

# With:

# batch_size = 8

# it processes:

# 8 → 8

# Each batch is used to calculate the error and update the model's weights.

# 🔍 Compare the results

# After each experiment, look at:

# Batch Size	Training Loss	Validation Loss	Training Accuracy	Validation Accuracy
# 2	?	?	?	?
# 4	?	?	?	?
# 8	?	?	?	?

# You may notice that the learning curves aren't exactly the same.

# Generally:

# Smaller batch size

# batch = 2
#      ↓
# More frequent weight updates
#      ↓
# Learning can be noisier

# Larger batch size

# batch = 8
#      ↓
# Fewer weight updates per epoch
#      ↓
# Learning can be smoother

# But there isn't a rule that batch size 2 is always better than 8. The best value depends on the dataset, model, optimizer, and other settings.

# 🎯 Question to answer yourself

# Does changing batch size change the training behavior? Why?

# A good answer would be:

# Yes. Batch size determines how many training samples are processed before the model updates its weights. Changing it can affect the speed and stability of learning, and therefore can change training and validation loss and accuracy.


