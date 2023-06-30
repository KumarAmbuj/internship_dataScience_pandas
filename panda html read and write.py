import pandas as pd
data=pd.read_html('https://www.imdb.com/search/title?groups=top_250&sort=user_rating')
print(type(data))
print(data[0])

print(data)
print("###########")
print(data[0].head())


print("222222222222222222222")
data=pd.read_html('https://www.lawctopus.com/academike/crime-crime-rates/')
print(type(data))
print(data)


print("example33333333333")
url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'

tips = pd.read_csv(url)
print(tips)
