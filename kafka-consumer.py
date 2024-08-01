from kafka import KafkaConsumer

# Initialize a Kafka Consumer
consumer = KafkaConsumer(
    'metrics',
    bootstrap_servers=['localhost:29092'],
    auto_offset_reset='earliest',
    group_id='my-group'
)

# Consume messages
for message in consumer:
  print(f"Received message: {message.value.decode('utf-8')}")
