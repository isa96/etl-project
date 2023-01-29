#!/usr/bin/python3

import json
import pandas as pd
from kafka import KafkaProducer

file = pd.read_csv('data/stream/search.csv').to_dict(orient='records')
producer = KafkaProducer(bootstrap_servers=['localhost'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for data in file:
    print(data)
    producer.send('project', data)