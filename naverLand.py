from dataclasses import dataclass, field, asdict
from typing import List
from collections import namedtuple
import pandas as pd
import requests
import time
import sqlite3
from pathlib import Path

import dataProvider
import forLooper
import saveLoad

gp = dataProvider.GuDataProvider()  # ex : '1168000000'
dp = dataProvider.DongDataProvider() # ex : '1168010300'
cp = dataProvider.ComplexDataProvider() # ex : '8928'
cpp = dataProvider.ComplexPriceDataProvider()
ap = dataProvider.ArticleDataProvider() # ex : '2201917900'
aip = dataProvider.ArticleInfoDataProvider()

class create_city_gu_db :

    def excute(self):
        gu_gen = gp.get_generator()
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.GuSaver()

        save_looper = forLooper.SavingLooper(saver)
        save_looper.handle_request(gu_gen_gen)

class create_gu_dong_db :

    def excute(self):
        gu_gen = gp.get_generator()
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.DongSaver()

        save_looper = forLooper.SavingLooper(saver)
        dp_looper = forLooper.idLooper(dp, save_looper)
        dp_looper.handle_request(gu_gen_gen)

class create_dong_complex_db :

    def excute(self):
        gu_gen = gp.get_generator()
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.ComplexSaver()

        save_looper = forLooper.SavingLooper(saver)
        complex_looper = forLooper.idLooper(cp, save_looper)
        dp_looper = forLooper.idLooper(dp, complex_looper)
        dp_looper.handle_request(gu_gen_gen)

class create_complex_price_db :

    def excute(self):
        # gu_gen = gp.get_generator()
        # gu_gen_gen = (gu_gen for k in [0])

        # saver = saveLoad.ComplexPriceSaver()

        # save_looper = forLooper.SavingLooper(saver)
        # complex_price_looper = forLooper.idLooper(cpp, save_looper)
        # complex_looper = forLooper.idLooper(cp, complex_price_looper)
        # dp_looper = forLooper.idLooper(dp, complex_looper)
        # dp_looper.handle_request(gu_gen_gen)

        df = saveLoad.SqlLoader().load('map', 'dong_complex')
        complexlst = df.idNo.unique().tolist()
        nt = namedtuple('nt', ['idNo']) 
        print(nt(complexlst[0]))
        complex_gen = (nt(k) for k in complexlst)
        complex_gen_gen = (complex_gen for k in [0])
        saver = saveLoad.ComplexPriceSaver()
        save_looper = forLooper.SavingLooper(saver)
        complex_price_looper = forLooper.idLooper(cpp, save_looper)
        complex_price_looper.handle_request(complex_gen_gen)

class create_complex_article_db :

    def excute(self):
        df = saveLoad.SqlLoader().load('map', 'dong_complex')
        complexlst = df.idNo.unique().tolist()
        nt = namedtuple('nt', ['idNo']) 
        print(nt(complexlst[0]))
        complex_gen = (nt(k) for k in complexlst)
        complex_gen_gen = (complex_gen for k in [0])

        saver = saveLoad.ArticleSaver()
        save_looper = forLooper.SavingLooper(saver)
        article_looper = forLooper.idLooper(ap, save_looper)
        article_looper.handle_request(complex_gen_gen)

if __name__ == '__main__' :
    
    # create_city_gu_db().excute()
    # create_gu_dong_db().excute()
    # create_dong_complex_db().excute()
    # create_complex_price_db().excute()
    # create_complex_article_db().excute()
    df = saveLoad.SqlLoader().load('map', 'complex_article')
    print(df)

