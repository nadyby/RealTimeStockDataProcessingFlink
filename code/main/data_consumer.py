from kafka import KafkaConsumer
import json
import time

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "stock_prices" 
GROUP_ID = "stock-price-consumer-group"

def clean_data(data):
    """
    Fonction de nettoyage des données avant traitement.
    Cette fonction peut être étendue pour d'autres traitements nécessaires.
    """
    try:
        data_dict = json.loads(data)
        
        cleaned_data = {
            "timestamp": data_dict["timestamp"],
            "close": data_dict["close"],
            "volume": data_dict["volume"]
        }
        return cleaned_data
    except Exception as e:
        print(f"Erreur de nettoyage des données : {e}")
        return None

def consume_data():
    """
    Fonction principale pour consommer les messages du topic Kafka.
    Les données sont extraites et nettoyées avant d'être affichées.
    """
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=GROUP_ID,
        auto_offset_reset="earliest" 
    )
    
    print(f"Consommateur Kafka connecté au topic '{TOPIC}'...")

    for message in consumer:
        raw_data = message.value.decode("utf-8") 
        cleaned_data = clean_data(raw_data)
        
        if cleaned_data:
            print(f"Data received: {cleaned_data}")
        time.sleep(1)

if __name__ == "__main__":
    try:
        consume_data()
    except Exception as e:
        print(f"Erreur lors de la consommation des données : {e}")
