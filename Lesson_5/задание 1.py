import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
users_path = current_dir.parent / "All_Files" / "users_new.csv"
orders_path = current_dir.parent / "All_Files" / "orders_new.csv"

users = pd.read_csv(users_path)
orders = pd.read_csv(orders_path)

north_young_users = users[(users['region'] == 'North') & (users['age'] < 30)]
merged_data = pd.merge(north_young_users, orders, how='left')
total_orders = merged_data['order_id'].count()
print(north_young_users)
print("total_orders:", total_orders)