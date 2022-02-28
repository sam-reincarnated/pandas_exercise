import pandas as pd
# Loading data into pandas from multiple sources
csv_filename = "./data/pokemon_data.csv"
df = pd.read_csv(csv_filename)
print(df.head(4))