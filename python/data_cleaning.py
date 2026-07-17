import pandas as pd

customers = pd.read_csv("olist_customers_dataset.csv")
orders = pd.read_csv("olist_orders_dataset.csv")
order_items = pd.read_csv("olist_order_items_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")  
reviews = pd.read_csv("olist_order_reviews_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
sellers = pd.read_csv("olist_sellers_dataset.csv")
geolocation = pd.read_csv("olist_geolocation_dataset.csv")
translation = pd.read_csv("product_category_name_translation.csv")

customers.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
order_items.drop_duplicates(inplace=True)
payments.drop_duplicates(inplace=True)
reviews.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
sellers.drop_duplicates(inplace=True)
geolocation.drop_duplicates(inplace=True)
translation.drop_duplicates(inplace=True)


print(products.isnull().sum())
print(orders.isnull().sum())
print(reviews.isnull().sum())
print(payments.isnull().sum())
print(geolocation.isnull().sum())
print(translation.isnull().sum())
print(customers.isnull().sum())
print(order_items.isnull().sum())
print(sellers.isnull().sum())

products["product_category_name"] = products["product_category_name"].fillna("Unknown")
products["product_weight_g"] = products["product_weight_g"].fillna(products["product_weight_g"].median())

products["product_length_cm"] = products["product_length_cm"].fillna(products["product_length_cm"].median())

products["product_height_cm"] = products["product_height_cm"].fillna(products["product_height_cm"].median())

products["product_width_cm"] = products["product_width_cm"].fillna(products["product_width_cm"].median())

reviews["review_comment_title"] = reviews["review_comment_title"].fillna("No Title")

reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No Review")

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"]
)



orders["delivery_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_purchase_timestamp"]
).dt.days

orders["purchase_month"] = (
    orders["order_purchase_timestamp"].dt.month
)

orders["purchase_year"] = (
    orders["order_purchase_timestamp"].dt.year
)

orders["purchase_day"] = (
    orders["order_purchase_timestamp"].dt.day_name()
)

products = products.merge(
    translation,
    on="product_category_name",
    how="left"
)

customers.to_csv("data/processed/customers.csv", index=False)

orders.to_csv("data/processed/orders.csv", index=False)

order_items.to_csv("data/processed/order_items.csv", index=False)

payments.to_csv("data/processed/payments.csv", index=False)

reviews.to_csv("data/processed/reviews.csv", index=False)

products.to_csv("data/processed/products.csv", index=False)

sellers.to_csv("data/processed/sellers.csv", index=False)

geolocation.to_csv("data/processed/geolocation.csv", index=False)

translation.to_csv("data/processed/category_translation.csv", index=False)

print("✅ All cleaned datasets saved successfully!")