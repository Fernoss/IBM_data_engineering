# Hands-on Lab tasks:

## 1) Getting started with Apache Airflow
## Objectives
After completing this lab, you will be able to:
  - Start Apache Airflow.
  - Open the Airflow UI in a browser.
  - List all the DAGs.
  - List the tasks in a DAG.
  - Explore a DAG in the UI.

  ## Example CLI Commands:

  ### List out all existing DAGs
  airflow dags list
  ### List out all tasks in a specific DAG (e.g., example_bash_operator)
  airflow tasks list example_bash_operator
  ### Unpause a DAG (e.g., example_bash_operator)
  airflow dags unpause example_bash_operator
  ### Pause a DAG (e.g., example_bash_operator)
  airflow dags pause example_bash_operator

## 2) Create a DAG for Apache Airflow
## Objectives
After completing this lab you will be able to:
  - Explore the anatomy of a DAG.
  - Create a DAG.
  - Submit a DAG.
## Anatomy of a DAG
An Apache Airflow DAG is a python program. It consists of these logical blocks.
  - Imports
  - DAG Arguments
  - DAG Definition
  - Task Definitions
  - Task Pipeline

## Exercise
  - Task 1: Create the imports block.
  - Task 2: Create the DAG Arguments block. You can use the default settings
  - Task 3: Create the DAG definition block. The DAG should run daily.
  - Task 4: Create the download task.
  - Task 5: Create the extract task.
  - Task 6: Create the transform task.
  - The transform task must capitalize the visitorid.
  - Task 7: Create the load task.
  - Task 8: Create the task pipeline block.
  - The pipeline block should schedule the task in the order listed below:
    - download
    - extract
    - transform
    - load
  - Task 10: Submit the DAG.
  - Task 11. Verify if the DAG is submitted

