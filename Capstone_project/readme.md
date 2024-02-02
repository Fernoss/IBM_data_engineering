# Data Engineering Capstone Project
## About this project
Showcase your skills in this Data Engineering project! In this course you will apply a variety of data engineering skills and techniques you have learned as part of the previous courses in the IBM Data Engineering Professional Certificate.  

You will demonstrate your knowledge of Data Engineering by assuming the role of a Junior Data Engineer who has recently joined an organization and be presented with a real-world use case that requires architecting and implementing a data analytics platform. 

In this Capstone project you will complete numerous hands-on labs. You will create and query data repositories using relational and NoSQL databases such as MySQL and MongoDB. You’ll also design and populate a data warehouse using PostgreSQL and IBM Db2 and write queries to perform Cube and Rollup operations.  

You will generate reports from the data in the data warehouse and build a dashboard using Cognos Analytics. You will also show your proficiency in Extract, Transform, and Load (ETL) processes by creating data pipelines for moving data from different repositories. You will perform big data analytics using Apache Spark to make predictions with the help of a machine learning model. 

## Data Platform Architecture
### Tools and Technologies
- OLTP database - MySQL
- NoSql database - MongoDB
- Production Data warehouse – DB2 on Cloud
- Staging Data warehouse – PostgreSQL
- Big data platform - Hadoop
- Big data analytics platform – Spark
- Business Intelligence Dashboard - IBM Cognos Analytics
- Data Pipelines - Apache Airflow

### Process
- SoftCart's online presence is primarily through its website, which customers access using a variety of devices like laptops, mobiles and tablets.
- All the catalog data of the products is stored in the MongoDB NoSQL server.
- All the transactional data like inventory and sales are stored in the MySQL database server.
- SoftCart's webserver is driven entirely by these two databases.
- Data is periodically extracted from these two databases and put into the staging data warehouse running on PostgreSQL.
- The production data warehouse is on the cloud instance of IBM DB2 server.
- BI teams connect to the IBM DB2 for operational dashboard creation. IBM Cognos Analytics is used to create dashboards.
- SoftCart uses Hadoop cluster as its big data platform where all the data is collected for analytics purposes.
- Spark is used to analyse the data on the Hadoop cluster.
- To move data between OLTP, NoSQL and the data warehouse, ETL pipelines are used and these run on Apache Airflow.
