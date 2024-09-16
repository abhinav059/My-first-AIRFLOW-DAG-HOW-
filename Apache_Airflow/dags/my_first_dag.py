from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 16),   start date
    'retries': 1,
}

# Function to be executed by PythonOperator
def simple_hello():
    print("Hello, Airflow!")

# Define the DAG
dag = DAG(
    'simple_hello_world_dag',  # DAG ID
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=None,  # Run manually, not on a schedule
)

# Define the task using PythonOperator
hello_task = PythonOperator(
    task_id='say_hello',  # Task ID
    python_callable=simple_hello,  # Function to be called
    dag=dag,  # Pass the DAG instance
)

            

# Task dependencies (for more complex DAGs)
hello_task  # This is a single task DAG so no dependencies
