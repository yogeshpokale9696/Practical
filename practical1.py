# 1.
import numpy as np;
import pan as pd;

# 2.
print("Q.2")
print("Helllo World")

# 3. abs():
print("Q.3")
i = -20
print("Absoulate value of -20 is ", abs(i))

fl = -10.83
print("Absoulate value of -10.83 is ", abs(fl))

# 4.all() --- Function Writes Boolean Value - True if all Values are not null and writtens False if any one value is null
print("Q.4")
a = [-1, 2, 3, 4, 5, 6]
print(a)
print(all(a))

a = [1, False]
print(a)
print(all(a))

# 5. bin()
print("Q.5")
x = 11
y = bin(x)
print(y)

# .6 bool()
print("Q.6")
d1 = 0
d2 = True
print(d1)
print(bool(d1))
print(d2)
print(bool(d2))

# 7. bytes()
print("Q.7")
st = "Hello Welcome to python World "
print(st)
print(bytes(st, 'utf-8'))

# 8. exec()
print("Q.8")

x = 20
exec('print(x==10)')
exec('print(x==20)')
exec('x+20')
# print(x+20)
print(x == 20)

# 9. sum()
print("Q.9")
n = [1, 2, 3, 2, 4, 2, 3, 5, 2, 5]
print(sum(n))

# 10 . any()
print("Q.10")
list1 = [1]
print(any(list1))

# 11.eval()
print("Q.11")
x = 20
print(eval('x*10'))
# 12.float()
print("Q.12")
x = 9
print(type(x))

y = float(9)
print(type(y))

a = 0.4
print(type(a))
b = float(a)
print(type(b))

# 13. format()
print("Q.13")
data = "The book {price:.2f}dollars!"
print(data.format(price=150))

# 14.list
print("Q.14")
list = [1, 2, 3, 4, 5]
list_item = iter(list)
print(list)  # To print all list at a time
print(next(list_item))
for i in list_item:  # TO print element one by one
    print(i)

# 15. len()
print("Q.15")
print(len(list))

# 16.min(()
print("Q.16")

list = [1, 2, 3, 4, 0, 1, 0, 2]
print(min(list))

# 17. sorted
print("Q.17")
print(sorted(list))

# 18. set   Reapeted items not Allowed and sort in acending order
print("Q.18")
print(set(list))

# 19 input
print("Q.19")
# name=input("Enter Name \n")
print("Hello")
# print("Hello",name)

# 20. int()
print("Q.20")
val = int(20)
print(val)
val2 = int(11.52)
print(val2)
val3 = int('10')
print(val3)

# 21. pow()
print("Q.21")
print(pow(2, 3))

# 22 range()
print("Q.22")
print(range(4))
for i in range(2, 4): print(i)
for i in range(1, 20, 2): print(i)
print("round(20.2)")
print(round(20.2))
# User Defined Function

print("User Defined Functions")
# 1. Creating or declaring a function
print("Q.1")


def first_fun():
    print("MY First Function")


print("Function Declared")

# 2. Calling A function
print("Q.2")
first_fun()

# 3. Argument in Function
print("Q.3")


def summ(x, y):
    sum = x + y
    return sum


summ(10, 20)
a = summ(50, 30)
x = 100
y = 350
print("The sum of ", x, "and", y, "is:-", summ(x, y))

# 4 .Arbitrary Arguments *args
# Pass Multiple Values but no .of values are not Known
print("Q.4")


def arb(*names):
    print(names)


arb("Yogesh", "Nagesh", "Ganesh")
print("")


def add(*x):
    ans = 0
    for i in range(len(x)):
        print(x[i])
        ans = ans + x[i]
    print(ans)
    return ans


a = add(12, 13, 12, 31, 22, 5)
print("List")
l1 = [1, 2, 3, 4, 4, 5]
print(*l1)  # * Sign is used to unpack the list pr multiple elements
add(*l1)
print("Print1 function")


def print1(*x):
    for i in range(len(x)):
        print(x[i])


print1(10, 20, 30, 40, 50)

# 5 .  Argunment With key value pair
print("Q.5")


