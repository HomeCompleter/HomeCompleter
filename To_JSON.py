import pandas as pd

df1 = pd.read_csv('dataset\ikea_products_mentor_data.csv')

df1.to_json('data.json')