import pandas as pd
x = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Property Price Register Datasets\Property_Price_Register_Ireland-28-05-2021.csv')
#print(x.head())

df=pd.DataFrame(x)
#print(df.head())
#print(df.columns)
#print(df.info())
#print(df.describe())

#df.shape - how many rows, columns
#df.values - data values in 2D Numpy array
#df.columns - Shows columns
#f.index

print(df['SALE_PRICE'])
