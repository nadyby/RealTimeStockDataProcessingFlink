import requests
import json

api_key = "JU19JUO8DWYUIT4T"
url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "GOOG",
    "interval": "1min",
    "apikey": api_key,
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Données récupérées avec succès:")
    print(json.dumps(data, indent=4))
else:
    print(f"Erreur lors de la requête : {response.status_code}")
    print(response.text)
