import pandas as pd



def main():
    customers = pd.read_csv("olist_customers_dataset.csv")

    print(customers.head())

    print(customers.shape)
    print(customers.info())
    print(customers.isnull().sum())
    print(customers.duplicated().sum())
    customers.describe(include="all")

if __name__== "__main__":
    main()