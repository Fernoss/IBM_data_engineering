import sqlite3
import pandas as pd

# use SQLite3 to create and connect process to a new database STAFF
conn = sqlite3.connect('SQLite3_python_db/STAFF.db')

# create a table in the database with attributes
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# read the CSV using Pandas
file_path = 'SQLite3_python_db/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

# loading data to table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)

# testing the database with queries
# view all the data in tables
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# view fname
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# view total number of entries
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# appending new data to the db and creating 
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

# to INSTRUCTOR db
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# view total number of entries again to see the difference
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()