#!/usr/bin/python3

import json
import pandas as pd
from sqlalchemy import create_engine
from kafka import KafkaConsumer

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
consumer = KafkaConsumer('project', bootstrap_servers=['localhost'])

for message in consumer:
    data = json.loads(message.value)
    df = pd.DataFrame([data])
    df.to_sql('search1', con=engine, if_exists='append', index=False)
    print(f'Records = {data}')