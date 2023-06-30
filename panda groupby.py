import pandas as pd
import numpy as np
data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Person':['SAM','Charlie','Amy','Vanessa','carl','Sarah'],'Sales':[200,120,340,124,243,350]}
df=pd.DataFrame(data)
print(df)
bycomp=df.groupby('Company')
#by mean
print(bycomp.mean())


#by sum
print(bycomp.sum())

#by standard deviation
print(bycomp.std())
print("&&&&&&&&&")

#for specific
print(bycomp.sum().loc['FB'])

#just in one line
print(df.groupby('Company').sum().loc['FB'])


print("count")
#count
print(df.groupby('Company').count())
#or print(bycomp.count())

print("***********")
#max
print(df.groupby('Company').max())
#or print(bycomp.max())


print("min")
print(df.groupby('Company').min())

print("##############")
#describe() function
print("describe")
print(df.groupby('Company').describe())


print(df.groupby('Company').describe().transpose())


# for just one
print("$$$$$$$$$$$$$$$$$$")
print(df.groupby('Company').describe().transpose()['FB'])
