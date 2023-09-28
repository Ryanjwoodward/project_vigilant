"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
      _       _                _                                                  _                                    
   __| | __ _| |_ __ _     ___| |_ ___  _ __ __ _  __ _  ___      _ __   ___  ___| |_ __ _ _ __ ___  ___   _ __  _   _ 
  / _` |/ _` | __/ _` |   / __| __/ _ \| '__/ _` |/ _` |/ _ \    | '_ \ / _ \/ __| __/ _` | '__/ _ \/ __| | '_ \| | | |
 | (_| | (_| | || (_| |   \__ \ || (_) | | | (_| | (_| |  __/    | |_) | (_) \__ \ || (_| | | |  __/\__ \_| |_) | |_| |
  \__,_|\__,_|\__\__,_|___|___/\__\___/|_|  \__,_|\__, |\___|____| .__/ \___/|___/\__\__, |_|  \___||___(_) .__/ \__, |
                     |_____|                      |___/    |_____|_|                 |___/                |_|    |___/ 
                  
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       September 11, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       data_storage_postgres.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file is used to store the collected and cleaned data in a PostGres SQL Database. This 
#                   |       file is meant to be accessed, only, by the data_storage_main file.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


#*-----------------------------------------------------------------------------------------
#*                                        IMPORTS
#*-----------------------------------------------------------------------------------------

import psycopg2
from psycopg2 import sql

#*-----------------------------------------------------------------------------------------
#*                                    GLOBAL VARIABLES
#*-----------------------------------------------------------------------------------------



#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

"""
      The store_data_in_postgres function accepts a database connection, a dataset (data), a schema name, 
      and a table name as parameters. It is designed to insert data into a specified PostgreSQL table within 
      a given schema. The function uses a cursor to execute an SQL INSERT query, inserting the provided data 
      into the specified schema and table. If the data insertion is successful, it commits the transaction 
      and prints a success message. If an error occurs during insertion, it prints an error message with details
      of the exception.
"""
def store_data_in_postgres(connection, data, schema_name, table_name):
    try:
        #? Create a cursor object for database interaction
        cursor = connection.cursor()
        
        #? Define the SQL query for inserting data into a specified schema and table
        insert_query = f"""
            INSERT INTO {schema_name}.{table_name} (
                cpu_usage_1mi,
                cpu_usage_5mi,
                cpu_usage_15mi,
                memory_total,
                memory_used,
                memory_free,
                memory_percent_used,
                disk_space_total,
                disk_space_used,
                disk_space_free,
                disk_space_percent_used,
                network_connection,
                network_latency,
                network_throughput_rx,
                network_throughput_tx,
                perf_load_avg_1mi,
                perf_load_avg_5mi,
                perf_load_avg_15mi,
                perf_response_time,
                perf_uptime_users,
                timestamp
            ) VALUES (
                %(cpu_usage_1mi)s,
                %(cpu_usage_5mi)s,
                %(cpu_usage_15mi)s,
                %(memory_total)s,
                %(memory_used)s,
                %(memory_free)s,
                %(memory_percent_used)s,
                %(disk_space_total)s,
                %(disk_space_used)s,
                %(disk_space_free)s,
                %(disk_space_percent_used)s,
                %(network_connection)s,
                %(network_latency)s,
                %(network_throughput_rx)s,
                %(network_throughput_tx)s,
                %(perf_load_avg_1mi)s,
                %(perf_load_avg_5mi)s,
                %(perf_load_avg_15mi)s,
                %(perf_response_time)s,
                %(perf_uptime_users)s,
                %(timestamp)s
            )
        """

        #? Execute the SQL query with the provided data
        cursor.execute(insert_query, data)
        
        #? Commit the transaction to save the data in the database
        connection.commit()
        
        #? Close the cursor
        cursor.close()
        
        print("Data inserted successfully.")
    except Exception as e:
        #? Handle exceptions and print an error message if insertion fails
        print(f"Error inserting data: {e}")
