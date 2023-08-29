from fastapi import FastAPI
from model_handler import ModelVehicleDamageClassification

import json
app = FastAPI()
obj_model_veh_clfxn = ModelVehicleDamageClassification()


@app.get('/')
async def home():
    print(obj_model_veh_clfxn.getTunedModel())
    return {"AVL": "This is the home page."}

@app.get('/classify')
async def classify():
    vehicle_instance = obj_model_veh_clfxn.getRandomVehicleInstance()
    X = vehicle_instance.drop(['LABEL'], axis=1).values
    y = vehicle_instance['LABEL']
    X_preprocessed = obj_model_veh_clfxn.preProcessInstance(X)
    classification = obj_model_veh_clfxn.classify(X_preprocessed)
    print(classification)
    #print(classification)
    return {"predicted": classification, 
            "true": y.item()}

