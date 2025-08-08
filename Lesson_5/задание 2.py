import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders_new.csv"

orders = pd.read_csv(orders_path)

filtered_orders = orders.query("product == 'C' and (price * quantity) > 250")

print(filtered_orders[['order_id', 'user_id', 'product', 'price', 'quantity']])