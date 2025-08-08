import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
group_orders_path = current_dir.parent / "All_Files" / "group_orders.csv"

df = pd.read_csv(group_orders_path)

orders_by_city = df.groupby('city')['order_id'].count().reset_index()
orders_by_city.columns = ['city', 'order_count']
print("Ко-во заказов по городам:")
print(orders_by_city)