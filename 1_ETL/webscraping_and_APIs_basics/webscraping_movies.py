import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# establishing needed entities
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'webscraping_and_APIs_basics/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

# loading the webpage for scraping and parsing with Beautiful Soup
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# scraping the target information
tables = data.find_all('tbody') # gets the body of all the tables
rows = tables[0].find_all('tr') # gets all the rows of the first table

# iterate over the rows
for row in rows:
    if count<50: # restrict to 50 entries
        col = row.find_all('td') # Extract all the td data objects in the row and save
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0]) # convert the dictionary to a dataframe 
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

print(df)

# save the dataframe to a file
df.to_csv(csv_path)

# storing the data in a database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()