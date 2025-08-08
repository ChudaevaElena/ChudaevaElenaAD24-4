import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders_new.csv"
users_path = current_dir.parent / "All_Files" / "users_new.csv"

orders = pd.read_csv(orders_path)
users = pd.read_csv(users_path)

merged_data = pd.merge(orders, users, on='user_id')
merged_data['total_amount'] = merged_data['price'] * merged_data['quantity']
pivot_table = pd.pivot_table(
    merged_data,
    index='region',
    columns='product',
    values='total_amount',
    aggfunc='sum',
    fill_value=0
)

print(pivot_table)