import pandas as pd
import os

DATA_DIR = "data/raw"

print("=" * 70)
print("BLUESTOCK DAY 1 - DATA INGESTION")
print("=" * 70)

files = sorted(
    [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
)

for file in files:
    print(f"\nProcessing: {file}")

    path = os.path.join(DATA_DIR, file)

    try:
        df = pd.read_csv(path)

        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("-" * 70)

    except Exception as e:
        print(f"Error reading {file}")
        print(e)