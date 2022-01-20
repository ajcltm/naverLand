from collections import namedtuple
import pandas as pd
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


class create_article_info_db :

    def excute(self):
        df = saveLoad.SqlLoader().load('map', 'complex_article')
        articlelst = df.idNo.unique().tolist()
        nt = namedtuple('nt', ['idNo']) 
        article_gen = (nt(k) for k in articlelst)
        article_gen_gen = (article_gen for k in [0])

        saver = saveLoad.ArticleInfoSaver()
        save_looper = forLooper.SavingLooper(saver)
        article_looper = forLooper.idLooper(aip, save_looper)
        article_looper.handle_request(article_gen_gen)

if __name__ == '__main__' :
    
    import dataclass

    create_city_gu_db().excute()
    create_gu_dong_db().excute()
    create_dong_complex_db().excute()
    create_complex_article_db().excute()
    create_article_info_db().excute()

    # create_complex_price_db().excute()

    # dcs = dataclass.GuDCs()
    # print('='*100, 'data :', dcs.data, sep='\n')
    # print('='*100, 'get_by_idNo result :', dcs.get_by_idNo('1162000000'), sep='\n')
    # print('='*100, 'get_by_name result :', dcs.get_by_name('강남구'), sep='\n')
    # print('='*100, 'get_by_cityNo result :', dcs.get_by_cityNo('1100000000'), sep='\n')

    # print('='*100, 'AND result', [i for i in dcs.get_by_cityNo('1100000000') if i in dcs.get_by_name('강남구')], sep='\n')
    # print('='*100, 'OR result', dcs.get_by_cityNo('1100000000') + dcs.get_by_name('강남구'), sep='\n')



    # dcs = dataclass.DongDCs()
    # print('='*100, 'data :', dcs.data, sep='\n')
    # print('='*100, 'get_by_idNo result :', dcs.get_by_idNo('1168010300'), sep='\n')
    # print('='*100, 'get_by_name result :', dcs.get_by_name('화곡동'), sep='\n')
    # print('='*100, 'get_by_guNo result :', dcs.get_by_guNo('1150000000'), sep='\n')

    # print('='*100, 'AND result', [i for i in dcs.get_by_guNo('1150000000') if i in dcs.get_by_name('화곡동')], sep='\n')
    # print('='*100, 'OR result', dcs.get_by_guNo('1150000000') + dcs.get_by_name('화곡동'), sep='\n')

    # dcs = dataclass.ComplexDCs()
    # print('='*100, 'data :', dcs.data, sep='\n')
    # print('='*100, 'get_by_idNo result :', dcs.get_by_idNo('8928'), sep='\n')
    # print('='*100, 'get_by_name result :', dcs.get_by_name('LG개포자이'), sep='\n')
    # print('='*100, 'get_by_dongNo result :', dcs.get_by_dongNo('1168010300'), sep='\n')

    # print('='*100, 'AND result', [i for i in dcs.get_by_dongNo('1168010300') if i in dcs.get_by_name('LG개포자이')], sep='\n')
    # print('='*100, 'OR result', dcs.get_by_dongNo('1168010300') + dcs.get_by_name('LG개포자이'), sep='\n')

    # filter = pd.DataFrame([{'name' : i.name, 'count': i.totalHouseholdCount} for i in dcs.data if i.totalHouseholdCount>4000])
    # print('='*100, 'filter result', filter, sep='\n')
