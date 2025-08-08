import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders.csv"

orders = pd.read_csv(orders_path)
filtered_orders = orders[
    (orders['customer_id'].between(10, 20)) & 
    (orders['total'] > 8000)
]


print(filtered_orders[['order_id', 'customer_id', 'total']].to_string(index=False))