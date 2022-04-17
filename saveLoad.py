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
            if len(dc.price)>0:
                df = pd.DataFrame({'date':dc.date, 'price':dc.price})
                df = df.assign(pct_change = dc.pct_change)
            else:
                df = pd.DataFrame({'date':None, 'price':None}, index=[0])
                df = df.assign(pct_change = dc.pct_change)
        else :
            if len(dc.price)>0:
                df = pd.DataFrame({'date':dc.date, 'price':dc.price, 'pct_change':dc.pct_change})
            else :
                df = pd.DataFrame({'date':None, 'price':None, 'pct_change':None}, index=[0])
        df = df.assign(idNo = dc.idNo)
        df = df.assign(ptpNo = dc.ptpNo)
        df = df.loc[:, ['idNo', 'ptpNo', 'date', 'price', 'pct_change']]
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
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        print('='*100, f'fileDir: \n {fileDir}', sep='\n')
        con = sqlite3.connect(fileDir)
        try:
            df = pd.read_sql(f'SELECT * FROM {tableName}', con, index_col=None)
        except:
            df = None
        return df



