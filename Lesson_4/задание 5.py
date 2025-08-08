import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
group_orders_path = current_dir.parent / "All_Files" / "group_orders.csv"

df = pd.read_csv(group_orders_path)

average_order_value = df.groupby('city')['total'].mean().reset_index()
sorted_cities = average_order_value.sort_values('total', ascending=False)
top_3_cities = sorted_cities.head(3).copy()
top_3_cities['total'] = top_3_cities['total'].round(2)
top_3_cities.columns = ['city', 'average_order_total']
print("\nТоп-3 города с самой высокой средней стоимостью заказа:")
print(top_3_cities)