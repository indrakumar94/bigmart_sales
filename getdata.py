#import sqlalchemy
#import psycopg2
import pandas as pd

class getdata():
    def __init__(self):
        self.data = []

    """def loaddata():
        engine = sqlalchemy.create_engine("postgresql://postgres:indrakumar@7@localhost/abcd")
        con = engine.connect()
        data = pd.read_sql_query('select * from bigmart_sales', con = engine)
        return data"""

    def loadxls():
        data = pd.read_csv('Train.csv')
        return data

df = getdata.loadxls()
print(df.head())
print(type(df))


