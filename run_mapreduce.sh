#!/bin/bash

# Install Dependencies
pip install mrjob

# Extract Data from HDFS with MapReduce
python3 /mnt/c/etl_project/mapreduce/date_customer.py -r hadoop hdfs://localhost:9000/data/transaction.csv > /mnt/c/etl_project/output/mapreduce/date_customer.txt
python3 /mnt/c/etl_project/mapreduce/date_product.py -r hadoop hdfs://localhost:9000/data/transaction.csv > /mnt/c/etl_project/output/mapreduce/date_product.txt
python3 /mnt/c/etl_project/mapreduce/date_transaction.py -r hadoop hdfs://localhost:9000/data/transaction.csv > /mnt/c/etl_project/output/mapreduce/date_transaction.txt