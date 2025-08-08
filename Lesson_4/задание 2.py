import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
group_orders_path = current_dir.parent / "All_Files" / "group_orders.csv"

df = pd.read_csv(group_orders_path)

average_order_by_city = df.groupby('city')['total'].mean().reset_index()
average_order_by_city.columns = ['city', 'average_order_total']
average_order_by_city['average_order_total'] = average_order_by_city['average_order_total'].round(2)
print("\nСредняя сумма заказа по каждому городу:")
print(average_order_by_city)