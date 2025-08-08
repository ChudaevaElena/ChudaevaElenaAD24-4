import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
group_orders_path = current_dir.parent / "All_Files" / "group_orders.csv"

df = pd.read_csv(group_orders_path)

product_quantity = df.groupby('product')['quantity'].sum().reset_index()
max_quantity = product_quantity['quantity'].max()
top_products = product_quantity[product_quantity['quantity'] == max_quantity]
print("\nСамый топ товар по кол-ву:")
print(top_products)