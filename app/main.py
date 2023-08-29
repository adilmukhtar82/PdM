from fastapi import FastAPI
from .model_handler import ModelVehicleDamageClassification
from .db_handler import DBHandler

app = FastAPI()
obj_model_veh_clfxn = ModelVehicleDamageClassification()
obj_db = DBHandler()

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
    vehicle_instance['PREDICTED'] = y.item()
    insert_res = obj_db.insertClassifications(vehicle_instance)
    return {"predicted": classification, 
            "true": y.item(),
            "record_inserted": insert_res}
    
@app.get('/getVehicleInfo')
async def getVehicleIno(pseudo_vin: int):
    veh_info = obj_db.getVehicleInfo(pseudo_vin)
    
    return veh_info