#!/usr/bin/python3

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timezone

dag = DAG(dag_id='extract_transform', start_date=datetime.now(timezone.utc), schedule='@once')
task1 = BashOperator(task_id='run_load', bash_command='/mnt/c/etl_project/run_load.sh ', dag=dag)
task2 = BashOperator(task_id='run_mapreduce', bash_command='/mnt/c/etl_project/run_mapreduce.sh ', dag=dag)
task3 = BashOperator(task_id='run_pyspark', bash_command='/mnt/c/etl_project/run_pyspark.sh ', dag=dag)

task1 >> task2 >> task3