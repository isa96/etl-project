#!/bin/bash

# Install Dependencies
pip install pyspark
pip install sqlparse

# Extract Data from PostgreSQL with Spark
python3 /mnt/c/etl_project/pyspark/age_gender.py
python3 /mnt/c/etl_project/pyspark/country_transaction.py
python3 /mnt/c/etl_project/pyspark/date_search.py
python3 /mnt/c/etl_project/pyspark/date_transaction.py
python3 /mnt/c/etl_project/pyspark/product_search.py
python3 /mnt/c/etl_project/pyspark/product_transaction.py