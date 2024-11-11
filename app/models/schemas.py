
# app/models/schemas.py
from pydantic import BaseModel, Field, ConfigDict


class DiabetesInput(BaseModel):
    Pregnancies: int = Field(..., ge=0, description="Number of pregnancies")
    Glucose: float = Field(..., gt=0, description="Glucose level")
    BloodPressure: float = Field(..., ge=0, description="Blood pressure")
    SkinThickness: float = Field(..., ge=0, description="Skin thickness")
    Insulin: float = Field(..., ge=0, description="Insulin level")
    BMI: float = Field(..., gt=0, description="Body Mass Index")
    DiabetesPedigreeFunction: float = Field(...,
                                            gt=0, description="Diabetes pedigree function")
    Age: int = Field(..., gt=0, description="Age")


class PredictionResponse(BaseModel):
    prediction: int = Field(...,
                            description="0 for non-diabetic, 1 for diabetic")
    probability: float = Field(...,
                               description="Probability of being diabetic")
    risk_level: str = Field(..., description="Risk level (Low/Medium/High)")


class HealthResponse(BaseModel):
    # Disable protected namespace warning
    model_config = ConfigDict(protected_namespaces=())

    status: str
    is_model_loaded: bool  # Changed from model_loaded to is_model_loaded
