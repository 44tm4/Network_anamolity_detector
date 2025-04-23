# core/packet_sniffer.py

from scapy.all import sniff, IP
import pandas as pd
from datetime import datetime
from config.settings import FEATURE_COLUMNS

class PacketSniffer:
    def __init__(self, interface, packet_count):
        self.interface = interface
        self.packet_count = packet_count
        self.packets_data = []

    def extract_features(self, packet):
        if IP in packet:
            return {
                "src_ip": packet[IP].src,
                "dst_ip": packet[IP].dst,
                "proto": packet[IP].proto,
                "length": len(packet),
                "timestamp": datetime.now().timestamp()
            }

    def packet_callback(self, packet):
        features = self.extract_features(packet)
        if features:
            self.packets_data.append(features)

    def sniff_packets(self):
        print(f"[+] Sniffing on interface: {self.interface} | Capturing {self.packet_count} packets...")
        sniff(iface=self.interface, prn=self.packet_callback, count=self.packet_count, store=False)
        print(f"[✓] Packet capture complete. Total packets captured: {len(self.packets_data)}")
        return pd.DataFrame(self.packets_data, columns=FEATURE_COLUMNS)
