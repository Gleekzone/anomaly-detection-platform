from pydantic import BaseModel
from typing import List, Optional


class PredictionRequest(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = False
