# Final Assignment - Database Administration - Part 2

**Scenario**

You are now a MySQL server administrator, responsible for tasks like configuration checks, data recovery, indexing, storage engine management, and automating backup processes.

**Objectives**

In this part of the assignment, you will explore the following aspects of database administration:

1. Installation/Provisioning
2. Configuration
3. Recovery
4. Indexing
5. Storage Engines
6. Automation of routine tasks

**Exercise 2.1 - Setting up the lab environment**

Before proceeding with the assignment, start the MySQL Server.

**Exercise 2.2 - Recovery**

### Task 2.1 - Restoring MySQL server using a previous backup

1. Download the backup file from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0231EN-SkillsNetwork/labs/Final%20Assignment/billingdata.sql.
2. Restore the backup file onto the MySQL server.
3. List the tables in the `billing` database.
4. Take a screenshot of the table list and name it `database-restore.jpg`.

### Task 2.2 - Finding the table data size

1. Find the data size of the table `billdata`.
2. Take a screenshot of the command and output and name it `table-data-size.jpg`.

**Exercise 2.3 - Indexing**

### Task 2.3 - Baseline query performance

1. Write a query to select all rows with a `billedamount` greater than 19,999 in table `billdata`.
2. Take a screenshot of the command, output, and query time and name it `query-base-line.jpg`.

### Task 2.4 - Creating an index

1. Create an appropriate index to improve the query performance of your baseline query.
2. Take a screenshot of the command and output and name it `index-creation.jpg`.

### Task 2.5 - Documenting the improvement in query performance

1. After creating the index, re-run the baseline query.
2. Take a screenshot of the command, output, and query time and name it `query-indexed.jpg`.

**Exercise 2.4 - Storage Engines**

### Task 2.6 - Listing supported storage engines

1. Run a command to find out if your MySQL server supports the `MyISAM` storage engine.
2. Take a screenshot of the command, output, and query time and name it `storage-engines.jpg`.

### Task 2.7 - Identifying the storage engine for a table

1. Find the storage engine of the table `billdata`.
2. Take a screenshot of the command and output and name it `storage-engine-type.jpg`.

**Exercise 2.5 - OPTIONAL Exercise (Non-graded) - Automation of routine tasks**

**Bonus Task 2.8 - Writing a bash script for automatic backup**

1. Create a bash script named `mybackup.sh` that performs the following tasks:

   a. Backs up all databases using `mysqldump` and stores the output in the file `all-databases-backup.sql`.
   b. Creates a directory named after the current date (YYYYMMDD) in the `/tmp/mysqldumps` directory. For example, `20210830`.
   c. Moves the file `all-databases-backup.sql` to the `/tmp/mysqldumps/<current date>/` directory.

2. Take a screenshot of the bash script with the entire code clearly visible and name it `bash-script.jpg`.

**Conclusion - Part 2**

This concludes Part 2 of the Data Platform Management Project. You have successfully completed tasks related to configuration checks, data recovery, indexing, storage engine management, and the optional automation of backup processes for MySQL.
