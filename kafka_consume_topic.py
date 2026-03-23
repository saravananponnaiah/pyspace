from kafka import KafkaConsumer
import json
import pandas as pd

# Define Kafka topic and broker information
KAFKA_TOPIC = 'payment-topic'  # Replace with your topic name
KAFKA_BROKER = 'localhost:9092' # Default Kafka broker address

def consume_kafka_messages():
    """
    Consumes messages from a specified Kafka topic.
    """
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=[KAFKA_BROKER],
            group_id='payment_consumer_group_new',  # A unique group ID for your consumer
            auto_offset_reset='earliest',  # Start consuming from the earliest available message
            enable_auto_commit=False,       # Automatically commit offsets
            value_deserializer=lambda x: json.loads(x.decode('utf-8')) # Deserialize JSON messages
        )

        print(f"Listening for messages on topic: {KAFKA_TOPIC}")
        ls_messages = []
        ls_schema = ['topic', 'sender', 'receiver', 'phone', 'amount', 'timestamp']

        for message in consumer:
            # message.value will contain the deserialized message
            print(f"Received message: Topic={message.topic}, Partition={message.partition}, "
                  f"Offset={message.offset}, Key={message.key}, Value={message.value}")
            json_object = message.value
            tuple_record = (message.topic,
                            message.key,
                            json_object['value']['receiver'],
                            json_object['value']['phone'],
                            json_object['value']['amount'],
                            json_object['timestamp'])
            ls_messages.append(tuple_record)
            # print(type(message.value))

        df = pd.DataFrame(ls_messages, columns=ls_schema)
        print(df)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'consumer' in locals() and consumer is not None:
            consumer.close()
            print("Kafka consumer closed.")

if __name__ == "__main__":
    consume_kafka_messages()