import pandas as pd

customers = pd.read_csv("data/processed/customers.csv")
orders = pd.read_csv("data/processed/orders.csv")
order_items = pd.read_csv("data/processed/order_items.csv")
products = pd.read_csv("data/processed/products.csv")
payments = pd.read_csv("data/processed/payments.csv")
reviews = pd.read_csv("data/processed/reviews.csv")
sellers = pd.read_csv("data/processed/sellers.csv")

print(orders.columns)
print(customers.columns)

master = orders.merge(customers,on="customer_id",how="left")

print(master.shape)
print(master.head())

master = master.merge(
    order_items,
    on="order_id",
    how="left"
)

print(master.shape)

master = master.merge(
    products,
    on="product_id",
    how="left"
)

master = master.merge(
    payments,
    on="order_id",
    how="left"
)

master = master.merge(
    reviews,
    on="order_id",
    how="left"
)

master = master.merge(
    reviews,
    on="order_id",
    how="left"
)

master = master.merge(
    sellers,
    on="seller_id",
    how="left"
)

print(master.head())

print(master.shape)

print(master.columns)


master.to_csv(
    "data/processed/master_sales_dataset.csv",
    index=False
)

print("Master dataset created successfully!")