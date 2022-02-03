import sqlite3
from pathlib import Path
from numpy import where
import pandas as pd
import re

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None


class Tab1_table:

    def get_data(self, where=None):
        time_str = '(20220122-181419)'
        fileName = f'naverLand{time_str}'
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        print(fileDir)
        conn = sqlite3.connect(fileDir)
        conn.create_function("REGEXP", 2, regexp)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()


        # cols = ['city_gu.cityNo', 'city_gu.name as gu', 'gu_dong.name as dong', 'dong_complex.name as complex',
        #         'article_info.articleNo', 'article_info.articleName', 'article_info.realestateTypeCode', 
        #         'article_info.aptUseApproveYmd', 'article_info.dealPrice', 'article_info.warrantPrice',
        #         'article_info.householdCountByPtp','article_info.exposeStartYMD', 'article_info.tradeTypeName',
        #         'v.idNo as complexNo', 'v.date', 'v.price']

        cols = ['city_gu.cityNo', 'city_gu.name as gu', 'gu_dong.name as dong', 'dong_complex.name as complex',
                'article_info.articleNo', 'article_info.articleName', 'article_info.exposeStartYMD', 'article_info.exposeEndYMD',
                'article_info.articleConfirmYMD', 'article_info.aptName', 'article_info.aptHouseholdCount',
                'article_info.aptConstructionCompanyName', 'article_info.aptUseApproveYmd', 'article_info.totalDongCount',
                'article_info.realestateTypeCode', 'article_info.tradeTypeName', 'article_info.verificationTypeCode',
                'article_info.cityName', 'article_info.divisionName', 'article_info.sectionName', 'article_info.householdCountByPtp',
                'article_info.walkingTimeToNearSubway', 'article_info.detailAddress', 'article_info.roomCount',
                'article_info.bathroomCount', 'article_info.moveInTypeCode', 'article_info.moveInDiscussionPossibleYN',
                'article_info.monthlyManagementCost', 'article_info.monthlyManagementCostIncludeItemName',
                'article_info.buildingName', 'article_info.articleFeatureDescription', 'article_info.detailDescription',
                'article_info.floorLayerName', 'article_info.floorInfo', 'article_info.priceChangeState', 'article_info.dealOrWarrantPrc',
                'article_info.direction', 'article_info.latitude', 'article_info.longitude',
                'article_info.entranceTypeName', 'article_info.rentPrice',
                'article_info.dealPrice', 'article_info.warrantPrice', 'article_info.allWarrantPrice', 'article_info.financePrice',
                'article_info.premiumPrice', 'article_info.isalePrice', 'article_info.allRentPrice', 'article_info.priceBySpace',
                'article_info.bondPrice', 'article_info.middlePayment', 'article_info.realtorName', 'article_info.representativeName',
                'article_info.address', 'article_info.representativeTelNo', 'article_info.cellPhoneNo', 'article_info.supplySpace',
                'article_info.exclusiveSpace', 'article_info.exclusiveRate', 'article_info.tagList',
                'v.idNo as complexNo', 'v.date', 'v.price']

        cols_str = ', '.join(cols)
        print('='*100, f'cols_str : {cols_str}', sep='\n')

        outer_join_1 = f'left outer join complex_article on article_info.articleNo = complex_article.idNo'

        outer_join_2 = f'left outer join dong_complex on complex_article.complexNo = dong_complex.idNo'

        outer_join_3 = f'left outer join gu_dong on dong_complex.dongNo = gu_dong.idNo'

        outer_join_4 = f'left outer join city_gu on gu_dong.guNo = city_gu.idNo'

        outer_join_5 = f'inner join (\
                        select c.*, max(c.price)\
                        from (\
                            SELECT a.*\
                            from complex_price_info as a\
                            join (select complex_price_info.idNo, max(complex_price_info.date) as date from complex_price_info group by complex_price_info.idNo) b\
                            on a.idNO = b.idNo and a.date = b.date) as c\
                            group by c.idNO\
                        ) as v on v.idNo = complex_article.complexNo'

        if where==None:
            sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4} {outer_join_5}'
            print('='*100, f'sql : {sql}', sep='\n')

        #sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4} inner join complex_price on complex_article.complexNo = complex_price.idNo where complex_price.idNo in (select complex_price.idNo from complex_price where complex_price.date in (select min(complex_price.date) from complex_price group by complex_price.idNo))'
        #print('='*100, f'sql : {sql}', sep='\n')

            cur.execute(sql)        
        else :
            sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4} {outer_join_5} {where}'
            print('='*100, f'sql : {sql}', sep='\n')
            cur.execute(sql)

        dic = []
        for row in cur.fetchall():
            dic.append({key : row[key] for key in row.keys()})
        # print('='*100, f'sql : {dic[45]}', sep='\n')
        conn.close()

        return dic

