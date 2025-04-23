🛰️ Network Anomaly Detector
A Python-based tool to detect anomalous network activity using the Isolation Forest algorithm. 
It captures live network packets, extracts features, and identifies unusual patterns. 
Anomalies are logged into a CSV file for further analysis.

Project Structure:
Network_anamolity_detector/
├── config/ → settings.py (Configuration: interface, output paths, etc.)
├── core/ → model.py (IsolationForest logic), packet_sniffer.py (Captures and processes network packets), utils.py (Utility functions)
├── data/ → anomalies.csv (Output file for detected anomalies)
├── main.py → Main entry point to run the tool
├── requirements.txt → Python dependencies
└── README.md → This file

Configuration:
Modify config/settings.py to set the network interface for packet sniffing, the output path for the anomalies CSV, and other preferences like packet limits (can also be adjusted in main.py).

How to Run:

Create and activate a virtual environment:


python3 -m venv venv

source venv/bin/activate (Linux/macOS)

.\venv\Scripts\activate (Windows)


Install dependencies: pip install -r requirements.txt


Run the tool: python main.py


For permission to sniff packets, you may need: sudo ./venv/bin/python main.py


How It Works:

Captures packets from your specified interface using Scapy
Extracts relevant features from each packet
Uses IsolationForest from scikit-learn to identify anomalies
Logs anomalous entries to data/anomalies.csv

Requirements:

Python 3.6+
scikit-learn
scapy
pandas
