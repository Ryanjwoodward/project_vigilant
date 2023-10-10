"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
            _        _       _                _                  _                           
  _ __ ___ | |    __| | __ _| |_ __ _     ___| | ___  __ _ _ __ (_)_ __   __ _   _ __  _   _ 
 | '_ ` _ \| |   / _` |/ _` | __/ _` |   / __| |/ _ \/ _` | '_ \| | '_ \ / _` | | '_ \| | | |
 | | | | | | |  | (_| | (_| | || (_| |  | (__| |  __/ (_| | | | | | | | | (_| |_| |_) | |_| |
 |_| |_| |_|_|___\__,_|\__,_|\__\__,_|___\___|_|\___|\__,_|_| |_|_|_| |_|\__, (_) .__/ \__, |
            |_____|                 |_____|                              |___/  |_|    |___/ 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       October 9, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       ml_data_cleaning.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       The purpose of this file is to prepare the data used in ML process at different stages such as 
#                   |       making predictions or data storage.
#                   |   
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import pandas as pd

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------


#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------


"""
    The filter_latest_data function is designed to process a dictionary of prepared data, selecting specific 
    fields related to server metrics. It extracts fields such as CPU usage, network throughput, and performance 
    load averages, along with a timestamp. These selected fields are then organized into a new data dictionary. 
    The function further creates a Pandas DataFrame from this dictionary, ensuring it has an index to represent 
    the extracted metrics as a single row of data.
"""
def filter_latest_data(prepared_data):

    #? Define the list of fields to include in the new data dictionary
    selected_fields = [
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

    #? Create a new data dictionary by filtering the prepared data
    new_data_dictionary = {field: prepared_data[field] for field in selected_fields}

    #? Create a DataFrame from the new data dictionary with an index
    prediction_data = pd.DataFrame(new_data_dictionary, index=[0])

    return prediction_data

"""
    The function format_frame_to_dict(data_frame) serves to transform a DataFrame into a dictionary containing a single record. 
    It achieves this by utilizing the to_dict() method of the DataFrame with the specified orient parameter set to 'records', 
    which organizes the data in a dictionary format where each key represents a column name and its corresponding value corresponds 
    to the data within that column for a single row. Since the goal is to create a dictionary with a single record, the function 
    returns the resulting data dictionary
"""
def format_frame_to_dict(data_frame):
    #? Convert the DataFrame to a dictionary with a single record
    data_dict = data_frame.to_dict(orient='records')[0]
    return data_dict
