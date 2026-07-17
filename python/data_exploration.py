import pandas as pd


def explore_dataset(file_name):
    print("=" * 80)
    print(f"Exploring: {file_name}")
    print("=" * 80)

    df = pd.read_csv(file_name)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nSummary Statistics:")
    print(df.describe(include="all"))

    print("\n\n")


def main():

    datasets = [
        "olist_customers_dataset.csv",
        "olist_orders_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_order_payments_dataset.csv",
        "olist_order_reviews_dataset.csv",
        "olist_products_dataset.csv",
        "olist_sellers_dataset.csv",
        "olist_geolocation_dataset.csv",
        "product_category_name_translation.csv"
    ]

    for dataset in datasets:
        explore_dataset(dataset)


if __name__ == "__main__":
    main()