#!/bin/bash

# Install Dependencies
pip install pandas
pip install sqlalchemy
pip install psycopg2-binary

# Load Data to PostgreSQL
python3 /mnt/c/etl_project/load_postgres.py

# Load Data to HDFS
hadoop fs -put /mnt/c/etl_project/data/batch/* hdfs://localhost:9000/data