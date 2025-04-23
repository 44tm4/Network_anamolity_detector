# core/model.py

from sklearn.ensemble import IsolationForest
import pandas as pd
from config.settings import FEATURE_COLUMNS

class AnomalyDetector:
    def __init__(self, n_estimators=100, contamination=0.05):
        # Initialize the Isolation Forest model with default settings
        self.model = IsolationForest(n_estimators=n_estimators, contamination=contamination)

    def train_model(self, data):
        """
        Train the Isolation Forest model using the provided data.
        Assumes the data is a pandas DataFrame with relevant features.
        """
        print("[+] Training model...")
        # Use only the feature columns (we ignore the labels/target)
        X = data[FEATURE_COLUMNS].drop(columns=["src_ip", "dst_ip"])
        self.model.fit(X)

        print("[✓] Model training complete.")

    def detect_anomalies(self, data):
        """
        Predict anomalies in the provided data.
        Returns a list of predictions (-1 for anomaly, 1 for normal).
        """
        X = data[FEATURE_COLUMNS].drop(columns=["src_ip", "dst_ip"])
        predictions = self.model.predict(X)
        
        # Anomalies are marked with -1, normal packets with 1
        anomalies = data[predictions == -1]
        return anomalies
