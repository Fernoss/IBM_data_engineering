# ETL Process Synopsis 🔄

This repository showcases an ETL (Extract, Transform, Load) process implemented in Python. 
The ETL process involves extracting data from various file types, transforming the data,
and loading it into a database for further processing.

## Code Overview

The code utilizes Python with libraries such as `pandas` and `xml.etree.ElementTree` for data manipulation and processing.
It demonstrates the extraction of data from CSV, JSON, and XML files, performs unit conversions, and logs the ETL process progress.

## Extract Phase

The `extract` function employs the `glob` library to identify different file types. 
It processes CSV, JSON, and XML files, creating a unified dataframe for further transformations.

## Transform Phase

The `transform` function converts units from inches/pounds to meters/kilograms, rounding off the values to two decimals.

## Load Phase

The `load_data` function writes the transformed data to a CSV file.

## Logging Progress

The ETL process progress is logged with timestamps. 
The logs include the initiation and completion of each phase: Extract, Transform, and Load.

## Execution

To run the ETL process, execute the provided Python script (`etl_process.py`). 
The progress logs are recorded in the `log_file.txt`, and the transformed data is saved to `transformed_data.csv`.

Feel free to explore the code and adapt it to your specific ETL needs!

Happy coding! 🚀
