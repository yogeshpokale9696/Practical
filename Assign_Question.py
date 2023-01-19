from sys import getsizeof

import numpy as np
import pandas as pd
#from numpy import nditer

print("1.Write a NumPy program to get the numpy version and show numpy build configuration.")
#print(np.__version__)
#print(np.show_config())

print("2. Write a NumPy program to get help on the add function.")

print(np.info(np.add))

print("3. Write a NumPy program to test whether none of the elements of a given array is zero.")
a= np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(np.all(a))

print("4.Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number.")
print(np.isfinite(a))

print("5.Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.")
x=np.array([[1,2],[3,4]])
y=np.array([[6,7],[7,8]])
print(x)
print("Greater", np.greater(x, y), "\n")
print("Greater or equal ", np.greater_equal(x, y), "\n")
print("Less ", np.less(x, y), "\n")
print("Less or equal", np.less_equal(x, y), "\n")

print("6. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays")

x=np.array([[1,2],[3,4]])
y=np.array([[6.1,2.1],[7.1,4.5]])
print(x)
print(y)
print("Equal",np.equal(x,y),"\n")

print("equal Within tolerance",np.allclose(x,y))
print(np.isclose(x,y,))

print("7. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.")
arr=np.array([1,7,13,105])

print(arr.nbytes)
print()
print(getsizeof(arr))

print("8. Write a NumPy program to create an array of all the even integers from 30 to 70. ")

even=np.arange(30,70,2)
print(even)

print("9. Write a NumPy program to create a 3x3 identity matrix.")

matrix=np.eye(3)
print(matrix)

print("10. Write a NumPy program to generate a random number between 0 and 1. 11. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.")

rand=np.random.random(1)
array = np.linspace(0,1,1)
print(rand)

print("11. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution. ")

ran=np.random.normal(0,1,15)
print(ran)

print("12.Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.")

vec=np.arange(15,56)
print(vec,"\n")
print(vec[1:-1])

print("13. Write a NumPy program to create a 3X4 array using and iterate over it.")
arr3_4=np.array([[0,1,2,3],[1,2,3,4],[5,6,7,8]])
print(arr3_4.reshape(3,4))
print(arr3_4.ndim)
print(np.nditer(arr3_4))
for i in np.nditer(arr3_4):
    print(i)

print(" 14. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.")
#arbv=np.array(1)
def arb(*n):
    arbv=np.array(n)
    print(arbv)
arb(1,2,4,6,8)


print("15. Write a NumPy program to multiply the values of two given vectors. ")
x=np.array([1,2,3,4,5,6])
y=np.array([5,6,3,4,6,2])
print(x*y)

print("16. Write a NumPy program to find the number of rows and columns of a given matrix. ")

ar3_4=np.array([[0,1,2,3],[1,2,3,4],[5,6,7,8]])
print(ar3_4.reshape(3,4))
print(ar3_4.shape)

print(" 17. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1,the rest are 0.")
iden=np.identity(3)
print(iden)

print("18. Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.")

print(np.sum(ar3_4))

print(np.sum(ar3_4,axis=0))
print(np.sum(ar3_4,axis=1))

print("20. Write a NumPy program to save two given arrays into a single file in compressed format (.npz format) and load it.")
x = np.arange(10)
y = np.arange(11, 20)
print("Original arrays:")
print(x)
print(y)
np.savez('temp_arra.npz', x=x, y=y)
print("Load arrays from the 'temp_arra.npz' file:")
with np.load('temp_arra.npz') as data:
    x2 = data['x']
    y2 = data['y']
    print(x2)
    print(y2)


'''print("21.Write a NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib.")
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.2)
y = np.sin(x)
print("Plot the points using matplotlib:")
plt.plot(x, y)
plt.show()'''


print("22. Write a Pandas program to convert a NumPy array to a Pandas series. Sample NumPy array: d1 = [10, 20, 30, 40, 50]")

d1=[10,20,30,40,50]
d_s=pd.Series(d1)
print(d_s)

