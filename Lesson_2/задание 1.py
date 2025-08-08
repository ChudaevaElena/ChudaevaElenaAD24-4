import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders.csv"

df = pd.read_csv(orders_path)

df['order_date'] = df['order_date'].str.strip()
df['order_date'] = df['order_date'].str.replace(r'\s+,', ',', regex=True)

df['order_date'] = pd.to_datetime(
    df['order_date'], 
    errors='coerce',
    format='%Y-%m-%d %H:%M:%S'
)

filtered_orders = df[
    (df['total'] >= 30000) & 
    (df['total'] <= 40000) & 
    (df['order_date'] >= '2023-01-01')
]

order_ids = filtered_orders['order_id'].tolist()

print(filtered_orders[['order_id', 'order_date', 'total']].to_string(index=False))