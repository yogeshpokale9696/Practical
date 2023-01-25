
import pandas as pd
import itertools
#from goto import goto, label
min_sup=0
def getdata():
    Tn=int(input("Enter Transaction Number\n"))
    g = globals()
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
    min_sup = input("Enter Minimum Support")
        #min_conf = input("Enter Minimum Confidence")
    return data


def items(data):
    init = []
    for i in data:
        for q in i[1]:
            if(q not in init):
                init.append(q)
    init = sorted(init)
    return init


def maxnofitems(data) :
    list=[]
    for i in data:
        list.append(len(i[1]))
    return max(list)


def sub(x,init):
    s1=set()
    for L in range(x,x+ 1): # subset from maxi no of element
        for subset in itertools.combinations(init, L):
            s1.add(subset)
    return s1



def brut(maxi,init,data,min_sup):
    flist = []
    flag=0
    for k in range(maxi,0,-1):
        for i in sub(k,init) :
            cnt = 0
            for j in data:
                s3=set(i)
                s4=set(j[1])
                if (s3.issubset(s4)) :
                    cnt+=1

            if(cnt>=min_sup):
                flist.append([i,cnt])
                flag+=1
        if (flag!=0):
            return flist


def brutforce(data,min_sup):
    itemsindata = items(data)  # getting distinct items in data

    maxi = maxnofitems(data)  # max of no of items in any transaction

    # brut function matches combination of itemsindata with item sets of transaction
    df = pd.DataFrame(brut(maxi, itemsindata, data,min_sup), columns=['item', 'Support'])
    print(df)




#  main


data1 = [['T100',['I1','I2','I5']],
        ['T200',['I2','I4']],
        ['T300',['I2','I3']],
        ['T400',['I1','I2','I4']],
        ['T500',['I1','I3']],
        ['T600',['I2','I3']],
        ['T700',['I1','I3']],
        ['T800',['I1','I2','I3','I5']],
        ['T900',['I1','I2','I3']]
        ]

data2=[['T_1', ['M', 'O', 'N', 'K', 'E', 'Y']],
       ['T_2', ['D', 'O', 'N', 'K', 'E', 'Y']],
       ['T_3', ['M', 'A', 'K', 'E']],
       ['T_4', ['M', 'U', 'C', 'K', 'Y']],
       ['T_5', ['C', 'O', 'O', 'K', 'I', 'E']]]

data3=[['T_1', ['I1', 'I2', 'I3', 'I4']],
       ['T_2', ['I1', 'I2']],
       ['T_3', ['I1', 'I2', 'I3']],
       ['T_4', ['I1', 'I2', 'I3', 'I5']],
       ['T_5', ['I3', 'I4', 'I5']],
       ['T_6', ['I1', 'I3', 'I4', 'I5']]]


data4=[['T_1', ['A', 'B', 'D', 'E', 'H']], ['T_2', ['A', 'B', 'C', 'D']], ['T_3', ['B', 'C', 'E', 'G', 'H']], ['T_4', ['C', 'E', 'G', 'H']], ['T_5', ['A', 'B', 'C', 'E', 'F']], ['T_6', ['C', 'E', 'F']], ['T_7', ['A', 'B', 'C']]]


print("data1\n",data1)
print("data2\n",data2)
print("data3\n",data3)
# min_sup=2
# brutforce(data2)
for i in range(0,10):
    ch=int(input("1. On data1 \n 2. On data2 \n 3. On data3 \n 4. Enter Data \n"))
    if(ch==1):
        min_sup=int(input("Enter Minimum Support"))
        brutforce(data4,min_sup)
    elif(ch==2):
        min_sup = int(input("Enter Minimum Support"))
        brutforce(data2,min_sup)
    elif (ch==3):
        min_sup = int(input("Enter Minimum Support"))
        brutforce(data3, min_sup)
    elif(ch==4):
        brutforce(getdata(),min_sup)  # manually get data
    else:
        print("Enter Correct choice in format of 1 2 3 \n")