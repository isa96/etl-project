#!/usr/bin/python3

from pyspark.sql import SparkSession
import sqlparse

spark = SparkSession \
    .builder \
    .master('spark://aaa.localdomain:7077') \
    .appName('project') \
    .config('spark.jars', '/etc/postgresql/14/main/postgresql-42.5.0.jar') \
    .getOrCreate()

df_customer = spark.read \
    .format('jdbc') \
    .option('url', 'jdbc:postgresql://localhost:5432/postgres') \
    .option('dbtable', 'customer') \
    .option('user', 'postgres') \
    .option('password', 'postgres') \
    .option('driver', 'org.postgresql.Driver') \
    .load()

query = sqlparse.format(open('/mnt/c/etl_project/queries/age_gender.sql', 'r'))

df_customer.createOrReplaceTempView('customer')
results = spark.sql(f'{query}')
results.show(20)
results.toPandas().to_csv('/mnt/c/etl_project/output/pyspark/age_gender.csv', index=False)
