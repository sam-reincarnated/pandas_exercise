import pandas as pd
# Loading data into pandas from multiple sources
csv_filename = "./data/pokemon_data.csv"
df = pd.read_csv(csv_filename)
# Trying to print the whole data stream
# print(df)
# Trying to print the first N items in stream
N = 3
# print(df.head(N))
# Trying to print the last N items in stream
# print(df.tail(N))

tsv_file = "./data/pokemon_data.txt"
# Trying to read data from tab separated values
df_tsv = pd.read_csv(tsv_file, delimiter='\t')
# print(df_tsv.head(4))