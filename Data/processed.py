#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
train_model.py

Purpose:
1. Load preprocessed data from data/processed/.
2. Train an example model using the data (here, a Random Forest classifier).
3. Evaluate the model and optionally save the trained model.

Usage:
python train_model.py

Project structure example:
my-predictive-modeling-project/
├─ data/
│   ├─ raw/
│   └─ processed/
│       └─ processed_data.csv
├─ scripts/
│   ├─ data_preprocessing.py
│   └─ train_model.py
└─ ...
"""

import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_processed_data(processed_data_path: str) -> pd.DataFrame:
    """
    Loads processed data from a specified path.

    Args:
        processed_data_path (str): Path to the processed data file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    df = pd.read_csv(processed_data_path, encoding="utf-8")
    return df

def train_random_forest_model(df: pd.DataFrame):
    """
    Trains a Random Forest model as an example classifier.

    Args:
        df (pd.DataFrame): DataFrame containing features and a "label" column.

    Returns:
        RandomForestClassifier: Trained RandomForest model.
    """
    if "label" not in df.columns:
        raise ValueError("The 'label' column is missing from the dataset.")

    # Separate features and labels
    X = df.drop(columns=["label"])
    y = df["label"]

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initialize and train the model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Make predictions
    y_pred = rf_model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Random Forest Test Accuracy: {acc:.4f}")

    return rf_model

def main():
    processed_data_dir = os.path.join("data", "processed")
    processed_data_file = os.path.join(processed_data_dir, "processed_data.csv")

    # 1. Load processed data
    df_processed = load_processed_data(processed_data_file)

    # 2. Train the model
    model = train_random_forest_model(df_processed)

    # 3. Optional: save the trained model
    # from joblib import dump
    # os.makedirs("results", exist_ok=True)
    # dump(model, "results/random_forest_model.joblib")
    # print("Model saved to results/random_forest_model.joblib")

if __name__ == "__main__":
    main()
