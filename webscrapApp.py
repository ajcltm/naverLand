from collections import namedtuple

from datetime import datetime

import dataProvider
import forLooper
import saveLoad

gp = dataProvider.GuDataProvider()  # ex : '1168000000'
dp = dataProvider.DongDataProvider() # ex : '1168010300'
cp = dataProvider.ComplexDataProvider() # ex : '8928'
cpp = dataProvider.ComplexPriceDataProvider()
ap = dataProvider.ArticleDataProvider() # ex : '2201917900'
aip = dataProvider.ArticleInfoDataProvider()

time = datetime.now().strftime('%Y%m%d-%H%M%S')

class Create_city_gu_db :

    def excute(self):
        gu_gen = gp.get_generator()
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.GuSaver(f'naverLand({time})', f'city_gu')

        save_looper = forLooper.SavingLooper(saver)
        save_looper.handle_request(gu_gen_gen)

class Create_gu_dong_db :

    def excute(self):
        gu_gen = gp.get_generator()
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.DongSaver(f'naverLand({time})', f'gu_dong')

        save_looper = forLooper.SavingLooper(saver)
        dp_looper = forLooper.idLooper(dp, save_looper)
        dp_looper.handle_request(gu_gen_gen)

class Create_dong_complex_db :

    def excute(self):
        gu_gen = gp.get_generator()
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.ComplexSaver(f'naverLand({time})', f'dong_complex')

        save_looper = forLooper.SavingLooper(saver)
        complex_looper = forLooper.idLooper(cp, save_looper)
        dp_looper = forLooper.idLooper(dp, complex_looper)
        dp_looper.handle_request(gu_gen_gen)


class Create_complex_article_db :

    def excute(self):
        time_ = '20220122-180119'
        df = saveLoad.SqlLoader().load(f'naverLand({time_})', f'dong_complex')
        complexlst = df.idNo.unique().tolist()

        nt = namedtuple('nt', ['idNo']) 
        print(nt(complexlst[0]))
        complex_gen = (nt(k) for k in complexlst)
        complex_gen_gen = (complex_gen for k in [0])

        saver = saveLoad.ArticleSaver(f'naverLand({time})', f'complex_article')
        save_looper = forLooper.SavingLooper(saver)
        article_looper = forLooper.idLooper(ap, save_looper)
        article_looper.handle_request(complex_gen_gen)


class Create_article_info_db :

    def excute(self):
        time_ = '20220122-180119'
        df = saveLoad.SqlLoader().load(f'naverLand({time_})', f'complex_article')
        articlelst = df.idNo.unique().tolist()
        nt = namedtuple('nt', ['idNo']) 
        article_gen = (nt(k) for k in articlelst)
        article_gen_gen = (article_gen for k in [0])

        saver = saveLoad.ArticleInfoSaver(f'naverLand({time})', f'article_info')
        save_looper = forLooper.SavingLooper(saver)
        article_looper = forLooper.idLooper(aip, save_looper)
        article_looper.handle_request(article_gen_gen)


class Create_complex_price_db :

    def excute(self):
        time_ = '20220122-180119'
        df = saveLoad.SqlLoader().load(f'naverLand({time_})', f'dong_complex')
        complexlst = df.idNo.unique().tolist()
        nt = namedtuple('nt', ['idNo']) 
        print(nt(complexlst[0]))
        complex_gen = (nt(k) for k in complexlst)
        complex_gen_gen = (complex_gen for k in [0])

        saver = saveLoad.ComplexPriceSaver(f'naverLand({time})', f'complex_price_info')
        save_looper = forLooper.SavingLooper(saver)
        complex_price_looper = forLooper.idLooper(cpp, save_looper)
        complex_price_looper.handle_request(complex_gen_gen)

def main() :

    # Create_city_gu_db().excute()
    # Create_gu_dong_db().excute()
    # Create_dong_complex_db().excute()
    Create_complex_article_db().excute()
    Create_article_info_db().excute()

    Create_complex_price_db().excute()


if __name__ == '__main__' :

    main()