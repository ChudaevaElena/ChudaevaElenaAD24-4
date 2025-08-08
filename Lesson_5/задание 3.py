import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
orders_path = current_dir.parent / "All_Files" / "orders_new.csv"

orders = pd.read_csv(orders_path)

product_counts = orders['product'].value_counts()

print(product_counts)