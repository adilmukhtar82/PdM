import pickle
import pandas as pd
import random

class ModelVehicleDamageClassification:

    # load models for classification in the constructor
    def __init__(self):
        self.scaler_model = self.loadModels('../models/scaler.sav')
        self.tuned_model = self.loadModels('../models/tuned_rf_model.sav')
        self.log_model = self.loadModels('../models/log_model.sav')
        self.df_test_data = self.loadTestData('../data/test_logged_transformed_data.csv')

    # load specific model
    def loadModels(self,path):
        try:
            return pickle.load(open(path, 'rb'))
        except Exception as e:
            print(e)

    # load test data for predicitons
    def loadTestData(self, path):
        try:
            df_test = pd.read_csv(path, index_col=False)
            df_test = df_test.loc[:, ~df_test.columns.str.contains('^Unnamed')]

            return df_test
        
        except Exception as e:
            print(e)
    
    def preProcessInstance(self, X):
        return self.getScalerModel().transform(X)

    def classify(self, X):
       return self.getTunedModel().predict(X)[0].item()
       
    
    # randomly select vehicle data from test data for prediction
    def getRandomVehicleInstance(self):
        return self.getTestData().sample()

    # return test data
    def getTestData(self):
        return self.df_test_data
    
    # return saved scaler model
    def getScalerModel(self):
        return self.scaler_model
    
    # return saved classification model
    def getTunedModel(self):
        return self.tuned_model
    
    # return saved log model
    def getLogModel(self):
        return self.log_model