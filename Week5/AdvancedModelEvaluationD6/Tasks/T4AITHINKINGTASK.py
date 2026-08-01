# TASK 4 — AI THINKING TASK

# Answer in your own words:

# Why is AUC often preferred over Accuracy for imbalanced datasets?

# Think about:

# class imbalance
# threshold independence
# ranking predictions
# fraud detection

# AUC is often preferred over Accuracy for imbalanced datasets because accuracy can be misleading when one class has many more samples than the other. For example, in fraud detection, a model could predict every transaction as "not fraud" and still achieve high accuracy, while failing to detect actual fraud cases. AUC evaluates how well the model ranks positive examples above negative ones across all decision thresholds, making it independent of any single threshold. This provides a more reliable measure of a model's ability to distinguish between classes, especially when the minority class is the most important to detect.