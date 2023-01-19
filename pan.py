import numpy as np
import pandas
import pandas as pd
from numpy.core.numeric import identity
#demo=pd.Series()
#print(demo)

darr=["a","b","c","d","f"]
print(type(darr))

data=np.array(darr)
print(type(data))

series_d=pd.Series(data)
print(series_d)

#create series from dictionary

d1={'a':0,'b':1,'c':2}
print(type(d1))
print(d1)
s=pd.Series(d1)
print(s)
print(type(s))


s=pd.Series(d1,index=['b','c','d','r','a'])
print(s)

#Series from list

l1=['a','b','c','d','e','f']
s2=pd.Series(l1)
print(s2)

#acessing element of series

print(s2[0])
print(s2[4])


d3=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
print(d3)
print(d3[:4])
print(d3[2:4])
print(d3[1:])
print(d3[-2:])
print(d3[:-1])

#  Dataframe
print("Dataframe")
# empty Dataframe
df=pd.DataFrame()
print(type(df))

data=[4,1,2,3,4,5]
print(type(data))
df=pd.DataFrame(data)
print(df)

d4=[['a',1],['b',2],['c',3]]
print(type(d4))

df1=pd.DataFrame(d4,columns=['Name','Age'])
print(df1)

print("Dataframe from dictionary")

d5={'Name':['a','b','c','d'],'Age':[23,24,25,12],'Std':[5,2,5,2]}
df2=pd.DataFrame(d5)
print(df2)

d6=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
print(d6)

df3=pd.DataFrame(d6)
print(df3)

print("Fetching particular Element")
print(df2['Name'])
print(df2[['Name','Age']])

print("Fetching by row")
print(df2.loc[0])
print(df2.loc[2])
print(df2.loc[2:])
print(df2.loc[1:2])

#Pandas.iloc[]

#pandas.DataFrame.iloc[]
print(df1)