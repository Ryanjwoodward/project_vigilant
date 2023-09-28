
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
                                       _   _                               _                                                                               
  _ __  _ __ ___ _ __   __ _ _ __ __ _| |_(_) ___  _ __      ___ _   _ ___| |_ ___ _ __ ___      _ __ ___  ___  ___  _   _ _ __ ___ ___  ___   _ __  _   _ 
 | '_ \| '__/ _ \ '_ \ / _` | '__/ _` | __| |/ _ \| '_ \    / __| | | / __| __/ _ \ '_ ` _ \    | '__/ _ \/ __|/ _ \| | | | '__/ __/ _ \/ __| | '_ \| | | |
 | |_) | | |  __/ |_) | (_| | | | (_| | |_| | (_) | | | |   \__ \ |_| \__ \ ||  __/ | | | | |   | | |  __/\__ \ (_) | |_| | | | (_|  __/\__ \_| |_) | |_| |
 | .__/|_|  \___| .__/ \__,_|_|  \__,_|\__|_|\___/|_| |_|___|___/\__, |___/\__\___|_| |_| |_|___|_|  \___||___/\___/ \__,_|_|  \___\___||___(_) .__/ \__, |
 |_|            |_|                                    |_____|   |___/                     |_____|                                            |_|    |___/ 
                            
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 27, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       data_collection_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file contains all the data preparation functions for metrics pertaining to System Resource Usage
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
    The prepare_cpu_usage_data function is designed to process a list containing CPU usage values. 
    It first checks if the input list contains exactly three elements to ensure it has the expected 
    structure. Then, it extracts and converts these values to floating-point numbers
"""
def prepare_cpu_usage_data(cpu_usage_list):
    #? Ensure that cpu_usage_list contains three elements
    if len(cpu_usage_list) != 3:
        raise ValueError("cpu_usage_list should contain exactly three values")

    #? Extract and convert the values to floats
    value1 = float(cpu_usage_list[0])
    value2 = float(cpu_usage_list[1])
    value3 = float(cpu_usage_list[2])

    #? Return the extracted and converted CPU usage values
    return value1, value2, value3



"""
    The prepare_memory_usage_data function is designed to process a dictionary containing memory 
    usage data. It checks if the required keys ('total_memory_mb', 'used_memory_mb', and 'free_memory_mb') 
    are present in the dictionary. If these keys are found, it extracts the individual memory usage values. 
    Additionally, it calculates the percentage of free memory and formats it as an integer. 
"""
def prepare_memory_usage_data(memory_usage_dict):
    #? Check if the required keys are present in the memory_usage_dict
    if 'total_memory_mb' not in memory_usage_dict or 'used_memory_mb' not in memory_usage_dict or 'free_memory_mb' not in memory_usage_dict:
        raise ValueError("memory_usage_dict should contain 'total_memory_mb', 'used_memory_mb', and 'free_memory_mb' keys")

    #? Extract individual memory usage values from the dictionary
    total_memory = memory_usage_dict['total_memory_mb']
    used_memory = memory_usage_dict['used_memory_mb']
    free_memory = memory_usage_dict['free_memory_mb']

    #? Calculate the percentage of free memory and format it as an integer
    percent_free = ((free_memory / total_memory) * 100)

    #? Return the extracted values along with the formatted percentage
    return total_memory, used_memory, free_memory, "{:.0f}".format(percent_free)



"""
    The prepare_disk_space_data function is designed to extract specific disk space usage values 
    ('total', 'used', 'free', and 'percent_used') from a list of dictionaries. It checks if the 
    input list is not empty and assumes there is only one dictionary in the list. If the extracted 
    dictionary contains the required keys, it extracts and returns these values individually. 
"""
def prepare_disk_space_data(disk_space_list):
    #? Check if the input list is empty
    if not disk_space_list:
        raise ValueError("disk_space_list is empty")

    #? Assuming there is only one dictionary in the list, extract it
    disk_space_dict = disk_space_list[0]

    #? Check if the extracted dictionary contains the required keys
    if 'total' not in disk_space_dict or 'used' not in disk_space_dict or 'free' not in disk_space_dict or 'percent_used' not in disk_space_dict:
        raise ValueError("disk_space_dict should contain 'total', 'used', 'free', and 'percent_used' keys")

    #? Extract individual values from the dictionary
    total = round(disk_space_dict['total'] / (1024 ** 3))  #? Convert bytes to gigabytes
    used = round(disk_space_dict['used'] / (1024 ** 3))    #? Convert bytes to gigabytes 
    free = round(disk_space_dict['free'] / (1024 ** 3))    #? Convert bytes to gigabytes

    percent_used = int(round(disk_space_dict['percent_used']))

    #? Return the extracted values
    return total, used, free, percent_used