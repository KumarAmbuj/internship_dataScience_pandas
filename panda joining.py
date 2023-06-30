import pandas as pd
import numpy as np

d1={'A':['A0','A1','A2'],
    'B':['B0','B1','B2']}
d2={'C':['C0','C2','C3'],
    'D':['D0','D2','D3']
}

left=pd.DataFrame(d1,index=['K0','K1','K2'])
right=pd.DataFrame(d2,index=['K0','K2','K3'])

print(left)
print()
print(right)
print()

#joining
p=left.join(right)
print(p)

#inner join
print('inner join')
p=left.join(right,how='inner')
print(p)
print()

#outer join
print('outer join')
p=left.join(right,how='outer')
print(p)

