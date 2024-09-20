# sensor_fault_detection
Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.


Step 1: Creating conda environment 
$ conda create -p venv python==3.8 -y

Step 2: Activating the environmnet 
$ conda activate venv/

Step 4: Create a main folder name sensor 

Step 5: create requirement.txt

Step 6: Setup 
create setup.py file 

step 7: installing packages in requirements.txt
$ pip install -r requirements.txt

Step 8:Create a pileline folder in sensor folder in our main folder.
pipeline is used for sequence and execution flow.

Step 9: Create components folder.

Step 10: Creating folder data_access for accessing data from MongoDB
Main task of data access to communicate with database and create a csv file.
In this folder we will write a fuction to connect with MongoDB and create a csv file so that we can use it later in project.

Step 11: Creating folder cloud_storage because we will work with cloud like s3(simple store structure) bucket.

Step 12: Creating folder configuration for connection details 
Configuration for connection with mongoDB and s3 bucket.

Step 13: Create constant folder to maintain folder name,model name ,variable declaration etc.

Step 14: create logger.py and exception.py

Step 15: Create entity to define input output for every component.

Step 16: Create artifact_entity.py in entity folder used for output data.

Step 17: Create config_entity.py in entity folder used for input data.

Step 18: Create ml folder.  

Step 19: Connect MongDb 
mongoDB_url  = mongodb+srv://prashant:<password>@cluster0.sxxfnqg.mongodb.net/

Step 20: we are writing pymongo[srv] == 4.2.0 in requirement.txt because our mongodb connection  is from mongodb atlas you can 
see srv in the link too ,again install requirement.txt


Step 21: Starting with logger and exceptions.

Step 22: Creating env_variable.py,database.py,s3_bucket.py,application.py file 

Step 23: mongodb connection 

Step 24:Creating Traning_pipeline folder in constant  

Step 25: Creating config folder in main dir and in that creating schema.yaml

Step 26: data ingestion in config_entity.py
class
TrainingPipelineConfig
DataIngestionConfig


Step 27: data_ingestion.py components

step 28: training_pipeline.py in pipeline
class
TrainPipeline
    functions 
    start_data_ingestion
    start_data_validation
    start_data_transformation
    start_model_trainer
    start_model_evaluation
    start_model_pusher
    run_pipeline

Step 29: artifact_entity.py
class
DataIngestionArtifact

Step 28: Data ingestion component
class
DataIngestion
    functions 
    intital function 
    export_data_into_feature_store
    split_data_as_train_test
    initiate_data_ingestion

Step 29: for exporting data into export_data_into_feature_store we will create a sensor_data.py in data _access folder

Step 30: Data ingestion done.And starting data integration and data transformation.