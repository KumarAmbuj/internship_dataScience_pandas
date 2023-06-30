import pandas as pd
import numpy as np
labels=['a','b','c']
mydata=[10,20,30]
arr=np.array(mydata)
d={'a':10,'b':20,'c':30}

a=pd.Series(data=[sum,print,len])
print(a)


ser1=pd.Series([1,2,3,4,5],['India','Usa','Japan','Australia','WI'])
print(ser1)

ser2=pd.Series([1,2,5,4],['India','Usa','Italy','Japan'])
print(ser2)


print(ser1['Usa'])

print(ser1+ser2)