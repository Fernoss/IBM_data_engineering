# Web Scraping Project: Extracting Top 50 Highly-Ranked Films 🎬🕸️

Welcome to the Web Scraping project repository! In this project, you'll learn the process of
analyzing HTML code from a web page and extracting required information using web scraping in Python. 

## Project Overview 🌐🔍

### Objective
The main goal of this project is to scrape data from a webpage containing information about
the 100 most highly-ranked films and store the top 50 films in a database.

### Tools and Technologies
- **Python:** Utilizing the `requests`, `sqlite3`, `pandas`, and `BeautifulSoup` libraries.
- **Database:** SQLite is used to store the extracted information.
- **Data Processing:** Pandas is employed to structure the data before saving it to both CSV and SQLite.

## Code Sample 🚀📊

``` python
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# ... [Code Snippet - See Original Code] ...

# save the dataframe to a file
df.to_csv(csv_path)

# storing the data in a database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
```

## Execution Steps 🛠️🚀

1. **Web Scraping:** The HTML code of the target webpage is analyzed using the `requests` library, and the required information is extracted using `BeautifulSoup`.

2. **Data Extraction:** The project focuses on extracting details about the top 50 highly-ranked films, such as Average Rank, Film, and Year.

3. **Data Storage:** The extracted data is stored in both a CSV file (`top_50_films.csv`) and an SQLite database (`Movies.db`).

## Project Structure 📁🌐

- **`webscraping_and_APIs_basics` Folder:** Contains the Python script and relevant files for the web scraping project.
- **`top_50_films.csv`:** CSV file containing information about the top 50 films.
- **`Movies.db`:** SQLite database storing the extracted film data.

## Getting Started 🚀👨‍💻

1. Clone this repository.
2. Run the Python script to execute the web scraping and data extraction.
3. Explore the CSV file (`top_50_films.csv`) and SQLite database (`Movies.db`) for the extracted film information.

Feel free to experiment and enhance the project further! Happy coding! 🚀🎥
