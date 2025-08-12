from fastapi import APIRouter
from app.models.model_loader import model

router = APIRouter(prefix="/model_information", tags=["Model Information"])

@router.get("/")
def get_model_information():
    params = model.get_params()
    return params
