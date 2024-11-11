# app/api/endpoints.py
from fastapi import APIRouter, HTTPException
from app.models.schemas import DiabetesInput, PredictionResponse, HealthResponse
from app.services.prediction_service import PredictionService

# Create router instance
router = APIRouter()

# Initialize service
prediction_service = PredictionService()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Check if the service is healthy and model is loaded"""
    return HealthResponse(
        status="healthy",
        # Changed from model_loaded to is_model_loaded
        is_model_loaded=hasattr(prediction_service.predictor, 'model')
    )


@router.post("/predict", response_model=PredictionResponse)
async def predict(input_data: DiabetesInput):
    """
    Predict diabetes risk based on input features
    """
    try:
        result = prediction_service.predict(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
