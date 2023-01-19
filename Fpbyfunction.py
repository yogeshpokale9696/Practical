# library installation for FP-Growth
# !pip install pyfpgrowth

# Sample code to do FP-Growth in Python
import pyfpgrowth
import pandas as pd

# Creating Sample Transactions
data1 = [
    ['Milk', 'Bread', 'Saffron'],
    ['Milk', 'Saffron'],
    ['Bread', 'Saffron', 'Wafer'],
    ['Bread', 'Wafer'],
]
data2 = [['f', 'a', 'c', 'd', 'g', 'm', 'p'],
         ['a', 'b', 'c', 'f', 'l', 'm', 'o'],
          ['b', 'f', 'h', 'o'],
          ['b', 'k', 'c', 'p'],
          ['a', 'f', 'c', 'l', 'p', 'm', 'n'],
         ]
import csv

transaction_df = pd.read_csv("GroceryStoreDataSet.csv")
transaction_df
transaction_df.index.rename('TID', inplace=True)
transaction_df.rename(columns={"MILK','BREAD','BISCUIT'" : 'item_list'}, inplace=True)

print(transaction_df)
trans_df = transaction_df['item_list'].str.split(',')
trans_df
# for i in data:
#     print(i)
transactions=trans_df

min_support=3
tno=0
for i in transactions:
    tno+=1

min_threshold=min_support/tno
#min_threshold=0.5

confi=0.5
# support=0.5*4
# print(support)
# Finding the frequent patterns with min support threshold=0.5
FrequentPatterns = pyfpgrowth.find_frequent_patterns(transactions=transactions, support_threshold=min_threshold)
print(FrequentPatterns)

# Generating rules with min confidence threshold=0.5
Rules = pyfpgrowth.generate_association_rules(patterns=FrequentPatterns, confidence_threshold=confi)
print(Rules)