import requests
import json

def fetch_intraday_data(symbol, interval, api_key):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": api_key,
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Erreur lors de la requête API: {response.status_code}")

def extract_clean_data(raw_data):
    if "Time Series (1min)" not in raw_data:
        raise Exception("Format de données inattendu, vérifiez la réponse de l'API.")
    
    time_series = raw_data["Time Series (1min)"]
    clean_data = []
    
    for timestamp, values in time_series.items():
        clean_data.append({
            "timestamp": timestamp,
            "close": float(values["4. close"]),
            "volume": int(values["5. volume"]),
        })
    
    clean_data = sorted(clean_data, key=lambda x: x["timestamp"])
    return clean_data

def main():
    api_key = "JU19JUO8DWYUIT4T"
    symbol = "GOOG"
    interval = "1min"
    
    try:
        print("Récupération des données brutes depuis Alpha Vantage...")
        raw_data = fetch_intraday_data(symbol, interval, api_key)
        
        print("Extraction et nettoyage des données...")
        clean_data = extract_clean_data(raw_data)
        
        print("Données nettoyées:")
        for entry in clean_data[:5]: 
            print(entry)
        
        with open(f"{symbol}_clean_data.json", "w") as f:
            json.dump(clean_data, f, indent=4)
        print(f"Données sauvegardées dans {symbol}_clean_data.json")
    
    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    main()
