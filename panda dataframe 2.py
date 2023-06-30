import pandas as pd
import numpy as np
from numpy.random import randn
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#for printing true or false
print("********")
print(df>0)
#or b=df>0
#print(b)
print("***********")

#for printing nan
print("############")
b=df>0
print(df[b])
#or print(df[df>0])
print("#################")


print(df['W']>0)

# returns all rows in Z having value greater than zero
print(df[df['Z']<0])

# returns all rows in W having value greater than zero
print(df[df['W']>0])

##
print("<<<<<<<<<<<<<")
print(df[df['W']>0][['Y','X']])
print("<<<<<<<<<<<<<")

#selecting selected rows
print(df[(df['W']>0) & (df['Z']>0)])


print(df.reset_index())

print(df)

#implementing new column
print("#########")
newind='CA NY HS WY CZ'.split()
df['states']=newind
print(df)
print("##############")

print(df.set_index('states'))

print(df)
