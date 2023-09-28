
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

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------

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
    'perf_uptime_duration'   : "--", 
    'perf_uptime_users'      : "--",
    'timestamp'              : "--"
}

#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""

"""
def init_data_handling():
    print("STARTING - Data Handling")

    metrics_dictionary["timestamp"] = get_current_timestamp()

    init_data_collection(metrics_dictionary)
    time.sleep(3)

    #print("\n\n********************\n Metrics Dictionary dh_main\n********************")
    #for key, value in metrics_dictionary.items():
        #print(f"{key}: {value}")

    init_data_preparation(metrics_dictionary, prepared_dictionary)

    print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n Clean Dictionary dh_main\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    for key, value in  prepared_dictionary.items():
        print(f"{key}: {value}")

"""

"""
def get_current_timestamp():
    current_time = datetime.datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
