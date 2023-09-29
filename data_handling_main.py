
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
      _       _            _                     _ _ _                                 _                     
   __| | __ _| |_ __ _    | |__   __ _ _ __   __| | (_)_ __   __ _     _ __ ___   __ _(_)_ __    _ __  _   _ 
  / _` |/ _` | __/ _` |   | '_ \ / _` | '_ \ / _` | | | '_ \ / _` |   | '_ ` _ \ / _` | | '_ \  | '_ \| | | |
 | (_| | (_| | || (_| |   | | | | (_| | | | | (_| | | | | | | (_| |   | | | | | | (_| | | | | |_| |_) | |_| |
  \__,_|\__,_|\__\__,_|___|_| |_|\__,_|_| |_|\__,_|_|_|_| |_|\__, |___|_| |_| |_|\__,_|_|_| |_(_) .__/ \__, |
                     |_____|                                 |___/_____|                        |_|    |___/                          
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 11, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       data_handling_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file serves as the entry point to all data handling operations. Such as collection, cleaning,
#                   |       preparation, and storage.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import datetime

#? Imports for files defined by Project Vigilant:
from data_collection.data_collection_main import *      #? Import the Primary Data Collection Script
from data_preparation.data_preparation_main import *    #? Import the Primary Data Preparation Script
from data_storage.data_storage_main import *            #? Import the Primary Data Storage Script

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------

#* -------------------------------------------
#*  DATA COLLECTION DICTIONARY
#* -------------------------------------------
#? This dictionary is used to store all the gathered metrics from the data_collection scripts
#? It is stored as unedited, and uncleaned data. It will be sent to the data_cleaning scripts.
#? Following this the data will be sent to the data_storage scripts and on to Redis
metrics_dictionary = {
    "cpu_usage"     : "--", 
    "memory_usage"  : "--",
    "disk_space"    : "--",
    "throughput"    : "--",
    "latency"       : "--",
    "connection"    : "--",
    "load_average"  : "--",
    "response_time" : "--",
    "system_uptime" : "--",
    "timestamp"     : "--"
}

#* -------------------------------------------
#* DASHBOARD DISPLAY DISCTIONARY
#* -------------------------------------------
#? This dictiojary is used to store all the collected data after cleaning/preparation. This
#? dictionary data is heavily edited and expanded so that is can be stored in a Redis Cache
#? (for use with AWS) and also for a PostgresSQL Schema (for Grafana prior to Cloud Launch)
prepared_dictionary = {
    'cpu_usage_1mi'          : "--",
    'cpu_usage_5mi'          : "--",
    'cpu_usage_15mi'         : "--",
    'memory_total'           : "--",
    'memory_used'            : "--",
    'memory_free'            : "--",
    'memory_percent_used'    : "--",
    'disk_space_total'       : "--",
    'disk_space_used'        : "--",
    'disk_space_free'        : "--",
    'disk_space_percent_used': "--",
    'network_connection'     : "--",
    'network_latency'        : "--",
    'network_throughput_rx'  : "--",
    'network_throughput_tx'  : "--",
    'perf_load_avg_1mi'      : "--",
    'perf_load_avg_5mi'      : "--",
    'perf_load_avg_15mi'     : "--",
    'perf_response_time'     : "--",
    'perf_uptime_users'      : "--",
    'timestamp'              : "--"
}


#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    The 'init_data_handling' function is used to begin a data handling cycle which consists of three
    steps. First, data collection, Second, data preparation, and Third data storage. 
"""
def init_data_handling(iteration_counter):

    print("\tBegin Project Vigilant - Data Handling Cycle.")

    #? Update the metrics dictionary with the current timestamp
    metrics_dictionary["timestamp"] = get_current_timestamp()

    #? Step 1: Initialize data collection, which populates the metrics_dictionary
    init_data_collection(metrics_dictionary)
    print("\t\tData Successfully Collected.\n")
    time.sleep(0.5)

    #? Step 2: Initialize data preparation, which processes and prepares data for storage
    init_data_preparation(metrics_dictionary, prepared_dictionary)
    print("\t\tData Succesfully Prepared.\n")
    time.sleep(2)

    #? Step 3: Initialize data storage, which stores the prepared data in a database
    init_data_storage(prepared_dictionary, iteration_counter)
    print("\t\tData Successfully Stored.\n\n")
    time.sleep(0.5)

    #print("\n\n\n")
    #for key, value in prepared_dictionary.items():
    #    print(f'{key}: {value}')

"""
    Simple function to obtain the current date and time so that each data handling cycle can be distinguished
    according top date and time.
"""
def get_current_timestamp():
    current_time = datetime.datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S.%f')


"""
    This function simply allows outside files to access the data dictionary
"""
def get_prepared_data():
    return prepared_dictionary