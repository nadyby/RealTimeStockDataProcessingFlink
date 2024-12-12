from kafka import KafkaProducer, KafkaConsumer
import json
import time
import logging
from data_producer import fetch_and_send_data
from data_processor import process_data
from visualization import visualize_data

logging.basicConfig(level=logging.INFO)
KAFKA_TOPIC = 'stocks_data'
KAFKA_SERVER = 'localhost:9092'

def run_kafka_producer():
    fetch_and_send_data(KAFKA_SERVER, KAFKA_TOPIC)

def run_kafka_consumer():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_SERVER],
        group_id='stocks_group',
        auto_offset_reset='earliest'
    )

    for message in consumer:
        logging.info(f"Message reçu: {message.value}")
        processed_data = process_data(message.value)
        visualize_data(processed_data)

def main():
    producer_thread = threading.Thread(target=run_kafka_producer)
    producer_thread.start()

    consumer_thread = threading.Thread(target=run_kafka_consumer)
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()
