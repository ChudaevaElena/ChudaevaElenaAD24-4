import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders.csv"

orders = pd.read_csv(orders_path, dtype={'order_date': str})

orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(
    orders['order_date'], 
    errors='coerce',
    format='%Y-%m-%d %H:%M:%S'
)

feb_2023_orders = orders[
    (orders['order_date'].dt.year == 2023) &
    (orders['order_date'].dt.month == 2) &
    (orders['total'] > 5000)
]

print(feb_2023_orders[['order_id', 'order_date', 'total']].to_string(index=False))