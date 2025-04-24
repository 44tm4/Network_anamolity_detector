# config/settings.py

# Network interface to sniff on (example: "eth0", "Wi-Fi", "lo", etc.)
INTERFACE = "eth0"

# Number of packets to sniff before training
PACKET_COUNT = 500

# Isolation Forest model settings
N_ESTIMATORS = 100
CONTAMINATION = 0.05  # expected proportion of anomalies

# CSV output file
OUTPUT_CSV = "data/anomalies.csv"

# Columns we care about
FEATURE_COLUMNS = ["src_ip", "dst_ip", "proto", "length", "timestamp"]
