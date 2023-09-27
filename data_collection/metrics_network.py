"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            

                 _        _                            _                                                                               
  _ __ ___   ___| |_ _ __(_) ___ ___     ___ _   _ ___| |_ ___ _ __ ___      _ __ ___  ___  ___  _   _ _ __ ___ ___  ___   _ __  _   _ 
 | '_ ` _ \ / _ \ __| '__| |/ __/ __|   / __| | | / __| __/ _ \ '_ ` _ \    | '__/ _ \/ __|/ _ \| | | | '__/ __/ _ \/ __| | '_ \| | | |
 | | | | | |  __/ |_| |  | | (__\__ \   \__ \ |_| \__ \ ||  __/ | | | | |   | | |  __/\__ \ (_) | |_| | | | (_|  __/\__ \_| |_) | |_| |
 |_| |_| |_|\___|\__|_|  |_|\___|___/___|___/\__, |___/\__\___|_| |_| |_|___|_|  \___||___/\___/ \__,_|_|  \___\___||___(_) .__/ \__, |
                                   |_____|   |___/                     |_____|                                            |_|    |___/ 
                               
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 20, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       metrics_network.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file contains all the data collection functions for metrics pertaining to Network
#                   |       (i.e Throughput). This file meant to accessed, only, by the data collection script.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import subprocess
import psutil
import time
import requests


#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------


"""
    The get_network_throughput function measures the network throughput of a system by 
    calculating the rate at which data is sent and received over the network. It does this 
    by first recording the network data counters, waiting for a brief moment (e.g., 1 second), 
    and then recording the counters again. The difference in the number of bytes sent and received 
    between the two measurements is used to calculate the network throughput in bytes per second. 
    The function returns a dictionary containing two key-value pairs: "sent_bytes_per_sec," which 
    represents the rate of bytes sent per second, and "received_bytes_per_sec," which represents the 
    rate of bytes received per second. If any exceptions occur during the process, it returns an 
    error message as a string. 
"""
def get_network_throughput():
    try:
        #? Initialize network counters
        net_counters1 = psutil.net_io_counters()
        
        #? Wait for a moment (e.g., 1 second)
        time.sleep(1)
        
        #? Get network counters again
        net_counters2 = psutil.net_io_counters()
        
        #? Calculate network throughput in bytes per second
        sent_bytes_per_sec = net_counters2.bytes_sent - net_counters1.bytes_sent
        received_bytes_per_sec = net_counters2.bytes_recv - net_counters1.bytes_recv
        
        return {
            "sent_bytes_per_sec": sent_bytes_per_sec,
            "received_bytes_per_sec": received_bytes_per_sec,
        }
    except Exception as e:
        return str(e)


"""
    The get_network_latency function measures the network latency, specifically the round-trip time, between 
    the current system and a specified host using the ping command. It does this by running the ping command 
    with a default count of 4 packets (or as specified by the count parameter) to the given host, capturing the 
    command's output, and then parsing that output to extract the round-trip time (latency) information. The 
    function returns the calculated latency as a floating-point number, representing the time in milliseconds. 
    In case of any exceptions during the ping command execution or parsing process, it returns an error message 
    as a string. 
"""
def get_network_latency(host, count=4):
    try:
        #? Run the ping command and capture the output
        result = subprocess.check_output(["ping", "-c", str(count), host])

        #? Decode the output and split lines
        output = result.decode("utf-8").split('\n')

        #? Extract the last line containing the summary statistics
        summary_line = output[-2]

        #? Extract the round-trip time (latency) from the summary line
        latency = float(summary_line.split("/")[-2])

        return latency
    
    except Exception as e:
        return str(e)


"""
    The is_internet_connected function checks whether the local system is connected to the internet. It does this 
    by attempting to send a GET request to a well-known and reliable server, in this case, "https://www.google.com." 
    The function uses the requests library to perform the request with a timeout of 5 seconds. If the response status 
    code received is 200, it indicates that the request was successful, and the function returns True, signifying that 
    the system is connected to the internet. In the event of a requests.ConnectionError exception, which is raised when 
    there is no internet connection or when the request to Google's server fails for some reason, the function returns False.
"""
def is_internet_connected():
    try:
        #? Attempt to send a GET request to a well-known, reliable server (e.g., google.com)
        response = requests.get("https://www.google.com", timeout=5)
        
        #? If the response status code is 200, it means the request was successful, and you are connected to the internet.
        return response.status_code == 200
    
    except requests.ConnectionError:
        #? A ConnectionError is raised if there is no internet connection.
        return False