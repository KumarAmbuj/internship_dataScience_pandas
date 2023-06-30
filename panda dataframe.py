import pandas as pd
import numpy as np
from numpy.random import randn
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print("$$$$$$$$$$$")
print(df['W'])
print(type(df['W']))
print(type(df))

print("&&&&&&&&&0")
a=df['W']
print(a)
print("&&&&&&&&&&&&")

print(df[['W','Z']])
#new column
df['new']=df['W']+df['Y']
print(df)


print("@@@@@@@@@@@@")
#droping of column

df.drop('new',axis=1,inplace=True)
print(df)

#removing row like D
#for permanently removing we use inplace = True
df.drop('D',axis=0,inplace=True)
print(df)

print(df.shape)

#selecting rows
print(df.loc['A'])
#selcting multiple rows
print(df.loc[['A','B']])

#selecting rows way 2
print(df.iloc[0])



#selection of specific item or data
print("@@@@@@@@@")
print(df.loc['B','Y'])
print(df.iloc[1,2])

#selection of subgroups
print(df.loc[['A','B'],['W','Y']])

