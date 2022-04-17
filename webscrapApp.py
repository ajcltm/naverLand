from collections import namedtuple
from dataclasses import dataclass

from pathlib import Path
from datetime import datetime
import pandas as pd

import dataProvider
import forLooper
import saveLoad

gp = dataProvider.GuDataProvider()  # ex : '1100000000' -> seoul / '4100000000' -> guenggi
dp = dataProvider.DongDataProvider() # ex : '1168010300'
cp = dataProvider.ComplexDataProvider() # ex : '8928'
cpp = dataProvider.ComplexPriceDataProvider()
ap = dataProvider.ArticleDataProvider() # ex : '2201917900'
aip = dataProvider.ArticleInfoDataProvider()

time = datetime.now().strftime('%Y%m%d-%H%M%S')


class Create_city_gu_db :

    def excute(self, city, dbName=None):
        gu_gen = gp.get_generator(city)
        gu_gen_gen = (gu_gen for k in [0])

        if not dbName:
            saver = saveLoad.GuSaver(f'naverLand({time})', f'city_gu')
        else:
            saver = saveLoad.GuSaver(f'{dbName}', f'city_gu')

        save_looper = forLooper.SavingLooper(saver)
        save_looper.handle_request(gu_gen_gen)

class Create_gu_dong_db :

    def excute(self):
        gu_gen = gp.get_generator(city)
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.DongSaver(f'naverLand({time})', f'gu_dong')

        save_looper = forLooper.SavingLooper(saver)
        dp_looper = forLooper.idLooper(dp, save_looper)
        dp_looper.handle_request(gu_gen_gen)

class Create_dong_complex_db :

    def excute(self):
        gu_gen = gp.get_generator(city)
        gu_gen_gen = (gu_gen for k in [0])

        saver = saveLoad.ComplexSaver(f'naverLand({time})', f'dong_complex')

        save_looper = forLooper.SavingLooper(saver)
        complex_looper = forLooper.idLooper(cp, save_looper)
        dp_looper = forLooper.idLooper(dp, complex_looper)
        dp_looper.handle_request(gu_gen_gen)


class Create_complex_article_db :
   
    def excute(self):
        df = saveLoad.SqlLoader().load(f'naverLand({time})', f'dong_complex')
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

    def excute(self, dbName=None):
        if not dbName :
            df = saveLoad.SqlLoader().load(f'naverLand({time})', f'complex_article')
        else:
            self.dbName = dbName
            df = saveLoad.SqlLoader().load(f'{dbName}', f'complex_article')
        articlelst = df.idNo.unique().tolist()
        if dbName:
            i = self.get_nonExisted_index(dbName, articlelst)
            articlelst = articlelst[i:]
        nt = namedtuple('nt', ['idNo']) 
        article_gen = (nt(k) for k in articlelst)
        article_gen_gen = (article_gen for k in [0])
        if not dbName:
            saver = saveLoad.ArticleInfoSaver(f'naverLand({time})', f'article_info')
        else:
            saver = saveLoad.ArticleInfoSaver(f'{dbName}', f'article_info')
        save_looper = forLooper.SavingLooper(saver)
        article_looper = forLooper.idLooper(aip, save_looper)
        article_looper.handle_request(article_gen_gen)

    def get_nonExisted_index(self, dbName, lst):
        q = saveLoad.SqlLoader().load(f'{dbName}', f'article_info')
        if not isinstance(q, pd.DataFrame):
            return 0
        existed_lst = [i['articleNo'] for i in q.to_dict(orient='records')]

        for i in lst:
            if not i in existed_lst:
                return lst.index(i)

@dataclass
class ComplexPriceInputDC:
    idNo : str
    ptpNo : str

class Create_complex_price_db :
    def excute(self, dbName):
        if not dbName :
            df = saveLoad.SqlLoader().load(f'naverLand({time})', f'article_info')
        else:
            self.dbName = dbName
            df = saveLoad.SqlLoader().load(f'{dbName}', f'article_info')
        lst = df[['hscpNo', 'ptpNo']].drop_duplicates().dropna(how="all").to_dict(orient='records')
        lst = [ComplexPriceInputDC(idNo=i['hscpNo'], ptpNo=i['ptpNo']) for i in lst]
        if dbName:
            i = self.get_nonExisted_index(dbName, lst)
            lst = lst[i:]
        
        unique_dc_gen = (dc for dc in lst) 
        unique_dc_gen_gen = (unique_dc_gen for i in [0])
        if not dbName:
            saver = saveLoad.ComplexPriceSaver(f'naverLand({time})', f'complex_price_info')
        else:
            saver = saveLoad.ComplexPriceSaver(f'{dbName}', f'complex_price_info')
        save_looper = forLooper.SavingLooper(saver)
        complex_price_looper = forLooper.id_ptpNo_Looper(cpp, save_looper)
        complex_price_looper.handle_request(unique_dc_gen_gen)

    
    def get_nonExisted_index(self, dbName, lst):
        q = saveLoad.SqlLoader().load(f'{dbName}', f'complex_price_info')
        if not isinstance(q, pd.DataFrame):
            return 0
        q_ = q[['idNo', 'ptpNo']].to_dict(orient='records')
        existed_lst = [ComplexPriceInputDC(idNo=i['idNo'], ptpNo=i['ptpNo']) for i in q_]
        ix = lst.index(existed_lst[-1])
        return ix + 1


        # for i in lst:
        #     if not i in existed_lst:
        #         return lst.index(i)


def main() :

    Create_city_gu_db().excute(city=4100000000, dbName='naverLand(20220407-005031)')  # ex : '1100000000' -> seoul / '4100000000' -> guenggi
    # Create_gu_dong_db().excute()
    # Create_dong_complex_db().excute()
    
    # Create_complex_article_db().excute()
    # Create_article_info_db().excute(dbName='naverLand(20220407-005031)')
    # Create_complex_price_db().excute(dbName='naverLand(20220407-005031)')


if __name__ == '__main__' :

    main()