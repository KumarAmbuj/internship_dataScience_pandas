import pandas as pd
import numpy as np

d1={'key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']}

d2={'key':['K0','K1','K2','K3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']}

left=pd.DataFrame(d1)
right=pd.DataFrame(d2)

print(left)
print()
print(right)
print()

left.to_csv('mycsvfile',index=False)

df=pd.read_csv('mycsvfile')
print(df)

right.to_csv('mycsvfile',index=False)
df=pd.read_csv('mycsvfile')
print(df)
print()
print()

#not to write index
left.to_csv('mycsvfile2')
df=pd.read_csv('mycsvfile2')
print(df)

