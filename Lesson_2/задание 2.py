import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders.csv"

df = pd.read_csv(orders_path)

df['order_date'] = pd.to_datetime(
    df['order_date'], 
    errors='coerce',
    format='%Y-%m-%d %H:%M:%S'
)

russian_orders_2022 = df[
    (df['customer_id'].between(68, 88)) &  
    (df['order_date'].dt.year == 2022)    
]

result = russian_orders_2022.iloc[4:10][['order_id', 'total']]

print(result.to_string(index=False))