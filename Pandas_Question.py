import numpy as np
import pandas as pd

print("Q.1")
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

print("Q.2")
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)

print("Q.3")

print(df)
print( df.info())

print("Q.4")

print(df[:3])

print("Q.5")

print(df.iloc[:,:2])

print("Q.6")

print(df.iloc[[1,3,5,6],:2])

print("Q.7")
print(df)
print(df[df['attempts'] > 2])

#or

print(df[df.iloc[:,2] > 2])

print("Q.8")
#print("Row Count",df.count(axis=0))
#print("COLUMN Count",df.count(axis=1))
print("Row Count",len(df.axes[0]))
print("Column Count",len(df.axes[1]))

print("Q.9")

print(df[df['score'].isnull()])

print("Q.10")
print(df[df['score'].between(15,20)])

#print(df[df['score'].between(15,20,inclusive=True)])