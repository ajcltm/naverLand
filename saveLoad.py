import sqlite3
from pathlib import Path
import pandas as pd

class GuSaver:

    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{self.fileName}.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql(f'{self.tableName}', con, index=False, if_exists='append')


class DongSaver:

    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{self.fileName}.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql(f'{self.tableName}', con, index=False, if_exists='append')


class ComplexSaver:

    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{self.fileName}.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql(f'{self.tableName}', con, index=False, if_exists='append')



class ArticleSaver:

    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{self.fileName}.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql(f'{self.tableName}', con, index=False, if_exists='append')

class ArticleInfoSaver:

    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{self.fileName}.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql(f'{self.tableName}', con, index=False, if_exists='append')


class ComplexPriceSaver:

    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def create_df(self, dc):
        print(dc)
        if dc.pct_change == None :
            df = pd.DataFrame({'date':dc.date, 'price':dc.price})
            df = df.assign(pct_change = dc.pct_change)
        else :
            df = pd.DataFrame({'date':dc.date, 'price':dc.price, 'pct_change':dc.pct_change})
        df = df.assign(idNo = dc.idNo)
        df = df.loc[:, ['idNo', 'date', 'price', 'pct_change']]
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{self.fileName}.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql(f'{self.tableName}', con, index=False, if_exists='append')

class bakcUp:

    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def save_sql(self, df):
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{self.fileName}.db'
        con = sqlite3.connect(fileDir)
        df.to_sql(f'{self.tableName}', con, index=False, if_exists='append')

class SqlLoader:

    def load(self, fileName, tableName):
        print(fileName, tableName)
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        con = sqlite3.connect(fileDir)
        df = pd.read_sql(f'SELECT * FROM {tableName}', con, index_col=None)
        return df



