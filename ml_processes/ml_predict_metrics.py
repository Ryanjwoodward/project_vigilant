"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
            _                         _ _      _                      _        _                        
  _ __ ___ | |     _ __  _ __ ___  __| (_) ___| |_     _ __ ___   ___| |_ _ __(_) ___ ___   _ __  _   _ 
 | '_ ` _ \| |    | '_ \| '__/ _ \/ _` | |/ __| __|   | '_ ` _ \ / _ \ __| '__| |/ __/ __| | '_ \| | | |
 | | | | | | |    | |_) | | |  __/ (_| | | (__| |_    | | | | | |  __/ |_| |  | | (__\__ \_| |_) | |_| |
 |_| |_| |_|_|____| .__/|_|  \___|\__,_|_|\___|\__|___|_| |_| |_|\___|\__|_|  |_|\___|___(_) .__/ \__, |
            |_____|_|                            |_____|                                   |_|    |___/ 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       October 9, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       ml_train_model.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       The purpose of this file to load the vigilant_ml_model and use it to produce predicted metrics
#                   |       for specific asepcts of a server.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------

import pandas as pd
import pickle

#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------


"""
    The function filter_data_predict_metric takes two arguments: model_filename and data_frame. 
    It first loads a pre-trained machine learning model from a file specified by model_filename, 
    which is expected to be in pickle format. Then, it selects specific features from the provided data_frame 
    to make predictions on using the loaded model. These features are related to metrics such as CPU usage 
    and network throughput but exclude the 'timestamp' feature. The function then uses the model to predict 
    values for these selected features and adds the predicted values as a new column called 'predicted_timestamp' 
    to the data_frame. If successful, it returns the modified data frame with predictions; otherwise, 
    it handles exceptions and returns None.
"""
def filter_data_predict_metric(model_filename, data_frame):
    try:
        #? Load the trained model
        with open(model_filename, 'rb') as model_file:
            loaded_model = pickle.load(model_file)

        #? Select the desired features for prediction, excluding 'timestamp'
        selected_features = [
            'cpu_usage_1mi',
            'cpu_usage_5mi',
            'cpu_usage_15mi',
            'network_throughput_rx',
            'network_throughput_tx',
            'perf_load_avg_1mi',
            'perf_load_avg_5mi',
            'perf_load_avg_15mi'
        ]

        #? Make predictions for the selected features
        predicted_timestamp = loaded_model.predict(data_frame[selected_features])

        #? Add the predicted timestamp to the data_frame DataFrame
        data_frame['predicted_timestamp'] = pd.to_datetime(predicted_timestamp, unit='ns')

        return data_frame
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

