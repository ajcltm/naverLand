import sqlite3
from pathlib import Path
import pandas as pd


class Init_tab1_table:

    def get_data(self):
        time_str = '(20220122-181419)'
        fileName = f'naverLand{time_str}'
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        print(fileDir)
        conn = sqlite3.connect(fileDir)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()


        cols = ['city_gu.cityNo', 'city_gu.name as city', 'gu_dong.name as dong', 'dong_complex.name as complex',
                'article_info.articleNo', 'article_info.articleName', 'article_info.realestateTypeCode', 
                'article_info.aptUseApproveYmd', 'article_info.dealPrice', 'article_info.warrantPrice',
                'article_info.householdCountByPtp','article_info.exposeStartYMD', 'article_info.tradeTypeName']
        cols_str = ', '.join(cols)
        print('='*100, f'cols_str : {cols_str}', sep='\n')

        outer_join_1 = f'left outer join complex_article on article_info.articleNo = complex_article.idNo'

        outer_join_2 = f'left outer join dong_complex on complex_article.complexNo = dong_complex.idNo'

        outer_join_3 = f'left outer join gu_dong on dong_complex.dongNo = gu_dong.idNo'

        outer_join_4 = f'left outer join city_gu on gu_dong.guNo = city_gu.idNo'

        sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4}'
        print('='*100, f'sql : {sql}', sep='\n')
        cur.execute(sql)

        dic = []
        for row in cur.fetchall():
            dic.append({key : row[key] for key in row.keys()})
        print('='*100, f'sql : {dic[45]}', sep='\n')
        conn.close()

        return dic

if __name__ == '__main__':
    
    init = Init_tab1_table().get_data()
    print('='*100, f'result : {init[20]}', sep='\n')



    

