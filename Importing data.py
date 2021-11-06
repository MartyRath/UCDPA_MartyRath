#importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#importing the csv dataset and converting to dataframe using pandas
file = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Test\Property_Price_Register_Ireland-28-05-2021.csv', index_col=0)
df= pd.DataFrame(file)

#Dataframe was truncated to width 80 in Pycharm, so found the following options here to get a better overview: https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
pd.options.display.width= None
pd.options.display.max_columns= None

#print(file.head())
#print(file.shape)
#print(file.describe())

#Date is in readable format

#Missing Values
#Checking if there are missing values
missing_values = file.isnull().sum()
#print(missing_values[0:])

#what percent of these missing values against total rows minus column row
total_rows = file.shape[0] - 1

# % POSTAL_CODE missing values
#missing_values_POSTAL_CODE = file['POSTAL_CODE'].isnull().sum() / total_rows * 100
#print(missing_values_POSTAL_CODE)

# % PROPERTY_SIZE_DESC missing values
#missing_values_PROPERTY_SIZE_DESC = file['PROPERTY_SIZE_DESC'].isnull().sum() / total_rows * 100
#print(missing_values_PROPERTY_SIZE_DESC)

#With over 80% missing in both cases, using these columns won't show valuable and accurate insights
#Dropping columns



#With a budget of 110K, finding cheap properties under this price
cheap = file['SALE_PRICE'] < 100000
#cheap = file.loc[:, 'SALE_PRICE']
#cheap = file.iloc[:, 3]
print(file[cheap]) #All properties under 100000