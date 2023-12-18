# ETL Practice Project - World Economies 🌐💰

## Introduction

This project demonstrates a comprehensive ETL process for extracting, transforming, loading, a
nd querying GDP data related to world economies. It utilizes web scraping, data transformation, 
CSV and database file handling, and logging mechanisms. The project structure, execution steps, 
and query snippet are well-organized and clearly explained. It serves as a practical learning 
tool for understanding and implementing ETL tasks. 🤓

## Project Structure 📂

- **ETL_practice_project Folder:** Contains the Python script and relevant files for the ETL practice project. 📦
  - **World_Economies.db:** SQLite database storing the transformed GDP data. 💾
  - **Countries_by_GDP.csv:** CSV file containing information about countries and their GDP. 📊
  - **etl_project_log.txt:** Log file recording the progress of the ETL process. 📈

## Execution Steps 🛠️🚀

### 1. Data Extraction 🔎

The `extract` function retrieves relevant GDP information from the Wikipedia page using web scraping and the requests API. 🌐

### 2. Data Transformation 🔮

The `transform` function converts GDP values from 'Million USD' to 'Billion USD' and updates the column name accordingly. 💰

### 3. Data Loading 🚀

- The transformed data is saved to a CSV file (`Countries_by_GDP.csv`) using the `load_to_csv` function. 📄
- The data is loaded into an SQLite database (`World_Economies.db`) as a table named `Countries_by_GDP` using the `load_to_db` function. 💿

### 4. Querying the Database 🔎

The `run_query` function demonstrates querying the database. An example query is provided in the readme. 🔍

```sql
SELECT * FROM Countries_by_GDP WHERE GDP_USD_billions >= 100;
Country   GDP_USD_billions
-------  ---------------
US         26854.60
China      19373.59
Japan       4409.74
Germany     4308.85
India       3736.88
...         ...            ...
Kenya       118.13
Angola      117.88
Oman        104.90
Guatemala    102.31
Bulgaria    100.64
```

This query retrieves countries with GDP equal to or greater than 100 billion USD. 💰

### Getting Started 🚀👨‍💻

- Clone this repository. 💾
- Run the Python script to execute the ETL process. 🏃‍♀️
- Explore the CSV file (`Countries_by_GDP.csv`) and SQLite database (`World_Economies.db`) for the transformed GDP information. 🔍
- Experiment and enhance the project further! 🧪

Happy coding! 🚀💹
