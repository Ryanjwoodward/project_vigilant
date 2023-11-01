"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
            _                         _ _      _           _        _       _                _                                           
  _ __ ___ | |     _ __  _ __ ___  __| (_) ___| |_ ___  __| |    __| | __ _| |_ __ _     ___| |_ ___  _ __ __ _  __ _  ___   _ __  _   _ 
 | '_ ` _ \| |    | '_ \| '__/ _ \/ _` | |/ __| __/ _ \/ _` |   / _` |/ _` | __/ _` |   / __| __/ _ \| '__/ _` |/ _` |/ _ \ | '_ \| | | |
 | | | | | | |    | |_) | | |  __/ (_| | | (__| ||  __/ (_| |  | (_| | (_| | || (_| |   \__ \ || (_) | | | (_| | (_| |  __/_| |_) | |_| |
 |_| |_| |_|_|____| .__/|_|  \___|\__,_|_|\___|\__\___|\__,_|___\__,_|\__,_|\__\__,_|___|___/\__\___/|_|  \__,_|\__, |\___(_) .__/ \__, |
            |_____|_|                                      |_____|                 |_____|                      |___/       |_|    |___/ 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       October 9, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       ml_predicted_data_storage.py
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       The purpose of this file is to store the filtered and cleaned predicted data in Postgres. 
#                   |       
#                   |   
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

"""
#? Establish a connection to the PostgreSQL database
db_connection = psycopg2.connect(
    host="localhost",
    database="project_vigilant_db",
    user="vigilant_developer",
    password="root"
)
"""

db_connection = psycopg2.connect(
        database="vigilant_database",
        user="postgres",
        password="postgresroot",
        host="vigilant-aws-rds.c23zt6fnats7.us-east-2.rds.amazonaws.com",
        port='5432'
    )

#? Define the schema and table names for PostgreSQL
#! schema_name = "project_vigilant_schema" #! local deployment of vigilant
schema_name = "vigilant_schema"
table_name = "predicted_data_metrics"

#*-----------------------------------------------------------------------------------------
#*                                       FUNCTIONS
#*-----------------------------------------------------------------------------------------

def store_data_in_postgres(data):

    try:
        #? Create a cursor object for database interaction
        cursor = db_connection.cursor()
        
        #? Define the SQL query for inserting data into a specified schema and table
        insert_query = f"""
            INSERT INTO {schema_name}.{table_name} (
                cpu_usage_1mi,
                cpu_usage_5mi,
                cpu_usage_15mi,
                network_throughput_rx,
                network_throughput_tx,
                perf_load_avg_1mi,
                perf_load_avg_5mi,
                perf_load_avg_15mi,
                ptimestamp
            ) VALUES (
                %(cpu_usage_1mi)s,
                %(cpu_usage_5mi)s,
                %(cpu_usage_15mi)s,
                %(network_throughput_rx)s,
                %(network_throughput_tx)s,
                %(perf_load_avg_1mi)s,
                %(perf_load_avg_5mi)s,
                %(perf_load_avg_15mi)s,
                %(timestamp)s
            )
        """

        #? Execute the SQL query with the provided data
        cursor.execute(insert_query, data)
        
        #? Commit the transaction to save the data in the database
        db_connection.commit()
        
        #? Close the cursor
        cursor.close()
        
        print("\t\tPredicted Data Successfully Inserted in PostgreSQL.")
    except Exception as e:
        #? Handle exceptions and print an error message if insertion fails
        print(f"Error inserting data: {e}")


