import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset
# Make sure your CSV file has columns for 'Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH', 'Rainfall', and 'Label' (target variable).
data = pd.read_csv('crop.csv')

# Define features (X) and target (y)
X = data[['NITROGEN','PHOSPHORUS','POTASSIUM','TEMPERATURE','HUMIDITY','PH','RAINFALL']]
y = data['CROP']  # The target variable, e.g., crop type

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the KNN model
knn = KNeighborsClassifier(n_neighbors=5)  # You can choose a different value for k

# Train the model
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy * 100:.2f}%')

# Save the trained model to a file
joblib.dump(knn, 'crop_knn_model.pkl')
