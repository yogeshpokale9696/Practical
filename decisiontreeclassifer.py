import pandas as pd
import numpy as np

listOfColNames=[]
listofent=[]


def getmetadata(df):

    def entropy(lname,setname):
        ent=0
        for i in setname:
            cnt=0
            cnt=lname.count(i)
            tcnt=len(lname)
            ent+=-((cnt/tcnt)*np.log2(cnt/tcnt))
        return ent

    # Getting columns names
    for i in df:
        listOfColNames.append(i)
    
    
    lenofcolumns=len(listOfColNames)
    for i in listOfColNames:
        name="listFor{}".format(i)
        setname="setFor{}".format(i)
        name=[]
        for j in df[i]:
            name.append(j)
        # print(name)
        setname=set(name)
        print(setname)
        ent=0
        ent=entropy(name,setname)
        print(ent)
        listofent.append(["{}".format(i),[ent]])
    # print(dictofent)
    #print(listofent)
    return listofent


class Node:
    def __init__(self,AttributeName,value=None):
            self.data=AttributeName
            self.value=value
            self.result=None
            self.children=[]
            self.parent=None

    def print_tree(self):
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + str(self.data) + str(self.value))
            if self.children:
                for child in self.children:
                    child.print_tree()
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    def add_child(self,child):
        child.parent =self
        self.children.append(child)


def decision():
    min=100
    selectedattribute=None
    
    if len(listofent)>=0:
        for i in listofent:
            #print(i[1])
            if i[1][0] < min:
                min=i[1][0]
        #print(min)
        
        for index,i in enumerate(listofent):
            if min ==i[1][0]:
                selectedattribute=i[0]
                del listofent[index]
        print(selectedattribute)
        #print(listofent)
        return selectedattribute
    else:
        return None
        # selectedattribute=
             
def BuildTree():
    cntofd=len(listofent)
    print(cntofd)
    root=Node("Root")
    p=1
    #print(selectedattribute) 
    while(cntofd!=0):
        selectedattribute=decision()
        name="listFor{}".format(selectedattribute)
        setname="setFor{}".format(selectedattribute)
        name=[]
        for i in dff[selectedattribute]:
            name.append(i)
        setname=set(name)
        print(setname)
        for k in setname:
               
            treename="T_{}".format(p)
            p+=1
            print(treename)
            treename=Node(selectedattribute)
            treename.parent=root
            root.children.append(treename)
            treename.value=k
            
        cntofd-=1
    return root



if __name__=='__main__':

    df = pd.read_csv("golf_df.csv")

    print(df)

    # delete Result column
    dff=df.iloc[:,0:-1]
listofent=getmetadata(dff)

#print(listofent)
#decision()
root=BuildTree()
root.print_tree()