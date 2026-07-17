from sqlalchemy import create_engine
import pandas as pd

# ==========================
# MySQL Connection
# ==========================
engine = create_engine(
    "mysql+mysqlconnector://root:atharv@localhost/sales_analytics"
)

# Test connection
try:
    with engine.connect():
        print("[OK] Connected to MySQL successfully!\n")
except Exception as e:
    print("[ERROR] Connection Failed!")
    print(e)
    exit()

# ==========================
# Dataset Mapping
# ==========================
datasets = {
    "customers": "data/processed/customers.csv",
    "orders": "data/processed/orders.csv",
    "order_items": "data/processed/order_items.csv",
    "payments": "data/processed/payments.csv",
    "products": "data/processed/products.csv",
    "reviews": "data/processed/reviews.csv",
    "sellers": "data/processed/sellers.csv",
    "geolocation": "data/processed/geolocation.csv"
}

# ==========================
# Load One Table
# ==========================
def load_table(table_name, file_path):
    try:
        df = pd.read_csv(file_path)

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",   # Change to "append" later if required
            index=False
        )

        print(f"[OK] {table_name:<15} Loaded Successfully ({len(df)} rows)")

    except Exception as e:
        print(f"[ERROR] Failed to load {table_name}")
        print(e)


# ==========================
# Main ETL Process
# ==========================
def main():

    print("=" * 60)
    print("Starting ETL Process...")
    print("=" * 60)

    for table_name, file_path in datasets.items():
        load_table(table_name, file_path)

    print("\n" + "=" * 60)
    print("[OK] ETL Process Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()