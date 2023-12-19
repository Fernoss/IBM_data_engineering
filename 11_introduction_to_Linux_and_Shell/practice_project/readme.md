# Weather ETL Practice Project 🌤️

## Scenario: 🚦 Building an Automated Weather ETL System 🚦

Your team has entrusted you with the task of developing an automated Extract, Transform, Load (ETL)
process for weather data. This POC will focus on Casablanca, Morocco, and utilize the wttr.in web service
to extract, transform, and load weather data into a live report for further analysis by the analytics team.
The goal is to assess the historical accuracy of temperature forecasts at noon.

## Data Source: 📑 Weather Data from wttr.in 📑

For this exercise, we'll employ the weather data package from the open-source project wttr.in.
This service provides weather information in a straightforward, text-based format. 
We'll utilize the curl command to scrape the weather data.

For in-depth information, refer to the service's GitHub Repo.

## Learning Objectives: 🧠 Elevate Your Shell Scripting Prowess 🧠

This practice project will refine your shell scripting skills by enabling you to:

1. Retrieve raw weather data

2. Extract relevant information from the dataset

3. Transform the data as required

4. Load the data into a log file in tabular format

5. Automate the entire process to run daily at a specified time

## Overview: 🏘️ Weather Reporting Tasks 🏘️

We'll focus on Casablanca, Morocco, and extract and store the following data daily at noon, local time:

- Actual temperature (in degrees Celsius)

- Forecasted temperature (in degrees Celsius) for the following day at noon

An example of the resulting weather report:

| year | month | day | obs_tmp | fc_temp |
|---|---|---|---|---|
| 2023 | 1 | 1 | 10 | 11 |
| 2023 | 1 | 2 | 11 | 12 |
| 2023 | 1 | 3 | 12 | 10 |
| 2023 | 1 | 4 | 13 | 13 |
| 2023 | 1 | 5 | 10 | 9 |
| 2023 | 1 | 6 | 11 | 10 |
