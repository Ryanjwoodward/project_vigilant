"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
            _                                                            _                     
  _ __ ___ | |     _ __  _ __ ___   ___ ___  ___ ___     _ __ ___   __ _(_)_ __    _ __  _   _ 
 | '_ ` _ \| |    | '_ \| '__/ _ \ / __/ _ \/ __/ __|   | '_ ` _ \ / _` | | '_ \  | '_ \| | | |
 | | | | | | |    | |_) | | | (_) | (_|  __/\__ \__ \   | | | | | | (_| | | | | |_| |_) | |_| |
 |_| |_| |_|_|____| .__/|_|  \___/ \___\___||___/___/___|_| |_| |_|\__,_|_|_| |_(_) .__/ \__, |
            |_____|_|                              |_____|                        |_|    |___/ 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 29, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       ml_processes_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file serves as the entry point to all Machine Learning Operations. Such as Data Cleaning, 
#                   |       Model definition, Model Training, Predictive Analysis, etc.
#                   |   
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
    
    get data keys 0-100 from redis and store them in dictionaries
        these ought to be seprated by key and then the old dictionary is overwrittent to save space
        the important key_value pairs are: CPU Usage, load average, and throughput

    traing the model using the specific dictionaries

    predict the next value regarding the cpu usage, load average, and thre throughput.

    save the predicted values (with the current timestamp) to postgres table, 
        this is a new table, it can have rows for each cpu, load average, and throughput predictions
        then add these new predicted values to the Grafana visualizations

    FINALLY: DEPLOY TO CLOUD!


 """