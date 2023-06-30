import pandas as pd
import numpy as  np
d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df=pd.DataFrame(d)
print(df)
#deleting row having NaN value
print(df.dropna())

#deleting column having NaN value
print(df.dropna(axis=1))

#deleting row which dont have atleast 2 numeric value
print(df.dropna(thresh=2))

#deleting row which dont have atleast 1 numeric value
print(df.dropna(thresh=1))

#deleting row which dont have atleast 3 numeric value
print(df.dropna(thresh=3))

#printing vlaue in nan place
print(df.fillna(value="Fill value" ))

print(df)

print("$$$$$$$$$$")
print(df['A'].fillna(value=df['A'].mean()))



