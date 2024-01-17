# Hands-on Lab: Getting started with Apache Airflow

## Objectives
After completing this lab, you will be able to:
- Start Apache Airflow.
- Open the Airflow UI in a browser.
- List all the DAGs.
- List the tasks in a DAG.
- Explore a DAG in the UI.

## Example CLI Commands:

### List out all existing DAGs
airflow tags list
### List out all tasks in a specific DAG (e.g., example_bash_operator)
airflow tasks list example_bash_operator
### Unpause a DAG (e.g., example_bash_operator)
airflow dags unpause example_bash_operator
### Pause a DAG (e.g., example_bash_operator)
airflow dags pause example_bash_operator
