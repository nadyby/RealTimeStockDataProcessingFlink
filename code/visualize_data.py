import json
import matplotlib.pyplot as plt

def load_clean_data(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def visualize_data(clean_data):
    timestamps = [entry["timestamp"] for entry in clean_data]
    close_prices = [entry["close"] for entry in clean_data]
    volumes = [entry["volume"] for entry in clean_data]

    plt.style.use("seaborn-darkgrid")

    fig, ax1 = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
 
    ax1[0].plot(timestamps, close_prices, label="Prix de clôture (Close)", color="blue")
    ax1[0].set_title("Évolution du prix de clôture de GOOG")
    ax1[0].set_ylabel("Prix ($)")
    ax1[0].legend(loc="upper left")

    ax1[1].bar(timestamps, volumes, label="Volume", color="orange", alpha=0.7)
    ax1[1].set_title("Volume des transactions de GOOG")
    ax1[1].set_ylabel("Volume")
    ax1[1].set_xlabel("Timestamp")
    ax1[1].legend(loc="upper left")

    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()

    plt.show()

def main():
    clean_data_file = "GOOG_clean_data.json" 
    
    try:
        print("Chargement des données nettoyées...")
        clean_data = load_clean_data(clean_data_file)
        
        print("Visualisation des données...")
        visualize_data(clean_data)
    
    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    main()
