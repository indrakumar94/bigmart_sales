from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pandas as pd
from dataPreprocess import DataPreprocess
class linearreg():
    def __init__(self):
        self.data = DataPreprocess().cleandata()
        print('hello')

    #def evalmetrics(self, y_test, y_pred):
        #rms = np.sqrt(mean_squared_error(y_test, y_pred))
        #mae = mean_absolute_error(y_test, y_pred)
        #r2 = r2_score(y_test, y_pred)
        #return rms, mae, r2


    def makemodel(self):
        print('hi')
        X = self.data.drop('Item_Outlet_Sales', axis=1).values
        y = self.data['Item_Outlet_Sales'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(X_test)
        rms = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print("rms", rms)
        print("mae", mae)
        print("r2", r2)
        return regressor



linearreg().makemodel()




