#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
data_preprocessing.py

Purpose:
1. Load raw data from data/raw/.
2. Clean and preprocess the data (e.g., handle missing values, drop duplicates).
3. Save the processed data to data/processed/ for further use (e.g., training).

Usage:
python data_preprocessing.py

Project structure example:
my-predictive-modeling-project/
├─ data/
│   ├─ raw/
│   │   └─ example_data.csv
│   ├─ processed/
│   │   └─ processed_data.csv  (script output)
├─ scripts/
│   ├─ data_preprocessing.py
│   └─ train_model.py
└─ ...
"""

import os
import pandas as pd

def load_raw_data(raw_data_path: str) -> pd.DataFrame:
    """
    Loads raw data from a given path.

    Args:
        raw_data_path (str): Path to the raw data file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    df = pd.read_csv(raw_data_path, encoding="utf-8")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the data (e.g., removes empty rows and duplicates).

    Args:
        df (pd.DataFrame): Original DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = df.dropna(how="all")
    df = df.drop_duplicates()
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs feature engineering (e.g., normalization, encoding).

    Args:
        df (pd.DataFrame): Cleaned DataFrame.

    Returns:
        pd.DataFrame: DataFrame with additional or transformed features.
    """
    # Example: encoding categorical columns or scaling numeric columns
    # if "value" in df.columns:
    #     df["value_scaled"] = (df["value"] - df["value"].mean()) / df["value"].std()
    return df

def save_processed_data(df: pd.DataFrame, processed_data_path: str):
    """
    Saves the processed DataFrame to a specified path.

    Args:
        df (pd.DataFrame): Processed DataFrame.
        processed_data_path (str): Path to save the file.
    """
    df.to_csv(processed_data_path, index=False, encoding="utf-8")
    print(f"Processed data saved to: {processed_data_path}")

def main():
    raw_data_dir = os.path.join("data", "raw")
    processed_data_dir = os.path.join("data", "processed")

    # Create the processed data directory if it does not exist
    os.makedirs(processed_data_dir, exist_ok=True)

    # Example raw data file
    raw_data_file = os.path.join(raw_data_dir, "example_data.csv")
    processed_data_file = os.path.join(processed_data_dir, "processed_data.csv")

    # 1. Load raw data
    df_raw = load_raw_data(raw_data_file)

    # 2. Clean data
    df_clean = clean_data(df_raw)

    # 3. Perform feature engineering
    df_features = feature_engineering(df_clean)

    # 4. Save processed data
    save_processed_data(df_features, processed_data_file)

if __name__ == "__main__":
    main()
