from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 

# establishing needed entities
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
db_name = 'Banks.db'
table_attribs = ["Rank","Name", "MC_USD_Billions"]
table_attribute_final = [
    "Name", 
    "MC_USD_Billions", 
    "MC_GBP_Billions",
    "MC_EUR_Billions",
    "MC_INR_Billions",
    ]
table_name = 'Largest_banks'
output_path = './Largest_banks_data.csv'
csv_path = './exchange_rate.csv'

# logging progress
def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

def extract(url, table_attribs):
    # loading the webpage for scraping and parsing with Beautiful Soup
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')

    # to create an empty pandas DataFrame with table attributes
    df = pd.DataFrame(columns=table_attribs)

    # scraping the target information
    tables = data.find_all('tbody')  # gets the body of all the tables
    rows = tables[0].find_all('tr')  # gets all the rows of the first table
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 3:
            rank = cols[0].get_text(strip=True)
            name = cols[1].get_text(strip=True)
            mc_usd_billions = cols[2].get_text(strip=True)
            mc_usd_billions = float(mc_usd_billions)  # Convert to float
            data_dict = {"Rank": rank, "Name": name, "MC_USD_Billions": mc_usd_billions}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

    return df


def transform(df, csv_path):
    # Read the exchange rate CSV file into a DataFrame
    exchange_rate_df = pd.read_csv(csv_path)

    # Convert the DataFrame to a dictionary
    exchange_rate_dict = exchange_rate_df.set_index('Currency').to_dict()['Rate']

    # Add new columns to the dataframe, with new currencies + two decimals
    df['MC_GBP_Billion'] = [np.round(x * exchange_rate_dict['GBP'], 2) for x in df['MC_USD_Billions']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate_dict['EUR'], 2) for x in df['MC_USD_Billions']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate_dict['INR'], 2) for x in df['MC_USD_Billions']]

    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_queries(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)



# --- Log progress + function calls
log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, csv_path)
# print(df['MC_EUR_Billion'][4])
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, output_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')

# Query 1: Print the contents of the entire table
query_1 = "SELECT * FROM Largest_banks"
run_queries(query_1, sql_connection)

# Query 2: Print the average market capitalization of all the banks in Billion USD
query_2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
run_queries(query_2, sql_connection)

# Query 3: Print only the names of the top 5 banks
query_3 = "SELECT Name FROM Largest_banks LIMIT 5"
run_queries(query_3, sql_connection)
log_progress('Process Complete.')

# sql_connection.close()
log_progress('Server Connection closed.')