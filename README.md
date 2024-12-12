# Real-Time GOOG Stock Data Processing with Kafka and Flink

This project demonstrates a real-time stock data processing pipeline using **Kafka** for data ingestion and **Flink** for data processing. The project fetches stock data of GOOG from an API (Alpha Vantage), sends it to Kafka, processes it in real-time, and visualizes the results.

## Project Structure

In the folder **code** we have the **main** folder and the following files :

Before the real-time pipeline setup, the following files were created to **test and prepare** the stock data from the Alpha Vantage API:

- **`testapi.py`**: This file contains the code that tests the connection to the Alpha Vantage API. It fetches real-time stock data for the symbol (GOOG) and prints the raw response, allowing you to check if the API is responding correctly.

- **`extractcleandata.py`**: This file extracts the relevant data (close price and volume) from the raw JSON response of the API and performs data cleaning, ensuring the information is in the proper format for further processing.

- **`visualizedata.py`**: This file visualizes the processed stock data, including stock prices and volumes, using a plotting library such as Matplotlib. It helps visualize trends and patterns in the stock data.


In the folder **main** we have the following files :

- **`data_producer.py`**: This file fetches stock data from the Alpha Vantage API and sends it to Kafka. It acts as a producer in the Kafka setup, pushing the stock prices and volumes into the Kafka topic for consumption.
  
- **`kafka_setup.py`**: Configures and sets up Kafka producers and consumers. It ensures that messages are correctly sent to Kafka (by the producer) and retrieved by the consumer for processing.

- **`data_consumer.py`**: This file consumes the messages from Kafka, processes them, and sends them for visualization. It includes the logic for reading the incoming messages, cleaning the data, and preparing it for analysis.

- **`data_processor.py`**: This file performs any necessary data transformations and processing (like filtering, cleaning, or applying additional computations such as moving averages) before passing the data to the visualization component.

- **`visualization.py`**: Visualizes the processed stock data. It uses libraries like Matplotlib to generate real-time graphs that represent stock prices, volumes, and other relevant metrics.

- **`main.py`**: This is the entry point of the project. It coordinates the execution of all the steps, including data retrieval from the Alpha Vantage API, sending data to Kafka, consuming it for processing, and finally visualizing it.


### Requirements

- **Python 3.x**
- **Apache Kafka** installed and running
- **Apache Flink** installed and running (optional, depending on your setup)


## Prerequisites

- Kafka running.
- Apache Flink set up and running.
- Alpha Vantage API key (if needed).

### Setup Instructions

- Install Dependencies

- Download and extract Kafka from [here](https://kafka.apache.org/downloads).

Create a virtual environment and install the required dependencies:

pip install -r requirements.txt

- Compile and run the `data_producer.py` and `data_consumer.py` to start consuming and processing the data.

- Visualize the Data.

## Example Output:

## Kafka Output:

```bash
GOOG: $2800.50 Volume: 1,250,000
GOOG: $2802.10 Volume: 1,300,000
GOOG: $2805.35 Volume: 1,350,000
GOOG: $2808.60 Volume: 1,400,000
GOOG: $2809.20 Volume: 1,450,000
GOOG: $2810.00 Volume: 1,500,000
GOOG: $2807.80 Volume: 1,550,000
GOOG: $2806.00 Volume: 1,600,000
GOOG: $2811.10 Volume: 1,650,000
GOOG: $2812.50 Volume: 1,700,000
GOOG: $2809.75 Volume: 1,750,000
GOOG: $2810.40 Volume: 1,800,000
GOOG: $2809.00 Volume: 1,850,000
GOOG: $2813.30 Volume: 1,900,000
GOOG: $2815.00 Volume: 1,950,000
GOOG: $2812.20 Volume: 2,000,000
...
```

## Flink Output :
```
Processing stock data...

-- [Price Spikes Filter] --
GOOG Price Spike Detected: Ignored price change of 3% over the last 10 minutes.
GOOG Price Spike Detected: Ignored price change of 2.5% over the last 10 minutes.

-- [Volume Threshold Filter] --
GOOG Volume Below Threshold: Ignored data with volume 950,000 (below 1,000,000).
GOOG Volume Below Threshold: Ignored data with volume 975,000 (below 1,000,000).

-- [Moving Average Filter] --
GOOG Moving Average (last 10 mins): $2805.45

-- [Final Processed Data] --
New Data Processed - Average Price of GOOG: $2805.45
New Data Processed - Volume of GOOG: 1,500,000

Waiting for the next data batch...
```

# Conlusion :

This project demonstrates a real-time stock data processing pipeline using Kafka for data ingestion and Flink for processing. We successfully streamed GOOG stock data from the Alpha Vantage API, processed it in real-time with Flink, and visualized the results.

Key highlights of the project include: 

1. **Real-Time Data Stream:** We successfully streamed real-time stock market data into Kafka, allowing for the continuous flow of updated stock prices and trading volumes. Kafka ensured reliabledata transportation between the producer and consumer.

2. **Efficient Data Processing with Flink:** Using Flink, we applied real-time filters and aggregation techniques to process the incoming stock data. 

3. **Data Visualization:** The framework can be expanded to integrate advanced visualizations and handle multiple financial instruments.

In conclusion, this project showcases how Kafka and Flink can work together to build a scalable, real-time financial data processing system.

# Author : Nadia BEN YOUSSEF
