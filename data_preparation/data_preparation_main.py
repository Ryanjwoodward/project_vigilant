
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
      _       _                     _ _           _   _                                 _             
   __| | __ _| |_ __ _     ___ ___ | | | ___  ___| |_(_) ___  _ __      _ __ ___   __ _(_)_ __    ___ 
  / _` |/ _` | __/ _` |   / __/ _ \| | |/ _ \/ __| __| |/ _ \| '_ \    | '_ ` _ \ / _` | | '_ \  / __|
 | (_| | (_| | || (_| |  | (_| (_) | | |  __/ (__| |_| | (_) | | | |   | | | | | | (_| | | | | || (__ 
  \__,_|\__,_|\__\__,_|___\___\___/|_|_|\___|\___|\__|_|\___/|_| |_|___|_| |_| |_|\__,_|_|_| |_(_)___|
                     |_____|                                      |_____|                             
                                
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 27, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       data_collection_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file serves as the access point to all data preparation processes and scripts
#                   |       
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

#? Imports for files defined by Project Vigilant:
from data_preparation.preparation_system_resources import *   #? Import all functions for preparing System Resources Data
from data_preparation.preparation_network import *            #? Import all functions for preparing Network Data
from data_preparation.preparation_performance import *        #? Import all functions for preparing Performance Data

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
     The init_data_preparation function serves as a data preparation mechanism that calls the functions that reformat, organize, and segregate
     the data in a way that makes it useful to store in a Redis Cache and a PostgresSQL Schema.
"""
def init_data_preparation(dirty_data_dict, clean_data_dict):
    print("\t\tInitiating Data Preparation.")

    #? Prepare System Resource Usage Data
    clean_data_dict['cpu_usage_1mi'], clean_data_dict['cpu_usage_5mi'], clean_data_dict['cpu_usage_15mi'] = prepare_cpu_usage_data(dirty_data_dict['cpu_usage']) 
    clean_data_dict['memory_total'], clean_data_dict['memory_used'],clean_data_dict['memory_free'],clean_data_dict['memory_percent_used'] = prepare_memory_usage_data(dirty_data_dict['memory_usage']) 
    clean_data_dict['disk_space_total'], clean_data_dict['disk_space_used'], clean_data_dict['disk_space_free'], clean_data_dict['disk_space_percent_used'] = prepare_disk_space_data(dirty_data_dict['disk_space'])
 
    #? Prepare Network Data
    clean_data_dict['network_throughput_tx'], clean_data_dict['network_throughput_rx'] = prepare_throughput_data(dirty_data_dict['throughput'])
    clean_data_dict['network_latency'] = prepare_latency_data(dirty_data_dict['latency'])
    clean_data_dict['network_connection'] = prepare_connection_data(dirty_data_dict['connection'])
    
    #? Prepare Performance Data
    clean_data_dict['perf_load_avg_1mi'], clean_data_dict['perf_load_avg_5mi'], clean_data_dict['perf_load_avg_15mi'] = prepare_load_average_data(dirty_data_dict['load_average'])
    clean_data_dict['perf_response_time'] = prepare_response_time_data(dirty_data_dict['response_time'])
    clean_data_dict['perf_uptime_users'] = prepare_uptime_users_data(dirty_data_dict['system_uptime']) 

    #? Insert the time stamp in the dictionary with data prepared
    clean_data_dict['timestamp'] = dirty_data_dict['timestamp']
