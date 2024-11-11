
# app/models/predictor.py

import numpy as np
import pandas as pd
import pickle
from pathlib import Path


class DiabetesPredictor:
    def __init__(self, model_path: Path, scaler_path: Path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)
        with open(scaler_path, 'rb') as scaler_file:
            self.scaler = pickle.load(scaler_file)

    def preprocess_input(self, data: pd.DataFrame) -> pd.DataFrame:
        # Create BMI categories
        data['BMI_Category'] = pd.cut(data['BMI'],
                                      bins=[0, 18.5, 24.9, 29.9, 100],
                                      labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

        # Create age groups
        data['Age_Group'] = pd.cut(data['Age'],
                                   bins=[20, 30, 40, 50, 60, 100],
                                   labels=['20-30', '31-40', '41-50', '51-60', '60+'])

        # Log transform features
        data['Insulin'] = np.log1p(data['Insulin'])
        data['DiabetesPedigreeFunction'] = np.log1p(
            data['DiabetesPedigreeFunction'])

        # One-hot encode categorical variables
        data = pd.get_dummies(data, columns=['BMI_Category', 'Age_Group'])

        # Ensure all columns from training are present
        required_columns = self.scaler.get_feature_names_out()
        for col in required_columns:
            if col not in data.columns:
                data[col] = 0

        return data[required_columns]

    def predict(self, input_data: dict) -> tuple:
        # Convert input to DataFrame
        df = pd.DataFrame([input_data])

        # Preprocess
        processed_data = self.preprocess_input(df)

        # Scale
        scaled_data = self.scaler.transform(processed_data)

        # Predict
        prediction = self.model.predict(scaled_data)[0]
        probability = self.model.predict_proba(scaled_data)[0][1]

        return prediction, probability
