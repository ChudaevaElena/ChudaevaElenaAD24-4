import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
customers_path = current_dir.parent / "All_Files" / "customers.csv"

customers = pd.read_csv(customers_path)

customers['birth_date'] = pd.to_datetime(
    customers['birth_date'], 
    format='%Y-%m-%d',  
    errors='coerce'
)

result = customers[
    (customers['gender'] == 'F') & 
    (customers['birth_date'].dt.year < 1995) &
    (customers['birth_date'].notna())
]

result = result.assign(birth_year=result['birth_date'].dt.year)
print("\nЖенщины, родившиеся до 1995 года:")
print(result[['customer_id', 'first_name', 'last_name', 'birth_year']].to_string(index=False))