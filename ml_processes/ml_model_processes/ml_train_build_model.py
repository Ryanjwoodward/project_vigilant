"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            

            _    _             _           _           _ _     _                         _      _               
  _ __ ___ | |  | |_ _ __ __ _(_)_ __     | |__  _   _(_) | __| |    _ __ ___   ___   __| | ___| |  _ __  _   _ 
 | '_ ` _ \| |  | __| '__/ _` | | '_ \    | '_ \| | | | | |/ _` |   | '_ ` _ \ / _ \ / _` |/ _ \ | | '_ \| | | |
 | | | | | | |  | |_| | | (_| | | | | |   | |_) | |_| | | | (_| |   | | | | | | (_) | (_| |  __/ |_| |_) | |_| |
 |_| |_| |_|_|___\__|_|  \__,_|_|_| |_|___|_.__/ \__,_|_|_|\__,_|___|_| |_| |_|\___/ \__,_|\___|_(_) .__/ \__, |
            |_____|                  |_____|                   |_____|                             |_|    |___/ 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       October 9, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       ml_train_build_model.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       The purpose of this file is to train and save an ML model that uses a linear
#                   |       regression algorithm to provide predictive analysis for certain metrics
#                   |       related to the monitoring of a server.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import redis
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------


#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------


"""
    The train_vigilant_ml_model function connects to a Redis server to retrieve monitoring data, preprocesses it, 
    trains a linear regression model to predict timestamps, and then saves the trained model using the pickle library. 
    It's designed to create a machine learning model for predicting timestamps based on specific metrics related to server 
    monitoring data stored in a Redis database.
"""
import redis
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_vigilant_ml_model():
    #? Redis server details
    redis_host = 'redis-18635.c62.us-east-1-4.ec2.cloud.redislabs.com'
    redis_port = 18635
    redis_password = 'veQLwCVeOnqZQ6k6kk2yPgHpLVP0KbV3'
    redis_db = 0

    #? Connect to Redis server
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, db=redis_db, decode_responses=True)

    #? Retrieve data from Redis and create a Pandas DataFrame
    data_dicts = []

    #? Iterate over keys in Redis that match the pattern "vigilant_set*"
    for key in redis_client.scan_iter("vigilant_set*"):
        hash_data = redis_client.hgetall(key)
        
        #? Extract relevant data from Redis hash and convert to proper types
        extracted_data = {
            'cpu_usage_1mi': float(hash_data.get('cpu_usage_1mi', 0.0)),
            'cpu_usage_5mi': float(hash_data.get('cpu_usage_5mi', 0.0)),
            'cpu_usage_15mi': float(hash_data.get('cpu_usage_15mi', 0.0)),
            'network_throughput_rx': float(hash_data.get('network_throughput_rx', 0.0)),
            'network_throughput_tx': float(hash_data.get('network_throughput_tx', 0.0)),
            'perf_load_avg_1mi': float(hash_data.get('perf_load_avg_1mi', 0.0)),
            'perf_load_avg_5mi': float(hash_data.get('perf_load_avg_5mi', 0.0)),
            'perf_load_avg_15mi': float(hash_data.get('perf_load_avg_15mi', 0.0)),
            'timestamp': pd.to_datetime(hash_data.get('timestamp', '1970-01-01 00:00:00'))
        }
        data_dicts.append(extracted_data)

    df = pd.DataFrame(data_dicts)

    #? Select the desired features for prediction, including 'timestamp'
    selected_features = [
        'cpu_usage_1mi',
        'cpu_usage_5mi',
        'cpu_usage_15mi',
        'network_throughput_rx',
        'network_throughput_tx',
        'perf_load_avg_1mi',
        'perf_load_avg_5mi',
        'perf_load_avg_15mi',
        'timestamp'
    ]

    #? Split data into features (X) and target (y)
    X = df[selected_features[:-1]]  #? Exclude 'timestamp' from features
    y = df['timestamp']

    #? Create a linear regression model
    model = LinearRegression()

    #? Train the model
    model.fit(X, y)

    #? Save the trained model to a file using pickle
    model_filename = 'vigilant_ml_model.pkl'

    try:
        with open(model_filename, 'wb') as model_file:
            pickle.dump(model, model_file)
        print("Model saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the model: {str(e)}")



