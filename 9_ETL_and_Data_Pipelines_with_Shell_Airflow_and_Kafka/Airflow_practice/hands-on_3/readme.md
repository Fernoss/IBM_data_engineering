# Hands-on Lab tasks:

## 3) Create and execute a Shell script from Airflow
## Objectives
After completing this lab you will be able to:
  - Create a basic shell script
  - Explore the anatomy of a DAG.
  - Create a DAG.
  - Call and execute the shell script
  - Submit a DAG.

## Basic information
An Apache Airflow DAG is a python program. It consists of these logical blocks.
  - Imports
  - DAG Arguments
  - DAG Definition
  - Task Definitions
  - Task Pipeline

### DAG arguments are like settings for the DAG.
```python
#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Ramesh Sannareddy',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
```
  - the owner name,
  - when this DAG should run from: days_age(0) means today,
  - the email address where the alerts are sent to,
  - whether alert must be sent on failure,
  - whether alert must be sent on retry,
  - the number of retries in case of failure, and
  - the time delay between retries.
### A typical DAG definition block:
```python
# define the DAG
dag = DAG(
    dag_id='sample-etl-dag',
    default_args=default_args,
    description='Sample ETL DAG using Bash',
    schedule_interval=timedelta(days=1),
)
```
### A task definition block:
```python
# define the tasks

# define the task named extract_transform_and_load to call the shell script
extract_transform_and_load = BashOperator(
    task_id='extract_transform_and_load',
    bash_command='/home/project/airflow/dags/extract_transform_load.sh "',
    dag=dag,
)
```
  - A task_id which is a string and helps in identifying the task.
  - What bash command it represents. Here we are calling the shell script extract_transform_load.sh which we previously defined. 
  - Which dag this task belongs to.


### A task pipeline block
```python
# task pipeline
extract_transform_and_load
```

