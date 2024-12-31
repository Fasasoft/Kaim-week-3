import pandas as pd
from sklearn.model_selection import train_test_split

# Load your data (replace with the actual data file)
data = pd.read_csv("your_data.csv")

# Clean the data (example: fill missing values)
data.fillna(method='ffill', inplace=True)

# Feature engineering (example: adding a new feature)
data['new_feature'] = data['feature1'] * data['feature2']

# Split the data into training and testing sets
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


