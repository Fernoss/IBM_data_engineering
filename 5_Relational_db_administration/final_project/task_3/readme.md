# Final Assignment - Database Administration - Part 3

**Scenario**

You are now tasked with provisioning a cloud instance of IBM DB2 server and performing tasks like data restoration, index creation, view creation, and connecting from the command line.

**Objectives**

In this part of the assignment, you will explore the following aspects of database administration:

1. Restore data
2. Indexing
3. View creation
4. Command-line connection

**Exercise 3.1 - Preparing the Lab Environment**

Before proceeding with the assignment, ensure you have access to a cloud instance of IBM DB2 database. If you don't have access, follow the instructions in this lab: Hands-on Lab: Sign up for IBM Cloud and Create a Db2 service instance to create an instance for yourself.

Download the file `billing.csv`.

**Exercise 3.2 - Restoring Data**

### Task 3.1 - Restoring the Table `billing`

1. Use the `billing.csv` you downloaded earlier to restore the CSV file into a table named `billing`.

2. Note that the column data types and widths are automatically generated based on the content. Edit the column attributes by clicking on the pencil icon next to the respective attributes to change the width of the `country` column to `varchar(30)` and the `month` column to `varchar(7)`.

3. Take a screenshot of the import status clearly showing the number of rows imported. Name the screenshot `restore-table.jpg`.

**Exercise 3.3 - Creating a View**

### Task 3.2 - Creating a View `basicbilldetails`

1. Create a view named `basicbilldetails` with the columns `customerid`, `month`, `billedamount`.

2. Take a screenshot of the SQL statement used to create the view. Name the screenshot `create-view.jpg`.

**Exercise 3.4 - Indexing**

### Task 3.3 - Baseline Query Performance

1. Write a query to find out all the rows with a billing amount of 19,929.

2. Take a screenshot of the command you used along with the query execution time. Name the screenshot `query-base-line-db2.jpg`.

### Task 3.4 - Creating an Index

1. Create an index that can improve the query performance of the previous task. Name the index as `billingamount`.

2. Take a screenshot of the SQL statement you used and the output. Name the screenshot `index-creation-db2.jpg`.

### Task 3.5 - Documenting the Improvement in Query Performance

1. Find out if the index has any impact on query performance.

2. Re-run the query to find out all the rows with a billing amount of 19,929.

3. Take a screenshot of the command you used along with the output along with the query execution time. Note that sometimes, the query time after index creation may increase due to various factors like:

   * Bandwidth at the time of firing the query
   * The load on the free cloud tier that your IBM DB2 instance uses is dynamic, and other load may impact your query time.
