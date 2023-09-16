import pandas as pd

# merging all csv files
df = pd.concat(
    map(pd.read_csv, ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']), ignore_index=True)
# print(df)
remove_dollar = lambda x: float(x.replace('$', ''))

# apply the lambda function to the 'salary' column
df['price'] = df['price'].apply(remove_dollar)

df.drop(df[df['product'] != 'pink morsel'].index, inplace=True)
df['sales'] = df['quantity']*df['price']
df.drop(['product', 'price', 'quantity'], axis=1, inplace=True)

print(df)
df.to_csv('output.csv', index=False)
