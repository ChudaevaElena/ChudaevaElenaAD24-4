import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent

orders_path = current_dir.parent / "All_Files" / "orders.csv"
contacts_path = current_dir.parent / "All_Files" / "contacts.csv"
customers_path = current_dir.parent / "All_Files" / "customers.csv"

orders = pd.read_csv(orders_path)
contacts = pd.read_csv(contacts_path)
customers = pd.read_csv(customers_path)

merged = customers.merge(
    contacts, 
    left_on='contact_information', 
    right_on='customer_id',
    suffixes=('_cust', '_cont')
)

full_data = orders.merge(
    merged,
    left_on='customer_id',
    right_on='customer_id_cust'
)

full_data['order_date'] = full_data['order_date'].str.strip()
full_data['order_date'] = pd.to_datetime(full_data['order_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
full_data['registration_date'] = pd.to_datetime(full_data['registration_date'].str.strip(), format='%Y-%m-%d', errors='coerce')

europe_countries = ['Germany', 'UK', 'France', 'Italy', 'Spain', 'Russia']
filtered1 = full_data[
    (full_data['country'].isin(europe_countries)) & 
    (full_data['order_date'] >= '2023-01-01') & 
    (full_data['order_date'] <= '2023-06-30')
]
total_sales = filtered1['total'].sum()
print("Сумма продаж:", total_sales)