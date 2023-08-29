from pymongo import MongoClient
import json
from bson import json_util

class DBHandler:

    def __init__(self):
        self.myclient = MongoClient("mongodb://localhost:27017/")
        self.datbase = self.myclient["avl"]
        self.vehicle_collection = self.datbase["vehicle_fleet"]
        self.classifications = self.datbase["classifications"]

    
    def getVehicleInfo(self, psedo_vin=None):
        vehicle_info = self.vehicle_collection.find({"PSEUDO_VIN":psedo_vin})
        #print(list(vehicle_info))
        json_data = json.loads(json_util.dumps(vehicle_info))
        return json_data
    
    def insertClassifications(self, vehicle_info):
        try:
            json_vehicle_info = vehicle_info.to_dict('records')
            
            self.classifications.insert(json_vehicle_info)
 
            return "Success."
        except Exception as e:
            return "Unsuccessful"

       