# Vehicle Damage Classification
This repository implements various analysis and modeling techniques for the task of vehicle damage classification. The model is then deployed through [Docker](https://github.com/adilmukhtar82/PdM/blob/main/Dockerfile) container (locally). Mongodb is treated as the main data source for this project. 

The repository contains the following folders:
* [app/](https://github.com/adilmukhtar82/PdM/tree/main/app) 
This folder contains python files related to the deployment of the model through FastAPI, and implementation of APIs for various calls, e.g., classification, update database, retrieve vehicle fleet informtaion.