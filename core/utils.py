# core/utils.py

import pandas as pd
from config.settings import OUTPUT_CSV


def save_anomalies_to_csv(anomalies_df, path="data/anomalies.csv"):
    """
    Save the anomalies DataFrame to a CSV file.
    """
    if OUTPUT_CSV:
        path = OUTPUT_CSV
    anomalies_df.to_csv(path, index=False)
    print(f"[💾] Anomalies saved to: {path}")
