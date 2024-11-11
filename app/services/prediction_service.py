
# app/services/prediction_service.py

from app.models.schemas import DiabetesInput, PredictionResponse
from app.models.schemas import DiabetesInput, PredictionResponse
from app.core.config import settings
from app.models.predictor import DiabetesPredictor


class PredictionService:
    def __init__(self):
        self.predictor = DiabetesPredictor(
            settings.MODEL_PATH, settings.SCALER_PATH)

    def predict(self, input_data: DiabetesInput) -> PredictionResponse:
        # Convert Pydantic model to dict
        data_dict = input_data.model_dump()

        # Make prediction
        prediction, probability = self.predictor.predict(data_dict)

        # Determine risk level
        risk_level = 'High' if probability > 0.7 else 'Medium' if probability > 0.3 else 'Low'

        return PredictionResponse(
            prediction=int(prediction),
            probability=float(probability),
            risk_level=risk_level
        )
