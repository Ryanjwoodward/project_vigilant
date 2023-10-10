"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
            _                                                            _                     
  _ __ ___ | |     _ __  _ __ ___   ___ ___  ___ ___     _ __ ___   __ _(_)_ __    _ __  _   _ 
 | '_ ` _ \| |    | '_ \| '__/ _ \ / __/ _ \/ __/ __|   | '_ ` _ \ / _` | | '_ \  | '_ \| | | |
 | | | | | | |    | |_) | | | (_) | (_|  __/\__ \__ \   | | | | | | (_| | | | | |_| |_) | |_| |
 |_| |_| |_|_|____| .__/|_|  \___/ \___\___||___/___/___|_| |_| |_|\__,_|_|_| |_(_) .__/ \__, |
            |_____|_|                              |_____|                        |_|    |___/ 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 29, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       ml_processes_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file serves as the entry point to all Machine Learning Operations. Such as Data Cleaning, 
#                   |       Model definition, Model Training, Predictive Analysis, etc.
#                   |   
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import pandas as pd

#? Imports for files Defined By Project Vigilant:
from data_handling_main import get_prepared_data
from ml_processes.ml_data_cleaning import *
from ml_processes.ml_predict_metrics import *
from ml_processes.ml_predicted_data_storage import *

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------

unfiltered_data_dict = {}
filtered_data_dict = pd.DataFrame()
predicted_data_dict = pd.DataFrame()
prepared_data_dict = {}
model_path = 'vigilant_ml_model.pkl'

#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    This function is the entyr point to all Machine Learning operations for the Project Vigilant
    application. This function begins by fetching the latest collected data, then filters it for
    the columns that are to be used in ML predictive analysis. The funiton then generates predictions
    based on that data and prepares a data form of that predicted data. Finally, the function converts
    the data form into a data dictionary and stores it in a Postgres DB.
"""
def init_ml_processes():

    #? Obtain the latest data collection results
    unfiltered_data_dict = get_prepared_data()  # Data Handling

    #? Filter the data dictionary and prepare it to be ingested by the ML Model
    filtered_data_dict = filter_latest_data(unfiltered_data_dict)  

    #? Make predictions using the filtered DataFrame
    predicted_data_dict = filter_data_predict_metric(model_path, filtered_data_dict)
    
    #? Prepare the predicted data to be stored in a Postgres DB
    prepared_data_dict = format_frame_to_dict(predicted_data_dict)

    #? Store the Predicted Data in Postgres
    store_data_in_postgres(prepared_data_dict)


   
    
