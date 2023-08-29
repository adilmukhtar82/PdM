import pickle

class ModelVehicleDamageClassification:

    # load models for classification in the constructor
    def __init__(self):
        self.scaler_model = self.loadModels('../model/scaler.sav')
        self.tuned_model = self.loadModels('../model/tuned_rf_model.sav')
        self.log_model = self.loadModels('../model/log_model.sav')


    # load specific model
    def loadModels(self,path):
        try:
            return pickle.load(open(path, 'rb'))
        except Exception as e:
            print(e)

    def getScalerModel(self):
        return self.scaler_model
    
    def getTunedModel(self):
        return self.tuned_model
    
    def getLogModel(self):
        return self.log_model