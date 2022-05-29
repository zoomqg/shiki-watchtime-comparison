import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
df = pd.read_csv('anilist.csv', sep=',', index_col='title')
df['sum'] = df.sum(axis=1)
df = df.sort_values(by=['sum'], ascending=False)

df['sum'] = df['sum'] / 5
df = df.rename(columns = {"sum" : "avg"})
print(df)

# sum_df = df.head(10)
# sum_df.plot.bar()
# plt.show()

