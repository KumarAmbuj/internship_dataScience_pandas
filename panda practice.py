import numpy as np
import pandas as pd
labels=['a','b','c']
mydata=[10,20,30]
arr=np.array(mydata)
d={'a':10,'b':20,'c':30}
print(labels)
print(mydata)
print(arr)
print(d)

a=pd.Series(data=mydata)
print(a)

print("#############")
a=pd.Series(index=labels,data=mydata)
print(a)

a=pd.Series(data=mydata,index=labels)
print(a)

#other way
print("2nd way")
b=pd.Series(mydata,labels)
print(b)

b=pd.Series(labels,mydata)
print(b)

c=pd.Series(arr)
print(c)

c=pd.Series(arr,labels)
print(c)


#for dictionary
print("using dictionary")
e=pd.Series(d)
print(e)