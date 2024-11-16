# Import the necessary libraries
import time
import json
import logging

import six
import sys

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer
from src.utils.feature_selection import transformations_data

# Apply the feature selection
X_test = transformations_data()

# Create a producer object
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: str(v).encode('utf-8'))

for index, row in X_test.iterrows():
    X_test_to_dict = dict(row)
    data = json.dumps(X_test_to_dict)
    producer.send('predict-happiness', value=data)
    logging.info(f"Message sent {data}")
    time.sleep(0.2)