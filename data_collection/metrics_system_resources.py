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
#   DATE            |       September 11, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       metrics_system_resources.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file contains all the data collection functions for metrics pertaining to System Resource Usage
#                   |       (i.e CPU and Memory). This file meant to accessed, only, by the data collection script.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""



#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import subprocess
import psutil

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    The get_cpu_usage function retrieves and parses system load averages, which can provide 
    insights into CPU usage over a period of time, from the uptime command on a Unix-like 
    system. It runs the uptime command, captures its output, and then processes the output to 
    extract the load averages. The function returns these load averages as a list. In case of 
    any errors or exceptions during the process, it returns an error message as a string.
"""
def get_cpu_usage():
    try:
        result = subprocess.check_output(["uptime"])
        uptime_info = result.decode("utf-8").strip()
        # Extract CPU load averages from uptime output
        load_averages = uptime_info.split("load average:")[1].split(",")
        return load_averages
    except Exception as e:
        return str(e)


"""
    The get_memory_usage function retrieves memory usage information from a Unix-like system 
    using the free command. It executes the free -m command to obtain memory statistics, captures 
    the output, and then parses it to extract the total, used, and free memory values in megabytes 
    (MB). The function returns this information as a dictionary with keys "total_memory_mb," 
    "used_memory_mb," and "free_memory_mb." In the event of any errors or exceptions during the 
    execution or parsing process, it returns an error message as a string.
"""
def get_memory_usage():
    try:
        result = subprocess.check_output(["free", "-m"])
        memory_info = result.decode("utf-8").split("\n")[1]
        total, used, free, *_ = map(int, memory_info.split()[1:])
        return {
            "total_memory_mb": total,
            "used_memory_mb": used,
            "free_memory_mb": free,
        }
    except Exception as e:
        return str(e)


"""
    The get_disk_space_metrics function collects disk space metrics for a specified target partition 
    on a system. It first obtains a list of all disk partitions using the psutil.disk_partitions() function. 
    Then, it iterates through the list to find the partition that matches the provided target_partition. 
    For the matching partition, it retrieves disk space usage information, including total, used, free space, 
    and the percentage of space used, using psutil.disk_usage(partition.mountpoint). The function returns 
    this information as a list of dictionaries, with each dictionary containing details about the target 
    partition's disk space metrics, such as device name, mount point, total space, used space, free space, 
    and the percentage of space used.
"""
def get_disk_space_metrics(target_partition):
    partitions = psutil.disk_partitions()
    disk_metrics = []

    for partition in partitions:
        if partition.device == target_partition:
            usage = psutil.disk_usage(partition.mountpoint)
            metrics = {
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent_used": usage.percent
            }
            disk_metrics.append(metrics)

    return disk_metrics


