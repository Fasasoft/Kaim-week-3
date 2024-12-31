from sklearn.ensemble import RandomForestClassifier

# Instantiate the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model to the training data
model.fit(X_train, y_train)



#Model Evaluation

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


import matplotlib.pyplot as plt

# Get feature importances from the model
importances = model.feature_importances_

# Plot feature importances
plt.barh(X.columns, importances)
plt.xlabel("Feature Importance")
plt.title("Feature Importance for the RandomForest Model")
plt.show()



import shap

# Use SHAP to explain model predictions
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Plot SHAP summary plot
shap.summary_plot(shap_values[1], X_test)