class label:

    def get_data(self, where=None):
        time_str = '(20220122-181419)'
        fileName = f'naverLand{time_str}'
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        print(fileDir)
        conn = sqlite3.connect(fileDir)
        conn.create_function("REGEXP", 2, regexp)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        if where==None:
            pass
        else :
            cols = [
                'article_info.articleNo', 'article_info.articleName', 'article_info.exposeStartYMD', 'article_info.exposeEndYMD',
                'article_info.articleConfirmYMD', 'article_info.aptName', 'article_info.aptHouseholdCount',
                'article_info.aptConstructionCompanyName', 'article_info.aptUseApproveYmd', 'article_info.totalDongCount',
                'article_info.realestateTypeCode', 'article_info.tradeTypeName', 'article_info.verificationTypeCode',
                'article_info.cityName', 'article_info.divisionName', 'article_info.sectionName', 'article_info.householdCountByPtp',
                'article_info.walkingTimeToNearSubway', 'article_info.detailAddress', 'article_info.roomCount',
                'article_info.bathroomCount', 'article_info.moveInTypeCode', 'article_info.moveInDiscussionPossibleYN',
                'article_info.monthlyManagementCost', 'article_info.monthlyManagementCostIncludeItemName',
                'article_info.buildingName', 'article_info.articleFeatureDescription', 'article_info.detailDescription',
                'article_info.floorLayerName', 'article_info.floorInfo', 'article_info.priceChangeState', 'article_info.dealOrWarrantPrc',
                'article_info.direction', 'article_info.latitude', 'article_info.longitude',
                'article_info.entranceTypeName', 'article_info.rentPrice',
                'article_info.dealPrice', 'article_info.warrantPrice', 'article_info.allWarrantPrice', 'article_info.financePrice',
                'article_info.premiumPrice', 'article_info.isalePrice', 'article_info.allRentPrice', 'article_info.priceBySpace',
                'article_info.bondPrice', 'article_info.middlePayment', 'article_info.realtorName', 'article_info.representativeName',
                'article_info.address', 'article_info.representativeTelNo', 'article_info.cellPhoneNo', 'article_info.supplySpace',
                'article_info.exclusiveSpace', 'article_info.exclusiveRate', 'article_info.tagList'
                ]
            cols_str = ', '.join(cols)
            sql = f'select {cols_str} from article_info {where}'
            print('='*100, f'sql : {sql}', sep='\n')
            cur.execute(sql)

        dic = []
        for row in cur.fetchall():
            dic.append({key : row[key] for key in row.keys()})
        # print('='*100, f'sql : {dic[45]}', sep='\n')
        conn.close()

        return dic

class Tab4_table:

    def get_data(self, where=None):
        time_str = '(20220122-181419)'
        fileName = f'naverLand{time_str}'
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        print(fileDir)
        conn = sqlite3.connect(fileDir)
        conn.create_function("REGEXP", 2, regexp)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        if where==None:
            sql = f'select date, price from complex_price_info'
            print('='*100, f'sql : {sql}', sep='\n')
            cur.execute(sql)
        else :
            sql = f'select date, price from complex_price_info {where}'
            print('='*100, f'sql : {sql}', sep='\n')
            cur.execute(sql)

        dic = []
        for row in cur.fetchall():
            dic.append({key : row[key] for key in row.keys()})
        # print('='*100, f'sql : {dic[45]}', sep='\n')
        conn.close()

        return dic

if __name__ == '__main__':

    from datetime import datetime

    # data = Tab1_table().get_data()
    # print('='*100, f'data : {data[1]}', sep='\n')

    time_str = '(20220122-181419)'
    fileName = f'naverLand{time_str}'
    fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
    print(fileDir)
    conn = sqlite3.connect(fileDir)
    sql = 'select * from article_info'
    df = pd.read_sql(sql, conn, index_col=None)
    print(df.columns)
    

    # time_str = '(20220122-181419)'
    # fileName = f'naverLand{time_str}'
    # fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
    # print(fileDir)
    # conn = sqlite3.connect(fileDir)
    # cur = conn.cursor()

    # cur.execute('create table complex_price (idNo str, date datetime, price integer, pct_change null)')

    # # conn.commit()

    # # cur.execute('DROP TABLE complex_price')

    # cur.execute('select * from complex_price_info')

    # for row in cur.fetchall():
    #     row_ = (row[0], datetime.strptime(row[1], '%Y-%m-%d'), row[2], row[3])
    #     cur.execute('insert into complex_price values (?, ?, ?, ?)', row_)

    # conn.commit()
    # conn.close()

