
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
                                       _   _                            _                      _                  
  _ __  _ __ ___ _ __   __ _ _ __ __ _| |_(_) ___  _ __      _ __   ___| |___      _____  _ __| | __  _ __  _   _ 
 | '_ \| '__/ _ \ '_ \ / _` | '__/ _` | __| |/ _ \| '_ \    | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / | '_ \| | | |
 | |_) | | |  __/ |_) | (_| | | | (_| | |_| | (_) | | | |   | | | |  __/ |_ \ V  V / (_) | |  |   < _| |_) | |_| |
 | .__/|_|  \___| .__/ \__,_|_|  \__,_|\__|_|\___/|_| |_|___|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_) .__/ \__, |
 |_|            |_|                                    |_____|                                       |_|    |___/ 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 27, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       data_collection_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file contains all the data preparation functions for metrics pertaining to Network 
#                   |       This file is meant to be accessed, only, by data preparation script.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    The prepare_throughput_data function is designed to process a dictionary containing network throughput data. 
    It checks if both 'sent_bytes_per_sec' and 'received_bytes_per_sec' keys are present in the provided 
    throughput_data dictionary. If both keys are found, the function extracts and returns the associated values, 
    representing the rate of data transmission in bytes per second for sent and received data, respectively. 
    However, if either key is missing, it raises a ValueError with an appropriate error message.
"""
def prepare_throughput_data(throughput_data):
    if 'sent_bytes_per_sec' in throughput_data and 'received_bytes_per_sec' in throughput_data:
        sent_bytes_per_sec = throughput_data['sent_bytes_per_sec']
        received_bytes_per_sec = throughput_data['received_bytes_per_sec']
        return sent_bytes_per_sec, received_bytes_per_sec
    else:
        raise ValueError("The throughput_data dictionary should contain 'sent_bytes_per_sec' and 'received_bytes_per_sec' keys.")


"""
    The prepare_latency_data function simply accepts a float value from the metric dictionary and then converts it to float so
    the data in milliseconds is displayed without a decimal point.
"""
def prepare_latency_data(latency_data):
    return int(latency_data)



"""
    The prepare_connection_data function simple checks if the value of the network connection test is True or False
    If True the function returns 'yes' (meaning there is network connection) otherwise it returns 'no' (meaning there 
    is no network connection)
"""
def prepare_connection_data(connection_data):   
    if (connection_data):
        return 'yes'
    else:
        return 'no'