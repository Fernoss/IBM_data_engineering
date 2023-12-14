# SQLite3 with Python 🐍🔍

## Description

This project involves creating a database using SQLite3 in Python, 
loading a table with data from a CSV file using Pandas,
and running basic queries on the tables in the database.

### Execution Steps 🛠️🚀

1. **Create a database using SQLite3:**
   - The SQLite3 library in Python is used to create and connect the process to a new database named `STAFF`.

2. **Create and Load a Table:**
   - A table named `INSTRUCTOR` is created in the database with specific attributes (ID, FNAME, LNAME, CITY, CCODE).
   - Data is loaded into the table from a CSV file (`INSTRUCTOR.csv`) using Pandas.

3. **Run Basic Queries:**
   - Basic queries are executed on the tables in the database to retrieve and manipulate data.
     - View all data in the `INSTRUCTOR` table.
     - View the `FNAME` column.
     - View the total number of entries in the table.

4. **Append New Data:**
   - Additional data is appended to the `INSTRUCTOR` table in the database.

5. **Testing and Verification:**
   - Queries are re-executed to verify the changes, including viewing the total number of entries after appending new data.

## Project Structure 📁🌐

- `SQLite3_python_db` Folder: Contains the Python script and relevant files for the SQLite3 project.
- `INSTRUCTOR.csv`: CSV file containing data about instructors.
- `STAFF.db`: SQLite database storing the instructor data.

## Getting Started 🚀👨‍💻

1. Clone this repository.
2. Run the Python script to execute the SQLite3 operations.
3. Explore the changes in the database and verify the results.

Feel free to experiment and enhance the project further! Happy coding! 🚀📊

## Query Snippet

```sql
SELECT * FROM INSTRUCTOR;

   ID    FNAME      LNAME      CITY CCODE
0    1      Rav      Ahuja   TORONTO    CA
1    2     Raul      Chong   Markham    CA
2    3     Hima  Vasudevan   Chicago    US
3    4     John     Thomas  Illinois    US
4    5    Alice      James  Illinois    US
5    6    Steve      Wells  Illinois    US
6    7  Santosh      Kumar  Illinois    US
7    8    Ahmed    Hussain  Illinois    US
8    9    Nancy      Allen  Illinois    US
9   10     Mary     Thomas  Illinois    US
10  11  Bharath      Gupta  Illinois    US
11  12   Andrea      Jones  Illinois    US
12  13      Ann      Jacob  Illinois    US
13  14     Amit      Kumar  NewDelhi    IN
```
