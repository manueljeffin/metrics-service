from kafka import KafkaProducer
import json

# Initialize a Kafka Producer
producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Data to be sent
data = {'testKey': 'JIG'}

# Send data to the 'metrics' topic
producer.send('metrics', value=data)

# Ensure data is sent before exiting
producer.flush()
