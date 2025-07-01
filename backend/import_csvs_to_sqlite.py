import sqlite3
import pandas as pd
import os

# CONFIGURATION
DB_FILE = 'db.sqlite3'         # Your target SQLite DB
CSV_FOLDER = 'csv_exports'     # Folder containing all CSVs

# Connect to the database (creates if not exists)
conn = sqlite3.connect(DB_FILE)

# Loop over all CSV files in the folder
for csv_file in os.listdir(CSV_FOLDER):
    if csv_file.endswith('.csv'):
        table_name = os.path.splitext(csv_file)[0]
        csv_path = os.path.join(CSV_FOLDER, csv_file)
        
        print(f"Importing {csv_file} into table {table_name}...")
        
        # Read CSV with pandas
        df = pd.read_csv(csv_path)
        
        # Write to SQLite (replace existing table if any)
        df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()

print("✅ All CSV files have been imported successfully!")

