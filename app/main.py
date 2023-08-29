from fastapi import FastAPI
from model_handler import ModelVehicleDamageClassification

app = FastAPI()
model_vehicle_classification = ModelVehicleDamageClassification()


@app.get('/')
async def home():
    print(model_vehicle_classification.getSTunedModel())
    return {"AVL": "This is the home page."}

@app.get('/classify')
async def classify():
    return {"damage": 0}

