import matplotlib.pyplot as plt

def visualize_data(data):
    """
    Fonction pour afficher les données (prix de clôture, volume, etc.).
    """
    timestamps = [entry['timestamp'] for entry in data]
    close_prices = [entry['close'] for entry in data]
    volumes = [entry['volume'] for entry in data]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.plot(timestamps, close_prices, label="Prix de clôture", color="blue")
    ax1.set_title("Prix de Clôture au fil du Temps")
    ax1.set_xlabel("Temps")
    ax1.set_ylabel("Prix de Clôture")
    ax1.tick_params(axis='x', rotation=45)

    ax2.plot(timestamps, volumes, label="Volume", color="green")
    ax2.set_title("Volume des Transactions")
    ax2.set_xlabel("Temps")
    ax2.set_ylabel("Volume")
    ax2.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()


#EXEMPLE
if __name__ == "__main__":
    sample_data = [
        {"timestamp": "2024-12-12T10:00:00Z", "close": 2750.30, "volume": 1200000},
        {"timestamp": "2024-12-12T10:01:00Z", "close": 2751.20, "volume": 1300000},
        {"timestamp": "2024-12-12T10:02:00Z", "close": 2752.00, "volume": 1100000},
        {"timestamp": "2024-12-12T10:03:00Z", "close": 2750.90, "volume": 1400000},
        {"timestamp": "2024-12-12T10:04:00Z", "close": 2751.60, "volume": 1250000}
    ]
    visualize_data(sample_data)