def key(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


key(1, 2, 3, 4)
key(a="Nagesh", b="Ganesh", c="Yogesh", d="Govind")

# 6. Without Argument Function
print("Q.6")


def def_fun(State="Maharashtra"):
    print("My State us : ", State)


def_fun("UP")
# if Argument is not passed Then it will Consider Default argunment
def_fun()

# 7. Passing List to function
print("Q.7")


def fruit_func(fruits):
    print(fruits)


fruits = ["apple", "banana", "cherry"]
fruit_func(fruits)

# 8. Return
print("Q.8")


def ab(a):
    return 20 + a


print(ab(20))

# 9.Local Vs Global Variables
print("Q.9")

a = 10  # global Variable


def sm():
    w = 10  # Local Variable
    return a + w


print(sm())
print(a)
# print(w)  We can't print it is local variable

# 10.lambda arguments : expression
print("Q.10")
x2 = lambda a: a + 10
print(x2(10))

x3 = lambda a: a + 20
print(x3(5))

# 11
print("Q.11")

x4 = lambda x, y, z: x + y + z
print(x4(2, 4, 5))


def myfun(n):
    x5 = lambda n: n * 10
    return x5


print(myfun(20)(10))

# Numpy Section
print("Q.1")
print("Numpy Section.............!")
dist = [10, 20, 30, 40, 50]
time = [1.2, 1.3, 1.4, 1.5, 1.5]
print(dist)
print(time)
print(len(dist))
print(type(dist))
my_num_arr = np.array(dist)
print(my_num_arr)
print(type(my_num_arr))

# Single dimension Array
print("Q.2")

single_a = np.array([1, 2, 3, 4])
print(single_a)

# Create Multi Dimension Array
print("Q.3")
m_a = np.array([(1, 2, 3), (4, 5, 6)])
print(m_a)

# 4. Check Dimension
print("Q.4")
a = np.array([[[1, 2], [3, 4]]])
print(a)
print(a.ndim)
print("B Array")
b = np.array([[[[1, 2], [3, 4]], [4, 5], [6, 7]]])
print(b)
print(b.ndim)

# 5. Check the memory Size
print("Q.5")
print("Menory size of the array:", a.itemsize)

# 6. Check the type
print("Q.6")
print("Type of the array:", a.dtype)

# 7. Size of array
print("Q.7")
print("Size")
print(a.size)

# 8. Shape
print("Q.8")
print("Shape", a.shape)

# 9 reshape
print("Q.9")
a = np.array([(1, 2, 3), (5, 6, 7)])
print(a)
print(a.ndim)

reshape_array = a.reshape(3, 2)
print(reshape_array)
print(reshape_array.ndim)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)
print(arr.ndim)
arr = arr.reshape(2, 3, 2)
# 2 arrays that contains 3 rows each with 2 elements
arr
print(arr.ndim)

# 10 . Iterating 2D array

print("Q.10")
x = np.array([[1, 2, 3, 4, 5], [3, 6, 7, 2, 8]])

for x in x:
    for y in x:
        print(y)
    print("\n")

# 11. Concatenation of 2 array
print("Q.11")
f1 = np.array([1, 2, 3])
s1 = np.array([4, 5, 6])
n_a = np.concatenate((f1, s1))
print(n_a)

# 12 sort array with numpy
print("Q.12")
arrr1 = np.array([100, 6, 66, 466, 6, 623, 23])
print("Sorted array:", np.sort(arrr1))

# 13.
print("Q.13")
print("First Element :-", arrr1[0])

# 14. array Slicing
print("Q.14")

print(arrr1)
print(arrr1[0:5])  # Start from index 1 and go to till 4
print(arrr1[-1])  # last element
print(arrr1[-3:-1])  # -3 index to -1 index
print(arrr1[-5:-1])

multi_dimensional = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(multi_dimensional)
print("Second Dimension starts from 1 index to go tail 2:", multi_dimensional[1, 0:3])
arrr1[2:]
print(arrr1)
print(arrr1[0::3])
print(arrr1[0:6:3])
print(arrr1[::2])

# 15. Find the max and min of array
print("Q.15")
print("max of array", multi_dimensional.max())
print("max of array", multi_dimensional.min())

# 16.lin-spaces
print("Q.16")
array = np.linspace(4, 7,5)
print(array)
print("It will print 5 random value between 4 to 7 : -", array)

# 17 Create array from tuple
print("Q.17")
my_tuple=((1,2),(3,2),(4,5),(8,9))
my_tup_arr=np.array(my_tuple)
print(my_tup_arr)
print(type(my_tup_arr))
print(my_tup_arr.ndim)

# copy array

print("Q.18")

x=np.array([[0,1,2,3],[4,5,6,7]])
print("x is :\n",x)
y=x.copy()
print("y is :\n",y)

