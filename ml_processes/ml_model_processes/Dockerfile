#"""
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
#██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
#██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
#██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
#██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
#╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
#  ____             _              __ _ _      
# |  _ \  ___   ___| | _____ _ __ / _(_) | ___ 
# | | | |/ _ \ / __| |/ / _ \ '__| |_| | |/ _ \
# | |_| | (_) | (__|   <  __/ |  |  _| | |  __/
# |____/ \___/ \___|_|\_\___|_|  |_| |_|_|\___|
#                                              
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       October 9, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       Dockerfile
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file, pared with the ml_train_build_model.py, can be used to train and build a model
#                   |       That uses linera regression to perform predictive Anaylysis.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#"""

# First the user  must have this dockerfile in the same directory as the python script: ml_train_build_model.py
# Second the user must run this command in the terminal to build the dockerfile:   "   docker build -t vigilant-ml-model .    "
# Thirs the user can then run the docker image:                                    "   docker run vigilant-ml-model            "
# fourth the user can then export the model with:                                  "   docker ps -a                            "
# Fifthe the user can then copy the file from the container to their machine:      "    docker cp <container_id>:/app/vigilant_ml_model.pkl /path/on/host/machine  "

ARG http_proxy
ARG https_proxy
ARG no_proxy

# Use a base image with Python, scikit-learn, pandas, and Redis dependencies
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy your code and data into the container
COPY . /app

# Install the required Python packages
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install pickle
RUN pip install redis

# Expose the port if needed (not necessary for this specific project)
# EXPOSE 80

# Command to run your model training script
CMD ["python", "ml_train_build_model.py"]


