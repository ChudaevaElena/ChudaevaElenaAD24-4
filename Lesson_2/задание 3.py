import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
products_path = current_dir.parent / "All_Files" / "products.csv"

products = pd.read_csv(products_path)

filtered_products = products[
    (products['price'] < 500) & 
    (products['volume_ml'] == 5.0)
]

print(filtered_products[['product_name', 'price']].to_string(index=False))