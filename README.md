# project_vigilant
This project is a Linux Server monitor that will be deployed on AWS and leverages AI/ML tools.
***

## Description
This projet was conceptualized, designed, and built for my _Software Development Lifecycle 2_ class at Grand Canyon University as a part of the Software Engineering Program. 
Project Vigilant is a linux Server Monitoring System that I built for a Server I have at home. The application continually collects data metrics on the Server's health and activity
and displays that information on a Grafana Dashboard.


## Technologies
- Python
- Lua
- bash
- Docker
- SciKit
- Pandas
- Pickle
- Redis
- PostgreSQL
- Grafana
- AWS: Elastic Cloud Compute (EC2)
- AWS: Relational Database Service (RDS)
- AWS: Elastic Container Registry (ECR)

## Prototype 1
### Description
The first prototype of Vigilant was built on my local machine. I used Python, Lua, and Bash Scripts to collect data metrics from the server. The data was prepared and stored
in a local Postgres database. It was stored Raw in a Redis Database. The Data in Redis was used to train, build, and deploy an ML model that uses Linear regression to provide
Predictive Analytics.
![Screenshot 2023-11-01 at 12 30 25 PM](https://github.com/Ryanjwoodward/project_vigilant/assets/48807137/3952a24b-6d58-412a-8c82-bdbe8a555046)


<img width="1523" alt="screenshot of cloud grafana" src="https://github.com/Ryanjwoodward/project_vigilant/assets/48807137/d3873f81-b04b-4845-b012-e83f4e979f5c">

