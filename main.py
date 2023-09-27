
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
                  _                     
  _ __ ___   __ _(_)_ __    _ __  _   _ 
 | '_ ` _ \ / _` | | '_ \  | '_ \| | | |
 | | | | | | (_| | | | | |_| |_) | |_| |
 |_| |_| |_|\__,_|_|_| |_(_) .__/ \__, |
                           |_|    |___/ 
                    
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 11, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file is the entry point into the Project Vigilant application. From this file all other
#                   |       process and operations are called.
#                   |
#                   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import time
import subprocess

#? Imports for files Defined By Project Vigilant:
from data_handling_main import *
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
}



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------




#*-----------------------------------------------------------------------------------------
#*                                      ENTRY POINT
#*-----------------------------------------------------------------------------------------
try:

    while True:
        print("Calling Data handling Main.")
        init_data_handling(metrics_dictionary)

        print("\n\n********************\n Metrics Dictionary \n********************")
        for key, value in metrics_dictionary.items():
            print(f"{key}: {value}")

       
        time.sleep(5)

except KeyboardInterrupt:
    print("\nCtrl+C detected. Exiting Program... Auf Wiedersehen!")
