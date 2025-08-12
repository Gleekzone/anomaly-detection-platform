from pydantic import BaseModel
from typing import Optional


class PredictionResponse(BaseModel):
    is_inlier: int
    anomaly_score: Optional[float] = None
