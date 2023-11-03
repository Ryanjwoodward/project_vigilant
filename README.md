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
<img width="1053" alt="Screenshot 2023-11-03 at 1 10 16 PM" src="https://github.com/Ryanjwoodward/project_vigilant/assets/48807137/01dccd2c-42c3-4066-95e7-b82a8157e31f">

## Prototype 1
### Description
The first prototype of Vigilant was built on my local machine. I used Python, Lua, and Bash Scripts to collect data metrics from the server. The data was prepared and stored
in a local Postgres database. It was stored Raw in a Redis Database. The Data in Redis was used to train, build, and deploy an ML model that uses Linear regression to provide
Predictive Analytics.
![Screenshot 2023-11-01 at 12 30 25 PM](https://github.com/Ryanjwoodward/project_vigilant/assets/48807137/3952a24b-6d58-412a-8c82-bdbe8a555046)
<img width="613" alt="Screenshot 2023-11-03 at 1 15 35 PM" src="https://github.com/Ryanjwoodward/project_vigilant/assets/48807137/b4858052-2bfb-4767-83af-91a7b60e13ca">




## Prototype 2
### Description
The second, and final, prototype of Vigilant was deployed on AWS using Elastic Cloud Compute (EC2) service, Elastic Container Registry (ECR), and Relational Database Service (RDS). Vigilant was dockerized and stored in the ECR, pulled to an EC2 instance and executed from the EC2. The Data collected from the server was stored in a Postgres Database within AWS RDS and displayed on the Grafana cloud.
<img width="1523" alt="screenshot of cloud grafana" src="https://github.com/Ryanjwoodward/project_vigilant/assets/48807137/d3873f81-b04b-4845-b012-e83f4e979f5c">
<img width="613" alt="Screenshot 2023-11-03 at 1 15 29 PM" src="https://github.com/Ryanjwoodward/project_vigilant/assets/48807137/6a226942-8f90-4577-a653-28b50efb9673">

