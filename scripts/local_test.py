import pandas as pd
import os

# Local test script for the data pipeline transformations

# Read raw data
raw_path = os.path.join('data', 'raw', 'sample.csv')
df_bronze = pd.read_csv(raw_path, sep='\t')  # Assuming tab separated

print("Bronze layer:")
print(df_bronze.head())

# Silver transformation
df_silver = df_bronze.dropna()
df_silver['age_group'] = df_silver['age'].apply(lambda x: 'Young' if x < 30 else 'Adult')

print("\nSilver layer:")
print(df_silver.head())

# Gold aggregation
df_gold = df_silver.groupby('age_group').agg(
    total_customers=('id', 'count'),
    total_age=('age', 'sum')
).reset_index()

print("\nGold layer:")
print(df_gold)

# Save to processed
processed_path = os.path.join('data', 'processed')
os.makedirs(processed_path, exist_ok=True)
df_silver.to_csv(os.path.join(processed_path, 'customer_clean.csv'), index=False)
df_gold.to_csv(os.path.join(processed_path, 'customer_summary.csv'), index=False)

print("\nData saved to data/processed/")