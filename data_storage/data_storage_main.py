
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
      _       _                _                                                 _                     
   __| | __ _| |_ __ _     ___| |_ ___  _ __ __ _  __ _  ___     _ __ ___   __ _(_)_ __    _ __  _   _ 
  / _` |/ _` | __/ _` |   / __| __/ _ \| '__/ _` |/ _` |/ _ \   | '_ ` _ \ / _` | | '_ \  | '_ \| | | |
 | (_| | (_| | || (_| |   \__ \ || (_) | | | (_| | (_| |  __/   | | | | | | (_| | | | | |_| |_) | |_| |
  \__,_|\__,_|\__\__,_|___|___/\__\___/|_|  \__,_|\__, |\___|___|_| |_| |_|\__,_|_|_| |_(_) .__/ \__, |
                     |_____|                      |___/    |_____|                        |_|    |___/ 
                    
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 27, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       data_storage_main.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file serves as the access point to all data storage processes and scripts
#                   |       This file is meant to be accessed, only, from the data_handling_main script.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""



#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import time

#? Imports for files defined by Project Vigilant:
from data_storage.data_storage_redis import *       #? Import for storing data in Redis Caches
from data_storage.data_storage_postgres import *    #? Import for storing data in PostGres SQL Schema

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    The init_data_storage function is designed to initialize data storage by storing prepared data in both Redis and PostgreSQL databases. 
    It takes two parameters: prepared_data, which is the data to be stored, and data_key, which is used to store data in Redis.
    First, it calls the store_data_in_redis function to store the prepared data in Redis using the provided data key.
    Then, it establishes a connection to the PostgreSQL database using the specified connection parameters (host, database, username, and password).
    Next, it defines the schema name (project_vigilant_schema) and table name (collected_data_metrics) within the PostgreSQL database where the data will be stored.
    Finally, it calls the store_data_in_postgres function to insert the prepared data into the PostgreSQL database within the specified schema and table. 
    This function enables data to be stored in both Redis and PostgreSQL databases, facilitating data storage and retrieval for the project.
"""
def init_data_storage(prepared_data, data_key):

    print("\t\tInitiating Data Storage.")

    #? Store prepared data in Redis using the specified data key
    store_data_in_redis(prepared_data, data_key)
    time.sleep(2)

    #? Store the prepared data in the PostgreSQL database within the specified schema and table
    store_data_in_postgres(prepared_data)




