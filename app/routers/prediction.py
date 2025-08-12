from fastapi import APIRouter
from app.schemas.prediction_request import PredictionRequest
from app.schemas.prediction_response import PredictionResponse
from app.services.predict import make_prediction

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    features = [request.feature_vector]
    
    return make_prediction(features, return_score=request.score)
