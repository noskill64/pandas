import pandas as pd
#
#
starting = {'Col_1': [10, 11, 12, 13, 14, 15],
            'Col_2': [20, 21, 22, 23, 24, 25],
            'Col_3': [30, 31, 32, 33, 34, 35],
            'Col_4': [40, 41, 42, 43, 44, 45],
            'Col_5': [50, 51, 52, 53, 54, 55]}

df = pd.DataFrame(starting)
print(df)
print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(2))
print(df['Col_2'][2])
