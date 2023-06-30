import numpy as np
import pandas as pd
d={'col1':[1,2,3,4],
   'col2':[444,555,666,444],
   'col3':['abc','def','ghi','xyz']}
df=pd.DataFrame(d)
print(df.head())
print()

#finding unique value
print("finding unique value")
print(df['col2'].unique())


#length of unique values
print(len(df['col2'].unique()))

#or by usig inbuilt function nunique()

print(df['col2'].nunique())
print()
print()

#using value count
p=df['col2'].value_counts()
print(p)
print()
print()

#selection

p=df[df['col1']>2]
print(p)
print()

#selection
p=df[(df['col1']>2) & (df['col2']==444)]
print(p)
print()
print()

#using of apply method

def times2(x):
    return 2*x
p=df['col1'].apply(times2)
print(p)



print()
p=df['col2'].apply(lambda x:x*2 )
print(p)
print()
print()

#sorting by some column
p=df.sort_values('col2')
# or p=df.sort_values(by='col2)
print(p)