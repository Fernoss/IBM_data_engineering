#### Create and Access SQLite Database using Python🐍

### Objectives
After completing this lab you will be able to:

1. Create a database

2. Create a table

3. Insert data into the table

4. Query data from the table

5. Retrieve the result set into a pandas dataframe

6. Close the database connection

SQLite is a software library that implements a self-contained, serverless, 
zero-configuration, transactional SQL database engine. SQLite is the most 
widely deployed SQL database engine in the world.

**Snippet**

```python
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('mydatabase.db')
```
