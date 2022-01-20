import sqlite3
from pathlib import Path
import pandas as pd

class GuSaver:
    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'map.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql('city_gu', con, index=False, if_exists='append')


class DongSaver:

    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'map.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql('gu_dong', con, index=False, if_exists='append')


class ComplexSaver:
    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'map.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql('dong_complex', con, index=False, if_exists='append')


class ComplexPriceSaver:
    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame({'date':dc.date, 'price':dc.price})
        df = df.assign(idNo = dc.idNo)
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'complex_price_info.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql('complex_price_info', con, index=False, if_exists='append')

class ArticleSaver:
    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'map.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql('complex_article', con, index=False, if_exists='append')

class ArticleInfoSaver:
    def create_df(self, dc):
        print(dc)
        df = pd.DataFrame([dc])
        return df

    def save_sql(self, dc):
        fileDir = Path.cwd() / 'naverLand' / 'articleInfo.db'
        con = sqlite3.connect(fileDir)
        df = self.create_df(dc)
        df.to_sql('articleInfo', con, index=False, if_exists='append')

class SqlLoader:

    def load(self, fileName, tableName):
        fileDir = Path.cwd() / 'naverLand' / f'{fileName}.db'
        con = sqlite3.connect(fileDir)
        df = pd.read_sql(f'SELECT * FROM {tableName}', con, index_col=None)
        return df