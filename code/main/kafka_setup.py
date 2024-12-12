from kafka.admin import KafkaAdminClient, NewTopic

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092" 
TOPICS = ["stock_prices"] 

def create_topics():
    """
    Crée les topics Kafka nécessaires si ils n'existent pas déjà.
    """
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    print(f"Connexion au serveur Kafka : {KAFKA_BOOTSTRAP_SERVERS}")
    
    existing_topics = admin_client.list_topics()
    print(f"Topics existants : {existing_topics}")
    
    topics_to_create = [
        NewTopic(name=topic, num_partitions=1, replication_factor=1)
        for topic in TOPICS
        if topic not in existing_topics
    ]
    
    if topics_to_create:
        admin_client.create_topics(new_topics=topics_to_create)
        print(f"Topics créés : {[topic.name for topic in topics_to_create]}")
    else:
        print("Tous les topics existent déjà.")

if __name__ == "__main__":
    try:
        create_topics()
    except Exception as e:
        print(f"Erreur lors de la création des topics : {e}")
