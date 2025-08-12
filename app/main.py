from fastapi import FastAPI
from app.routers import prediction, model_information

app = FastAPI(title="ML Model API")

app.include_router(prediction.router)
app.include_router(model_information.router)
