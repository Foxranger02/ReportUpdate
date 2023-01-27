import pandas

df = pandas.read_csv("handwashing_report.csv")
namess = list(df['name'])
name  = list(set(namess))

df2 = df.groupby(["name"]).count().sort_values('date')

result = list(df2.index)
print(result)