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
#   DESCRIPTION     |       This file contains all the data collection functions for metrics pertaining to Server Performance
#                   |       (i.e Uptime, Load Average). This file meant to accessed, only, by the data collection script.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import subprocess
import time
import requests
import os

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    The get_load_average function retrieves the system load averages for the 1-minute, 5-minute, 
    and 15-minute intervals. It uses the os.getloadavg() function to obtain these load averages, 
    which are returned as a tuple. The function then structures this data into a dictionary, 
    making it easier to access each load average individually. In case of any OSError that may 
    occur while attempting to retrieve the load averages, the function prints an error message 
    and returns None. 
"""
def get_load_average():
    try:
        load_avg = os.getloadavg()
        #? The function os.getloadavg() returns a tuple of 3 load averages (1-minute, 5-minute, and 15-minute).
        #? You can access them individually or return the entire tuple based on your needs.
        return {
            "1-minute": load_avg[0],
            "5-minute": load_avg[1],
            "15-minute": load_avg[2]
        }
    except OSError as e:
        #? Handle any OSError that may occur when trying to obtain the load average.
        print(f"Error: {e}")
        return None


"""
    The get_uptime function retrieves and returns the system's uptime information using the uptime 
    command on a Unix-like system. It executes the uptime command, captures its output as a string, 
    and then returns this uptime information. In the event of any errors or exceptions occurring during 
    the execution process, the function returns an error message as a string.
"""
def get_uptime():
    try:
        result = subprocess.check_output(["uptime"])
        uptime_info = result.decode("utf-8").strip()
        return uptime_info
    except Exception as e:
        return str(e)
    

"""
    The get_response_time function measures the response time of a web request to a specified URL. 
    It starts by recording the current time, sends an HTTP GET request to the provided url using the 
    requests.get() function, and then records the time again when the response is received. If the 
    response status code is 200 (indicating a successful request), the function calculates the response 
    time in milliseconds by subtracting the start time from the end time and then multiplying the result by 
    1000. It returns this response time. In case of any exceptions during the HTTP request or response 
    processing, it prints an error message and returns None.
"""
def get_response_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            response_time_ms = (end_time - start_time) * 1000  #? Convert to milliseconds
            return response_time_ms
        else:
            print(f"HTTP request failed with status code {response.status_code}")
            return None

    except Exception as e:
        #? Handle any exceptions that may occur during the request.
        print(f"Error: {e}")
        return None
