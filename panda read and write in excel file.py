import pandas as pd


# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 40, 50, 60, 70]})


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('myexcelfile', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

df=pd.read_excel('myexcelfile',sheet_name='Sheet1')
print(df)