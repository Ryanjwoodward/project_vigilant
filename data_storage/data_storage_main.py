
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
      _       _            _                     _ _ _                                 _                     
   __| | __ _| |_ __ _    | |__   __ _ _ __   __| | (_)_ __   __ _     _ __ ___   __ _(_)_ __    _ __  _   _ 
  / _` |/ _` | __/ _` |   | '_ \ / _` | '_ \ / _` | | | '_ \ / _` |   | '_ ` _ \ / _` | | '_ \  | '_ \| | | |
 | (_| | (_| | || (_| |   | | | | (_| | | | | (_| | | | | | | (_| |   | | | | | | (_| | | | | |_| |_) | |_| |
  \__,_|\__,_|\__\__,_|___|_| |_|\__,_|_| |_|\__,_|_|_|_| |_|\__, |___|_| |_| |_|\__,_|_|_| |_(_) .__/ \__, |
                     |_____|                                 |___/_____|                        |_|    |___/                          
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

import redis

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
    The store_data_in_redis function is designed to store prepared data in a Redis database. It takes two parameters: 
    prepared_data, which is the data to be stored, and data_key, which is used to construct the Redis key under which 
    the data will be stored. The function first constructs a Redis key by appending the data_key to a template key named 
    "vigilant_set." It then establishes a connection to a specific Redis instance with the provided connection details, 
    including the host, port, password, and database name. Finally, it uses the hmset method to set the prepared_data as 
    a hash in Redis under the constructed Redis key.
"""
def store_data_in_redis(prepared_data, data_key):

    key_template = "vigilant_set"
    redis_data_key = key_template + str(data_key)

    print(f"\n\n\nHERE: {redis_data_key}\n\n\n")

    #? Redis connection details
    redis_host = '<host name here>'
    redis_port = 18635  # The port number for your Redis instance
    redis_password = '<password here>'  # Replace with your Redis password if required
    redis_db_name = '<name of database here>'  # Your Redis database name

    #? Connect to Redis
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, db=0, decode_responses=True)



    #? Set the dictionary in Redis with a specific key
    r.hmset(redis_data_key, prepared_data)


