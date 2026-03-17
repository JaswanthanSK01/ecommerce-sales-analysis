import pandas as pd

customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")
items = pd.read_csv("data/order_items.csv")

print(customers)

df = orders.merge(customers, on="customer_id") \
           .merge(items, on="order_id")

print(df)

df = df[df['status'] == 'Delivered']
df['revenue'] = df['quantity'] * df['price']
print(df)

print("Total Revenue:", df['revenue'].sum())

print(df.groupby('name')['revenue'].sum())

import matplotlib.pyplot as plt

df.groupby('product')['revenue'].sum().plot(kind='bar')
plt.show()