print("23. Write a Python Pandas program to convert the first column of a DataFrame as a Series. ")
d4=[['a',1],['b',2],['c',3]]
print(type(d4))

df1=pd.DataFrame(d4,columns=['Name','Age'])
print(df1,"\n\n")

print(df1['Name'])
pd_s=pd.Series(df1['Name'])

print(type(pd_s))

print("24. Write a Pandas program to create the mean and standard deviation of the data of a given Series.")
d1=[10,20,30,40,50]
d_s1=pd.Series(d1)
print(np.mean(d_s))
print(np.std(d_s))

print("25. Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series. ")
d1=[10,20,30,40,50]
d_s1=pd.Series(d1)

print("25% of Series ",np.percentile(d_s1,25))
print("Median=",np.median(d_s1))
print("75% of Series ",np.percentile(d_s1,75))

print("26. Write a Pandas program convert the first and last character of each word to upper case in each word of a given series.")

'''list=["yogesh","nagesh","soham","krushna"]
n_s=pd.Series(list)
#print(n_s)
#print(n_s.str.title())
print(n_s[0][0].upper())
new_s=pd.Series([])
print(type(new_s))
def first_last_upper(x):
    for i in range(0,len(x)):
       #new_s=new_s.append(pd.Series(x[i][0].upper() + x[i][1:-1] + x[i][-1].upper()))
        print(x[i][0].upper() +x[i][1:-1] + x[i][-1].upper())

#new_s=pd.series(new_s.append(n_s[0][0].upper() + n_s[0][1:-1] + n_s[0][-1].upper()))
#new_s=new_s.append(n_s[0][0].upper() + n_s[0][1:-1] + n_s[0][-1].upper())
first_last_upper(n_s)'''

'''or 
import pandas as pd
import numpy as np

list1=["yogesh","nagesh","soham","krushna"]
n_s=pd.Series(list1)
#print(n_s)
#print(n_s.str.title())
print(n_s[0][0].upper())




new_s=pd.Series(["null"])
l1=[]
def first_last_upper(x):
      for i in range(0,len(x)):
            #l1.append(x[i][0].upper() + x[i][1:-1] + x[i][-1].upper())
            z=(x[i][0].upper() +x[i][1:-1] + x[i][-1].upper())
            
            l1.append(z)
      return l1
l1=first_last_upper(n_s)
new_s=pd.Series(l1)
#new_s=pd.series(new_s.append(n_s[0][0].upper() + n_s[0][1:-1] + n_s[0][-1].upper()))
#new_s=new_s.append(n_s[0][0].upper() + n_s[0][1:-1] + n_s[0][-1].upper())

print(new_s)
'''


# or From Internet
series1 = pd.Series(['php', 'python', 'java', 'c#'])
print("Original Series:")
print(series1)
result = series1.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print("\nFirst and last character of each word to upper case:")
print(result)

print("27. Write a Pandas program to get the day of month, day of year, week number and day of week from a given series of date strings. ")

from dateutil.parser import parse
d_s = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("Original Series:")
print(d_s)
d_s = d_s.map(lambda x: parse(x))
print(d_s)
print("Day of month:")
print(d_s.dt.day.tolist())
print("Day of year:")
print(d_s.dt.dayofyear.tolist())
print("Week number:")
print(d_s.dt.weekofyear.tolist())
print("Day of week:")
from datetime import date
import calendar
print(d_s.dt.dayofweek.tolist())
day = d_s.dt.dayofweek.tolist()
print(day)
for i in day:
    x = calendar.day_name[i]
    print('Weekday name is:', x)



print("28. Write a Pandas program to compute the Euclidean distance between two given series. Euclidean distance From Wikipedia, In mathematics, the Euclidean distance or Euclidean metric is the ordinary straight-line distance between two points in Euclidean space. With this distance, Euclidean space becomes a metric space. The associated norm is called the Euclidean norm")
d3=[10,20,30,40,50]
d_s3=pd.Series(d1)
d4=[60,70,80,90,100]
d_s4=pd.Series(d4)

