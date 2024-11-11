# Diabetes Prediction API

## Overview

This project is a Diabetes Prediction API built using FastAPI, which implements a Machine Learning model to predict diabetes risk based on user input. The application follows the Model-View-Controller (MVC) architecture, ensuring a clean separation of concerns.


## Features

- Load and preprocess diabetes dataset.
- Train and evaluate machine learning models (Random Forest).
- Predict diabetes risk based on user input.
- RESTful API for interaction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmadZawW/diabetes-prediction-api.git
   cd diabetes-prediction-api
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI project:
   ```bash
   python run.py
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

3. Use the `/predict` endpoint to make predictions. The request body should follow the `DiabetesInput` schema.

## API Endpoints

### Health Check

- **GET** `/health`
  - Checks if the service is healthy and the model is loaded.

### Predict Diabetes Risk

- **POST** `/predict`
  - Request Body:
    ```json
    {
      "Pregnancies": 2,
      "Glucose": 120,
      "BloodPressure": 70,
      "SkinThickness": 20,
      "Insulin": 80,
      "BMI": 30,
      "DiabetesPedigreeFunction": 0.5,
      "Age": 25
    }
    ```
  - Response:
    ```json
    {
      "prediction": 0,
      "probability": 0.13,
      "risk_level": "low"
    }
    ```

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)