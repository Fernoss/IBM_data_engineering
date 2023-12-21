# Final Assignment - Database Administration - Part 1

## Scenario

You are now a PostgreSQL server administrator, responsible for managing users and performing database backups.

## Objectives

In this part of the assignment, you will delve into the following aspects of database administration:

1. Installation/Provisioning
2. Configuration
3. User Management
4. Backup

## Exercise 1.1 - Setting up the Lab Environment

Before proceeding with the assignment:

1. Start the PostgreSQL server.
2. Download the lab setup bash script from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/
3. Run the bash script.

### Task 1.1 - Identifying PostgreSQL Settings

What is the maximum number of connections allowed for the postgres server on the Theia lab?

**Hint:** The configuration file for PostgreSQL is located at `/home/project/postgres/data/postgresql.conf`.

1. Take a screenshot of the configuration file that clearly shows this information.
2. Name the screenshot `max-connections.jpg`.

## Exercise 1.2 - Managing PostgreSQL Users

Perform these user management tasks on your PostgreSQL server:

**Note:** Perform tasks 1.2 to 1.5 using the PostgreSQL CLI; do not use the PGADMIN GUI.

### Task 1.2 - Creating a User

Create a user named `backup_operator`.

1. Execute the command to create the user and take a screenshot of the command and output.
2. Name the screenshot `create-user.jpg`.

### Task 1.3 - Creating a Role

Create a role named `backup`.

1. Execute the command to create the role and take a screenshot of the command and output.
2. Name the screenshot `create-role.jpg`.

### Task 1.4 - Granting Privileges to a Role

Grant the following privileges to the `backup` role:

* `CONNECT` on the `tolldata` database.
* `SELECT` on all tables in the `toll` schema.

1. Execute the command to grant privileges and take a screenshot of the command and output.
2. Name the screenshot `grant-privs-to-role.jpg`.

### Task 1.5 - Granting a Role to an User

Grant the `backup` role to `backup_operator`.

1. Execute the command to grant the role and take a screenshot of the command and output.
2. Name the screenshot `grant-role.jpg`.

## Exercise 1.3 - Backing Up a Database

### Task 1.6 - Backing Up a PostgreSQL Database

Backup the `tolldata` database using PGADMIN GUI:

1. Backup the database `tolldata` into a file named `tolldatabackup.tar` using the `Tar` backup format.
2. Take a screenshot of the window displaying the filename and format configuration.
3. Name the screenshot `backup-database.jpg`.

## Conclusion - Part 1

This concludes Part 1 of the Data Platform Management Project. You have successfully completed the user management and backup tasks for the PostgreSQL server.
