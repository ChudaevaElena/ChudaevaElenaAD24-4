import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders_new.csv"
users_path = current_dir.parent / "All_Files" / "users_new.csv"

orders = pd.read_csv(orders_path)
users = pd.read_csv(users_path)

user_order_counts = orders['user_id'].value_counts().reset_index()
user_order_counts.columns = ['user_id', 'order_count']
users_with_multiple_orders = user_order_counts[user_order_counts['order_count'] > 1]
result = pd.merge(
    users_with_multiple_orders,
    users[['user_id', 'name']],
    on='user_id',
    how='left'
)

print(result[['user_id','name', 'order_count']].to_string(index=False))