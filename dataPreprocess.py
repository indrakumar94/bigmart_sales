import pandas as pd
import numpy as np
from getdata import getdata

class DataPreprocess():
    def __init__(self):
        print('data preprocess init called')
        self.df = getdata.loaddata()
        print(type(self.df))
        print(self.df.head())
        print(self.df.columns)


    def cleandata(self):

        df1 = self.df
        df2 = df1.dropna()
        df3 = df2[['Item_Weight', 'Item_MRP','Item_Visibility', 'Item_Outlet_Sales']]
        print(df3.head())
        return df3


df2 = DataPreprocess().cleandata()



