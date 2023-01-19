import pandas as pd
import itertools
from collections import Counter

data1 = [['T100', ['I1', 'I2', 'I5']],
         ['T200', ['I2', 'I4']],
         ['T300', ['I2', 'I3']],
         ['T400', ['I1', 'I2', 'I4']],
         ['T500', ['I1', 'I3']],
         ['T600', ['I2', 'I3']],
         ['T700', ['I1', 'I3']],
         ['T800', ['I1', 'I2', 'I3', 'I5']],
         ['T900', ['I1', 'I2', 'I3']]
         ]

data2 = [['T1', ['f', 'a', 'c', 'd', 'g', 'm', 'p']],
         ['T2', ['a', 'b', 'c', 'f', 'l', 'm', 'o']],
         ['T3', ['b', 'f', 'h', 'o']],
         ['T4', ['b', 'k', 'c', 'p']],
         ['T5', ['a', 'f', 'c', 'l', 'p', 'm', 'n']]
         ]

data = data2
min_sup = 3


def items(data):
    init = []
    for i in data:
        for q in i[1]:
            if (q not in init):
                init.append(q)
    init = sorted(init)
    return init


print(items(data))
list1 = sorted(items(data))

c = Counter()
for i in list1:
    for d in data:
        if (i in d[1]):
            c[i] += 1
print(c)
print("C1:")
C1 = []

for i in c:
    C1.append([i, c[i]])

L1 = []
for i in C1:
    if (i[1] >= min_sup):
        L1.append(i)
        # print(i[1])
print(L1)
dfc1 = pd.DataFrame(L1, columns=['item', 'Support'])
# print(C1)
print(dfc1)
print(sorted(dfc1))

final_df = dfc1.sort_values(by='Support', ascending=False)

print(final_df)  # Sorted
lforn = []
flforn = []
for i in data:
    for k in final_df['item']:
        if k in i[1]:
            lforn.append(k)
    flforn.append(lforn)
    lforn = []

# Sort in acending
acelist=[]
for n in final_df['item']:
    print(n)
    acelist.append(n)

acelist.reverse()
print(acelist)


print("Hello")





class TreeNode:
    def __init__(self, data):
        self.cnt = 1
        self.data = data
        self.children = []
        self.dummychild = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + str(self.data) + str(self.cnt))
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    orignalroot = TreeNode('Root')
    root = orignalroot
    for i in flforn:
        for j in i:
            flag = False
            for index, k in enumerate(root.dummychild):
                if j == k:
                    root = root.children[index]
                    root.cnt += 1
                    # print(j, "\n")
                    flag = True
            if not flag:
                r1 = root
                root = TreeNode(j)
                r1.add_child(root)
                r1.dummychild.append(j)
        root = orignalroot

    return orignalroot

# def fpchart():
#     ItemSet=[]
#     ConditionalPatternBase=[]
#     ConditionalFPTree=[]
#     FrePatternGen=[]

#     for i in acelist:
#         if (self.data == i):

#         else:
#     def print_tree(self):
#         if (self.data == i):

#         else:
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + str(self.data) + str(self.cnt))
#         if self.children:
#             for child in self.children:
#                 child.print_tree()

    root.print_tree()

root = build_product_tree()

root.print_tree()
#fpchart()
