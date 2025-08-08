import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders.csv"
customers_path = current_dir.parent / "All_Files" / "customers.csv"

orders = pd.read_csv(orders_path)
customers = pd.read_csv(customers_path)

customers['birth_date'] = pd.to_datetime(customers['birth_date'], errors='coerce')
customers['birth_year'] = customers['birth_date'].dt.year

customers_1990 = customers[customers['birth_year'] == 1990]

merged_data = pd.merge(
    orders, 
    customers_1990[['customer_id']], 
    on='customer_id', 
    how='inner'
)

print(merged_data[['order_id', 'customer_id']].to_string(index=False))