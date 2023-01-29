#!/bin/bash

# Enter Virtual Environment
source venv/bin/activate
pip install pandas
pip install sqlalchemy
pip install kafka-python

# Run Kafka Producer
python3 kafka_consumer.py