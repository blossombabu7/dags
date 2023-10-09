import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


@dag(start_date=datetime.datetime(2023, 10, 10), schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="task")
generate_dag()
