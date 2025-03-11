from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator 
from airflow.util.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl


default_args = {
    'owner' : 'airflow',
    'depends_on_past' : false,
    'start_date': datetime(2020, 11, 8),
    'email' : ['airflow@example.com']
    'email_on_failure' : False,
    'email_on_retry': False,
    'retries':1
}
