import pandas as pd
import numpy as np

def calculate_moving_average(data, window=10):
    """
    Calcul de la moyenne mobile simple sur les données.
    :param data: Liste de données (prix ou volume)
    :param window: La taille de la fenêtre pour la moyenne mobile
    :return: Liste des moyennes mobiles
    """
    return pd.Series(data).rolling(window=window).mean().iloc[-1]

def filter_by_volume(data, threshold=1000000):
    """
    Filtrer les données dont le volume est inférieur au seuil spécifié.
    :param data: Liste de données contenant les informations de volume
    :param threshold: Seuil de volume
    :return: True si le volume est au-dessus du seuil, sinon False
    """
    return data["volume"] >= threshold

def process_data(data):
    """
    Traiter les données avant de les envoyer à un autre service.
    Cette fonction applique des filtres et des calculs de moyennes mobiles.
    :param data: Données reçues à traiter
    :return: Données traitées ou None si les données ne passent pas les filtres
    """
    if not filter_by_volume(data): 
        print(f"Volume trop faible, données ignorées : {data['timestamp']} - Volume: {data['volume']}")
        return None

    close_prices = data.get("close_prices", [])
    if close_prices:
        moving_avg = calculate_moving_average(close_prices)
        print(f"Moyenne mobile sur 10 périodes : {moving_avg}")

    return data

#TEST 
if __name__ == "__main__":
    sample_data = {
        "timestamp": "2024-12-12T10:00:00Z",
        "close": 2750.30,
        "volume": 1200000,
        "close_prices": [2749.50, 2750.00, 2751.20, 2750.50, 2752.10, 2751.30, 2750.00, 2750.40, 2749.80, 2751.00]
    }
    
    processed_data = process_data(sample_data)
    if processed_data:
        print(f"Données traitées : {processed_data}")
