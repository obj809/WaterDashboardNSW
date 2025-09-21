# Water Dashboard NSW

[![Frontend Tests](https://github.com/obj809/frontend-water-dashboard-nsw/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/obj809/frontend-water-dashboard-nsw/actions/workflows/test.yml)
[![Backend Tests](https://github.com/obj809/backend-water-dashboard-nsw/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/obj809/backend-water-dashboard-nsw/actions/workflows/ci.yml)

## Project Overview
A dashboard application that displays and analyses data about dams in NSW. Created with a Flask API, TypeScript React, and MySQL.

- [Frontend](https://github.com/obj809/frontend-water-dashboard-nsw)
- [Backend](https://github.com/obj809/backend-water-dashboard-nsw)
- [Local Database](https://github.com/obj809/local-db-water-dashboard-nsw)

## Project Links (Cloud)

- [AWS RDS](https://github.com/obj809/aws-rds-water-dashboard-nsw)
- [AWS Glue](https://github.com/obj809/aws-glue-water-dashboard-nsw)
- [Data Engineering](https://github.com/obj809/aws-data-engineering-water-dashboard-nsw)

## Frontend
<img src="./gifs/drone.gif" alt="App Demo" width="900" height="600"/>
<!-- ![Portfolio Screenshot](images/project-screenshot-dark.png)
![Individual Page Screenshot](images/project-screenshot-2.png) -->

## Backend
![API documentation](./api-documentation.png)

## Database

<!-- ![Database ERD](./database-erd.png) -->

```sql

CREATE TABLE dams (
    dam_id VARCHAR(20) PRIMARY KEY,
    dam_name VARCHAR(255) NOT NULL,
    full_volume INT,
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6)
);

CREATE TABLE latest_data (
    dam_id VARCHAR(20) PRIMARY KEY,
    dam_name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    storage_volume DECIMAL(10, 3),
    percentage_full DECIMAL(6, 2),
    storage_inflow DECIMAL(10, 3),
    storage_release DECIMAL(10, 3),
    FOREIGN KEY (dam_id) REFERENCES dams(dam_id)
);

CREATE TABLE dam_resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    dam_id VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    storage_volume DECIMAL(10, 3),
    percentage_full DECIMAL(6, 2),
    storage_inflow DECIMAL(10, 3),
    storage_release DECIMAL(10, 3),
    FOREIGN KEY (dam_id) REFERENCES dams(dam_id)
);

CREATE TABLE specific_dam_analysis (
    dam_id VARCHAR(20),
    analysis_date DATE,
    avg_storage_volume_12_months DECIMAL(10, 3),
    avg_storage_volume_5_years DECIMAL(10, 3),
    avg_storage_volume_20_years DECIMAL(10, 3),
    avg_percentage_full_12_months DECIMAL(6, 2),
    avg_percentage_full_5_years DECIMAL(6, 2),
    avg_percentage_full_20_years DECIMAL(6, 2),
    avg_storage_inflow_12_months DECIMAL(10, 3),
    avg_storage_inflow_5_years DECIMAL(10, 3),
    avg_storage_inflow_20_years DECIMAL(10, 3),
    avg_storage_release_12_months DECIMAL(10, 3),
    avg_storage_release_5_years DECIMAL(10, 3),
    avg_storage_release_20_years DECIMAL(10, 3),
    PRIMARY KEY (dam_id, analysis_date),
    FOREIGN KEY (dam_id) REFERENCES dams(dam_id)
);

CREATE TABLE overall_dam_analysis (
    analysis_date DATE PRIMARY KEY,
    avg_storage_volume_12_months DECIMAL(10, 3),
    avg_storage_volume_5_years DECIMAL(10, 3),
    avg_storage_volume_20_years DECIMAL(10, 3),
    avg_percentage_full_12_months DECIMAL(6, 2),
    avg_percentage_full_5_years DECIMAL(6, 2),
    avg_percentage_full_20_years DECIMAL(6, 2),
    avg_storage_inflow_12_months DECIMAL(10, 3),
    avg_storage_inflow_5_years DECIMAL(10, 3),
    avg_storage_inflow_20_years DECIMAL(10, 3),
    avg_storage_release_12_months DECIMAL(10, 3),
    avg_storage_release_5_years DECIMAL(10, 3),
    avg_storage_release_20_years DECIMAL(10, 3)
);

CREATE TABLE dam_groups (
    group_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE dam_group_members (
    group_name VARCHAR(255) NOT NULL,
    dam_id VARCHAR(20) NOT NULL,
    PRIMARY KEY (group_name, dam_id),
    FOREIGN KEY (group_name) REFERENCES dam_groups(group_name),
    FOREIGN KEY (dam_id) REFERENCES dams(dam_id)
);

```








<!-- ## Table of Contents

- [Frontend](#frontend)
- [Backend](#backend)
- [Data Approach](#data)
- [General](#general)


## Goals & MVP

- This project aims to support water management efforts and enhance public awareness about water resource trends and statuses.

- The MVP was to collect live and historic data about dams in NSW, using the WaterNSW API and display this in a responsive data dashboard to the user. 

- One major focus was to integrate cloud and data tools to create a live data pipeline directly from the public API into an AWS RDS, which could then be cleaned, processed and analyzed with PySpark.

## Build Strategy

- **First Stage** - Python scripting to collect all available data from the WaterNSW API, process it with Pandas, and then seed it into a local MySQL database.

- **Second Stage** - Building a Flask API on top of the local database, then connecting a React UI to display the data, including graphically with the Chart.js package

- **Third Stage** - Creating a live data pipeline with AWS Services and connecting this live-update database with the Flask backend, to create a real-time data experience

<a id="frontend"></a>
# Frontend - React Typescript

## Tech Stack

- React 
- Chart.js
- Typescript

## Design Goals
- This frontend was designed primarily as an SPA, with additional search functionality to fetch pages about specific resources. 
- Designed with the objective of creating an aesthetically appealing and interactive interface to display useful data for an engaging UX experience. 

## How To Use
- Use the search functionality with the search bar or open a list to find specific insights on a dam. 
- Clicking the 'dam-group' button will allow for automatic population of a new grouping and re-render the associated graph. 
- A variety of graphs and statistics display useful information to the user.

## Project Features
- [x] Chart.js integrated to provide graphical insights
- [x] Search feature allowing users to find specific dams
- [x] Individual pages about each dam that provide specific insights and analysis
- [x] Google Maps API integration for dynamically displaying location 

<a id="backend"></a>
# Backend - Flask API

## Tech Stack

- Flask
- Python


## Design Goals

## How To Use

## Project Features

<a id="data"></a>
# Data - Collection, Storage & Analysis

## Project Diagram
![Project Diagram](images/project-diagram.png)

## Tech Stack

- Pandas
- PySpark
- WaterNSW API 
- AWS RDS
- AWS S3 bucket
- AWS Lambda

## Data Components

There are three major data components in this project:

### Collection 

- A series of Python scripts were written to collect all data from the WaterNSW API and automate the database seeding process. These files can be found in the database-prep folder.

### PySpark Analysis

- PySpark was attached to the local database during development to perform a series of real-time calculations on the dataset, accessible through endpoints in the Flask API. 

- The analysis focuses specifically about how the average water level of any specific dam or the aggregation of dams within the dataset have changed over set time periods (12 months, 5 years, and 20 years).


### Live Data Pipeline 

- The WaterNSW API provides new data about each dam in the dataset on the first day of each month.

- A live data pipeline was created by first creating an AWS Lambda function call to collect an OAuth2 key, with a 12-hour duration, from the WaterNSW API on the first of each month and store this in an AWS S3 Bucket. 

- A second Lambda function call then uses this key to make an API call that accesses the endpoint that provides the latest data for each dam. This recent data is then stored in the AWS S3 Bucket. 

- This recent data is then written into the historical and latest data tables in the associated AWS RDS to provide an access point to the Flask API.

## AWS Pipeline Diagram
![AWS Data Pipeline](images/aws-pipeline.png)

## Project Features
- [x] AWS Lambda, AWS S3 Bucket and AWS RDS to create a live data pipeline 
- [x] Pandas for data handling and transfer
- [x] Live data cleaning, processing and analysis with PySpark
- [x] Scripting for API data collection and database seeding 

## Deployment - Docker, AWS ECS, Fargate

- Deployed by using Docker by tagging images in the AWS ECR, and then creating a service in AWS ECS 
- This project uses AWS Fargate to spin up a serverless compute engine when the deployment URL is accessed.

<a id="general"></a>
# General

## Additions & Improvements
- [ ] Investigate cached storage for calculations each month
- [ ] Fix bug with dynamically updating months on graphs
- [ ] Fix bug with button click in 'Dam Capacity Percentage Over Last 12 Months' graph
- [ ] Create testing for frontend and backend 
- [ ] Providing more complex analysis with PySpark (time-series, seasonal trends, etc.)
- [ ] Addition of distributed computing for data processing with Spark


## Learning Highlights
- Building a cloud-based live update data pipeline
- Integrating new data tools such as Pandas and PySpark
- Gaining hands-on experience with various AWS services 
- Creating a React based data dashboard to display insights to users
- Deploying with Docker and serverless computing resources

## Challenges
Many aspects of this application were challenging and provided experience in new domains, including creating a live-data pipeline, deployment with Docker, and learning new data tools. -->

## Contact Me
- Visit my [LinkedIn](https://www.linkedin.com/in/obj809/) for more details.
- Check out my [GitHub](https://github.com/cyberforge1) for more projects.
- Or send me an email at obj809@gmail.com
<br />
Thanks for your interest in this project. Feel free to reach out with any thoughts or questions.
<br />
<br />
Oliver Jenkins © 2024



