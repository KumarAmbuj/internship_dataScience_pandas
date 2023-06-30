import pandas as pd
import numpy as np
d1={'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']}

d2={'A':['A4','A5','A5','A6'],
    'B':['B4','B5','B5','B6'],
    'C':['C4','C5','C5','C6'],
    'D':['D4','D5','D5','D6']}

d3={'A':['A8','A9','A10','A11'],
    'B':['B8','B9','B10','B11'],
    'C':['C8','C9','C10','C11'],
    'D':['D8','D9','D10','D11']}

df1=pd.DataFrame(d1,index=[0,1,2,3])
df2=pd.DataFrame(d2,index=[4,5,6,7])
df3=pd.DataFrame(d3,index=[8,9,10,11])

print(df1)
print()
print(df2)
print()
print(df3)

print("$$$$$$$$$$")
#concatenating
#print(pd.concat([df1,df2,df3]))
p=pd.concat([df1,df2,df3])
print(p)


print()
print("********")
p=pd.concat([df1,df2,df3],axis=1)
print(p)