# main.py

from core.packet_sniffer import PacketSniffer
from core.model import AnomalyDetector
from core.utils import save_anomalies_to_csv
from config.settings import INTERFACE

def main():
    # Step 1: Initialize sniffer with interface and number of packets
    sniffer = PacketSniffer(interface = INTERFACE, packet_count=10000)  

    # Step 2: Sniff packets and get DataFrame directly
    data = sniffer.sniff_packets()

    # Step 3: Train the anomaly detector
    detector = AnomalyDetector()
    detector.train_model(data)

    # Step 4: Detect anomalies in the same data
    anomalies = detector.detect_anomalies(data)

    # Step 5: Show and save anomalies
    print(f"\n[!] Found {len(anomalies)} anomalies:\n")
    print(anomalies)

    save_anomalies_to_csv(anomalies)

if __name__ == "__main__":
    main()
