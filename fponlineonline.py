import pandas as pd
import numpy as np
import math

transaction_df = pd.read_csv("GroceryStoreDataSet.csv")
transaction_df
transaction_df.index.rename('TID', inplace=True)
transaction_df.rename(columns={"MILK','BREAD','BISCUIT'" : 'item_list'}, inplace=True)

print(transaction_df)
trans_df = transaction_df['item_list'].str.split(',')
trans_df