def eculn(x,y):
    for i in range(0,len(d_s3)):
        sub=0;
        sub=sub+np.square((y[i]+x[i]))
    return (np.sqrt(sub))
print("Euclidean distance=")
print(eculn(d_s3,d_s4))

print("29.Write a Pandas program to create a TimeSeries to display all the Sundays of given year. ")
import datetime as dt

def sun():
    year=input("Enter Year")
    week=year.dt.weekofyear.tolist()

    for i in range(0,53):
        day = dt.year.dayofweek.tolist()
        if(day==7):
            print()


Year=2002
A=calendar.TextCalendar(calendar.SUNDAY)
print(A)
for b in range(1,13):
    for k in A.itermonthdays(Year,b):
        if k!=0:
            day=date(Year,b,k)
            if day.weekday()==6:
                print("%s,%d-%d-%d" % (calendar.day_name[6] ,k,b,Year))


print("30.Write a Pandas program to compute the autocorrelations of a given numeric series.")
series = pd.Series([2, 10, 3, 4, 9, 10, 2, np.nan, 3])

print("Series is ", series)
a=series.autocorr(lag=2)
print(a)

print("31. Write a Pandas program to detect missing values of a given DataFrame. Display True or False.")
df=[[70001.0, 150.50, '2012-10-05' ,3002 ,5002.0],[np.nan ,270.65 ,'2012-09-10' ,3001 ,5003.0],[70002.0 ,65.26,np.nan,3001, 5001.0],[ 70004.0, 110.50,' 2012-08-17', 3003 ,np.nan],[np.nan ,948.50, '2012-09-10', 3002 ,5002.0],[70005.0 ,2400.60 ,'2012-07-27' ,3001 ,5001.0],[ np.nan, 5760.00 ,'2012-09-10' ,3001, 5001.0],[ 70010.0 ,1983.43 ,'2012-10-10' ,3004 ,np.nan],[70003.0, 2480.40 ,'2012-10-10' ,3003 ,5003.0],[70012.0 ,250.45 ,'2012-06-27 ',3002 ,5002.0],[np.nan, 75.29 ,'2012-08-17' ,3001 ,5003.0],[70013.0 ,3045.60, '2012-04-25 ',3001 ,np.nan]]
print(df)

df1=pd.DataFrame(df,columns=['ord_no','purch_amt','ord_date','customer_id','salesman_id'])
print(df1)
print(df1.isna())
print("\nMissing values of the said dataframe:")
print(df1.any().isna())


print("32. Write a Pandas program to identify the column(s) of a given DataFrame which have at least one missing value. ")
print(df1.isna().any())
'''print("Hello")
for i in range(0,len(df1)):
    print(i)
    #print(df1.iloc[:,i])
    print(all(df1.iloc[:, i]))
    #print(any(df1.iloc[:, i]))'''

print("33. Write a Pandas program to count the number of missing values in each column of a given DataFrame.")
print("\nNumber of missing values of the said dataframe:")
print(df1.isna().sum())

print("34. Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.")
print("\nReplace the missing values with NaN:")

df=[[70001.0, 150.50, '2012-10-05' ,3002 ,5002.0],['--' ,270.65 ,'2012-09-10' ,3001 ,5003.0],[70002.0 ,65.26,np.nan,3001, 5001.0],[ 70004.0, 110.50,' 2012-08-17', 3003 ,'??'],['?' ,948.50, '2012-09-10', 3002 ,5002.0],[70005.0 ,2400.60 ,'2012-07-27' ,3001 ,5001.0],[ np.nan, 5760.00 ,'2012-09-10' ,3001, 5001.0],[ 70010.0 ,1983.43 ,'2012-10-10' ,3004 ,np.nan],[70003.0, 2480.40 ,'2012-10-10' ,3003 ,5003.0],[70012.0 ,250.45 ,'2012-06-27 ',3002 ,5002.0],[np.nan, 75.29 ,'2012-08-17' ,3001 ,5003.0],[70013.0 ,3045.60, '2012-04-25 ',3001 ,np.nan]]
print(df1)
result = df1.replace({"?": np.nan, "--": np.nan})
print(result)