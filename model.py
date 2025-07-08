import numpy as np
import joblib

# Load the pre-trained KNN model
model = joblib.load('crop_knn_model.pkl')

def predict_crop(data):
    data = np.array(data).reshape(1, -1)  # Reshape the input data for prediction
    prediction = model.predict(data)
    return prediction[0]
