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

#merge
p=pd.merge(left,right,how='inner',on='key')
print("after merging")
print(p)


#example2
print("#################")
d1={'Key1':['K0','K0','K1','K2'],
    'Key2':['K0','K1','K0','K1'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']}
left=pd.DataFrame(d1)

d2={'Key1':['K0','K1','K1','K2'],
    'Key2':['K0','K0','K0','K0'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']}
right=pd.DataFrame(d2)

print(left)
print()
print(right)
print()

#merging

p=pd.merge(left,right,on=['Key1','Key2'])
print("after merging")
print(p)

#outer merging
p=pd.merge(left,right,how="outer",on=['Key1','Key2'])
print("after outrer merging")
print(p)