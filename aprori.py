from itertools import product

import numpy as np;
import pandas as pd;
from collections import Counter
min_sup=0;min_conf=0;itemlist=[]
def getdata():
    Tn=int(input("Enter Transaction Number\n"))
    g = globals()
    dict = {}
    data = []
    for i in range(1,Tn+1):
        v='T_{0}'.format(i)
        #print(v)
        g['T_{0}'.format(i)] = []
        #print(g['T_{0}'.format(i)])
        print(f"Enter No of Items in T_{i}")
        In = int(input())
        for j in range(0,In):
            print("Enter Item\n",j+1)
            inp=input()
            g['T_{0}'.format(i)].append(inp)
        data.append([v,g['T_{0}'.format(i)]])
        print(g['T_{0}'.format(i)])
        print(data)
        #min_sup = input("Enter Minimum Support")
        #min_conf = input("Enter Minimum Confidence")
    return data

#data=getdata()
data=[['T_1',['i1','i2']],['T_2',['i3','i1','i2']]]
min_sup=2
df=pd.DataFrame(data,columns=['Transaction','ItemSet'])
print(df)

list1=[]
for i in data:
    for q in i[1]:
        if(q not in  list1):
            list1.append(q)

list1=sorted(list1)
print(list1)

c = Counter()
for i in list1:
    for d in data:
        if(i in d[1]):
            c[i]+=1
print(c)
print("C1:")
C1=[]

for i in c:
    C1.append([i,c[i]])
dfc1=pd.DataFrame(C1,columns=['item','Support'])

#print(C1)
print(dfc1)

print("L1:")
L1=[]
for i in C1:
    if(i[1]>=min_sup):
        L1.append(i)
        #print(i[1])
print(L1)
dfl1=pd.DataFrame(L1,columns=['item','Support'])
print(dfl1)



print("C2:")
#print(dfl1.iloc[0,0]+','+dfl1.iloc[1,0])
lfors1=[]
for i in dfl1:
    lfors1.append(str(dfl1.iloc[0,0])+','+str(dfl1.iloc[1,0]))

lfors1.append('i1,i3')
lfors1.append('i2,i1')
print(lfors1)
#s1=set([dfl1.iloc[0,0]+','+dfl1.iloc[1,0]])

#s1=set(lfors1)
s1={'i1,i2', 'i1,i2', 'i1,i3', 'i2,i1'}


l1=[{'i1'},{'i2'},{'i3'},{'i4'}]

lofpro=[]
def pro(lx):
    for i in range(0,len(lx)-1):
        for j in range((i+1),len(lx)):
            testset=lx[i].union(lx[j])
            if lx[i].issubset(testset) and lx[j].issubset(testset) and (len(lx[i]) + 1) == len(testset):
                #print(lx[i].issubset(testset))
                lt=lx[j].union(lx[i])
                lofpro.append(lt)
    return lofpro


print(pro(l1))
print("Hello")
listt=pro(l1)

ls= []
for i in listt:
    T=0;flag=0
    for j in data:
        settest=set(j[1])
        if(i.issubset(settest)):
            T+=1;
            flag+=1
    if flag!=0 :
        if ([i,T] not in ls):
            ls.append([i,T])
            print(T)

        #print(i.issubset(settest))

print(ls)
dfl1 = pd.DataFrame(ls, columns=['item', 'Support'])
print(dfl1)

print("Hello")
#print(lsc)