import pandas as pd
import dataclass
import saveLoad
import forLooper

from datetime import datetime


time = datetime.now().strftime('%Y%m%d-%H%M%S')

class BackUp_city_gu_table :

    def excute(self):
        data = dataclass.GuDCs().data
        print('=*100', 'df_to_dict : ', data, sep='\n')

        df = pd.DataFrame(data)

        saver = saveLoad.bakcUp(f'naverLand({time})', 'city_gu')
        saver.save_sql(df)


class BackUp_gu_dong_table :

    def excute(self):
        data = dataclass.DongDCs().data
        print('=*100', 'df_to_dict : ', data, sep='\n')
        df = pd.DataFrame(data)

        saver = saveLoad.bakcUp(f'naverLand({time})', 'gu_dong')
        saver.save_sql(df)


class BackUp_dong_complex_table :

    def excute(self):
        data = dataclass.ComplexDCs().data
        print('=*100', 'df_to_dict : ', data, sep='\n')
        df = pd.DataFrame(data)

        saver = saveLoad.bakcUp(f'naverLand({time})', 'dong_complex')
        saver.save_sql(df)


class BackUp_complex_article_table :

    def excute(self):
        data = dataclass.ArticleDCs().data
        print('=*100', 'df_to_dict : ', data, sep='\n')
        df = pd.DataFrame(data)

        saver = saveLoad.bakcUp(f'naverLand({time})', 'complex_article')
        saver.save_sql(df)


class BackUp_article_info_table :

    def excute(self):
        data = dataclass.ArticleInfoDCs().data
        print('=*100', 'df_to_dict : ', data, sep='\n')
        df = pd.DataFrame(data)

        saver = saveLoad.bakcUp(f'naverLand({time})', 'article_info')
        saver.save_sql(df)


class BackUp_complex_price_info_table :

    def excute(self):
        data = dataclass.ComplexPriceDCs().data
        print('=*100', 'df_to_dict : ', data, sep='\n')
        data_ = [{'idNo':[i.idNo for k in range(len(i.date))], 'date':i.date, 'price':i.price, 'pct_change':i.pct_change} for i in data]
        df = pd.concat([pd.DataFrame(i) for i in data_])

        saver = saveLoad.bakcUp(f'naverLand({time})', 'complex_price_info')
        saver.save_sql(df)



def main():
    BackUp_city_gu_table().excute()
    BackUp_gu_dong_table().excute()
    BackUp_dong_complex_table().excute()
    BackUp_complex_article_table().excute()
    BackUp_article_info_table().excute()
    BackUp_complex_price_info_table().excute()


if __name__ == '__main__':
    main()
