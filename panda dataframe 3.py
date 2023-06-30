import pandas as pd
from  numpy.random import randn

outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hierindex=list(zip(outside,inside))
hierindex=pd.MultiIndex.from_tuples(hierindex)
print(outside)
print(inside)
print(hierindex)

df=pd.DataFrame(randn(6,2),hierindex,['A','B'])
print(df)

#for G1
print(df.loc['G1'])

#indexing in G1
print("@@@@@@@@@@@")
print(df.loc['G1'].loc[1])


#indexing more for single data
print(df.loc['G1'].loc[1,'B'])

#making index
print("**********")
df.index.names=['Groups','Num']
print(df)
print("*********")


#way 2
print("@@@@@@@@@@@@")
print(df.xs)
print("@@@@@@@@")

print(df.xs('G1'))


print(df.xs(1,level='Num'))
