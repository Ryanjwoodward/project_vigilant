
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
#   DATE            |       September 11, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       data_collection_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file serves as the access point to all data collection processes and scripts
#                   |       
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------


#? Imports for Files Defined by Project Vigilant
from data_collection.metrics_system_resources import *    #? Import all functions to obtain System Resource Usage Metrics
from data_collection.metrics_network import *             #? Import all functions to obtain Networn Metrics
from data_collection.metrics_performance import *         #? Import all functions to obtain Performance Metrics  

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
     The init_data_collection function serves as a data collection mechanism that assembles a 
     comprehensive set of system and network metrics and stores them in a given dictionary called 
     metrics_dictionary. 
"""
def init_data_collection(metrics_dictionary):
    print("\t\tInitiating Data Collection.")

    #? Obtain System Resource Usage Metrics
    metrics_dictionary["cpu_usage"] = get_cpu_usage()
    metrics_dictionary["memory_usage"] = get_memory_usage()
    target_partition = "/dev/sda5"
    metrics_dictionary["disk_space"] = get_disk_space_metrics(target_partition)

    #? Obtain Network Metrics
    metrics_dictionary["throughput"] = get_network_throughput()
    metrics_dictionary["connection"] = is_internet_connected()
    metrics_dictionary["latency"] = get_network_latency('google.com')

    #? Obtain Performance Metrics
    metrics_dictionary["system_uptime"] = get_uptime()
    metrics_dictionary["load_average"] = get_load_average()
    metrics_dictionary["response_time"] = get_response_time('http://google.com')

