import json
import time
import requests
from kafka import KafkaProducer

API_KEY = "JU19JUO8DWYUIT4T" 
API_URL = "https://www.alphavantage.co/query"
SYMBOL = "GOOG" 

KAFKA_TOPIC = "stock_prices"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

def get_stock_data():
    """
    Récupère les données boursières depuis l'API Alpha Vantage.
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": SYMBOL,
        "interval": "1min",
        "apikey": API_KEY,
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        time_series = data.get("Time Series (1min)", {})
        return time_series
    else:
        print(f"Erreur lors de la requête API : {response.status_code}")
        return None

def produce_data():
    """
    Envoie les données boursières extraites à un topic Kafka.
    """
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print(f"Producteur Kafka connecté au serveur : {KAFKA_BOOTSTRAP_SERVERS}")
    
    while True:
        data = get_stock_data()
        if data:
            for timestamp, values in data.items():
                record = {
                    "symbol": SYMBOL,
                    "timestamp": timestamp,
                    "close": float(values["4. close"]),
                    "volume": int(values["5. volume"])
                }
                producer.send(KAFKA_TOPIC, value=record)
                print(f"Envoyé à Kafka : {record}")
        else:
            print("Aucune donnée récupérée.")
        time.sleep(60)

if __name__ == "__main__":
    try:
        produce_data()
    except KeyboardInterrupt:
        print("Production arrêtée.")
