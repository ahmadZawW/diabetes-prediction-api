# app/core/config.py
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Diabetes Prediction API"
    MODEL_PATH: Path = Path("saved_models/random_forest.pkl")
    SCALER_PATH: Path = Path("saved_models/scaler.pkl")


settings = Settings()
