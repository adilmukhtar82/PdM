# Vehicle Damage Classification
This repository implements various analysis and modeling techniques for the task of vehicle damage classification. The model is then deployed through [Docker](https://github.com/adilmukhtar82/PdM/blob/main/Dockerfile) container (locally). Mongodb is treated as the main data source for this project. 

The repository contains the following folders and files at [./](https://github.com/adilmukhtar82/PdM/tree/main) path:
* [app/](https://github.com/adilmukhtar82/PdM/tree/main/app): 

    This folder contains python files related to the deployment of the model through FastAPI, and implementation of APIs for various calls, e.g., classification, update database, retrieve vehicle fleet informtaion.

* [data/](https://github.com/adilmukhtar82/PdM/tree/main/data):

    This folder includes raw data of the vehicle fleet, along with preprocessed and analyzed dataset for the training and testing of the models.

* [docs/](https://github.com/adilmukhtar82/PdM/tree/main/docs):

    This folder contains files that provides information related to the problem statement.

* [models/](https://github.com/adilmukhtar82/PdM/tree/main/models):

    This folder contains trained model saved for the API calls. 

* [Dockerfile](https://github.com/adilmukhtar82/PdM/blob/main/Dockerfile):

    Dockerfile includes instructions to build the image of the application, which can be containerized.

* [EDA, Preprocessing and FeatureSelection.ipynb](https://github.com/adilmukhtar82/PdM/blob/main/EDA%2C%20Preprocessing%20and%20Feature%20Selection.ipynb):
    
    Jupyternotebook for the analysis of the data, feature importance, feature selection, and preprocessing.

* [Modeling.ipynb](https://github.com/adilmukhtar82/PdM/blob/main/Modeling.ipynb)
    
    Jupyternotebook for model selection and training.

* [requirements.txt](https://github.com/adilmukhtar82/PdM/blob/main/requirements.txt)
    
    This file contains relevant packages to create new environment for this project. 


![architecture](https://github.com/adilmukhtar82/PdM/blob/main/architecture.png)