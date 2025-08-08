import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
group_orders_path = current_dir.parent / "All_Files" / "group_orders.csv"

df = pd.read_csv(group_orders_path)

df['order_date'] = pd.to_datetime(df['order_date'])
df['year_month'] = df['order_date'].dt.to_period('M')
monthly_revenue = df.groupby('year_month')['total'].sum().reset_index()
monthly_revenue.columns = ['order_month', 'monthly_revenue']
monthly_revenue['monthly_revenue'] = monthly_revenue['monthly_revenue'].astype(int)
print("\nОбщая выручка по месяцам:")
print(monthly_revenue)