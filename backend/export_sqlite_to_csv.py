import sqlite3
import csv
import os

# Path to your SQLite database file
DB_FILE = 'db.sqlite3'

# Output folder for CSV files
OUTPUT_FOLDER = 'csv_exports'

# Create the output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Connect to the database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f"Found {len(tables)} tables.")

for table_name in tables:
    table = table_name[0]
    print(f"Exporting table: {table}")

    # Get all rows
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    # Get column names
    cursor.execute(f"PRAGMA table_info({table})")
    columns_info = cursor.fetchall()
    headers = [col[1] for col in columns_info]

    # Write CSV
    csv_file_path = os.path.join(OUTPUT_FOLDER, f"{table}.csv")
    with open(csv_file_path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Saved {csv_file_path}")

conn.close()
print("✅ All tables exported successfully!")

