
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
                                       _   _                                   __                                                         
  _ __  _ __ ___ _ __   __ _ _ __ __ _| |_(_) ___  _ __       _ __   ___ _ __ / _| ___  _ __ _ __ ___   __ _ _ __   ___ ___   _ __  _   _ 
 | '_ \| '__/ _ \ '_ \ / _` | '__/ _` | __| |/ _ \| '_ \     | '_ \ / _ \ '__| |_ / _ \| '__| '_ ` _ \ / _` | '_ \ / __/ _ \ | '_ \| | | |
 | |_) | | |  __/ |_) | (_| | | | (_| | |_| | (_) | | | |    | |_) |  __/ |  |  _| (_) | |  | | | | | | (_| | | | | (_|  __/_| |_) | |_| |
 | .__/|_|  \___| .__/ \__,_|_|  \__,_|\__|_|\___/|_| |_|____| .__/ \___|_|  |_|  \___/|_|  |_| |_| |_|\__,_|_| |_|\___\___(_) .__/ \__, |
 |_|            |_|                                    |_____|_|                                                             |_|    |___/ 

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

import re

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    The prepare_load_average_data function is designed to process a dictionary containing load average values. 
    It checks if all three keys ('1-minute', '5-minute', and '15-minute') are present in the provided 
    load_average_data dictionary. If all keys are found, the function extracts and returns the associated values, 
    representing the load averages for different time periods (1-minute, 5-minute, and 15-minute). If any of the keys 
    are missing, it raises a ValueError with an appropriate error message. 
"""
def prepare_load_average_data(load_average_data):
    #? Check if '1-minute', '5-minute', and '15-minute' keys are present in the dictionary
    if '1-minute' in load_average_data and '5-minute' in load_average_data and '15-minute' in load_average_data:
        #? Extract the values associated with these keys
        value1 = load_average_data['1-minute']
        value2 = load_average_data['5-minute']
        value3 = load_average_data['15-minute']
        return value1, value2, value3
    else:
        #? Raise a ValueError if any of the keys is missing
        raise ValueError("The load_average_data dictionary should contain '1-minute', '5-minute', and '15-minute' keys.")


"""

"""
def prepare_response_time_data(response_time_data):
    #? Round the response time to the nearest ones place and convert it to an integer
    formatted_response_time = int(round(response_time_data))
    return formatted_response_time

"""

"""
def prepare_uptime_users_data(uptime_data):
    try:
        # Split the uptime_data using whitespace as the delimiter
        data_parts = uptime_data.split()

        # Extract the number of users
        user_count_index = data_parts.index("user,")
        user_count = int(data_parts[user_count_index - 1])

        return user_count
    except Exception as e:
        return str(e)
    

def prepare_uptime_duration_data(up_time_str):
    # Use regular expressions to extract the uptime duration
    duration_match = re.search(r'up\s+((\d+) day)?\s*((\d+):(\d+))', up_time_str)
    
    if duration_match:
        days = int(duration_match.group(2)) if duration_match.group(2) else 0
        hours = int(duration_match.group(4)) if duration_match.group(4) else 0
        mins = int(duration_match.group(5)) if duration_match.group(5) else 0
    else:
        days, hours, mins = 0, 0, 0
    
    total_minutes = days * 24 * 60 + hours * 60 + mins
    return f"{total_minutes // 60:02d}:{total_minutes % 60:02d}"

    

