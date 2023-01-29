#!/usr/bin/python3

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')

pd.read_csv('/mnt/c/etl_project/data/batch/customer.csv').to_sql('customer', con=engine, if_exists='replace', index=False)
pd.read_csv('/mnt/c/etl_project/data/batch/transaction.csv').to_sql('transaction', con=engine, if_exists='replace', index=False)