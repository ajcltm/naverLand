import sqlite3
from pathlib import Path
from numpy import where
import pandas as pd
import re

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

time_str = '(20220302-011045)'

class Tab1_table:

    def get_data(self, where=None):
        fileName = f'naverLand{time_str}'
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        print(fileDir)
        conn = sqlite3.connect(fileDir)
        conn.create_function("REGEXP", 2, regexp)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cols = ['city_info.cityName as cityName', 'city_gu.cityNo', 'city_gu.name as gu', 'gu_dong.name as dong', 'dong_complex.name as complex',
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
                'v.complexNo as complexNo', 'v.ptpNo as ptpNo', 'v.date as date', 'v.price as price',
                '(dong_complex.cortarAddress || " " || dong_complex.detailAddress) as fullAddress']

        cols_str = ', '.join(cols)

        outer_join_1 = f'left outer join complex_article on article_info.articleNo = complex_article.idNo'

        outer_join_2 = f'left outer join dong_complex on complex_article.complexNo = dong_complex.idNo'

        outer_join_3 = f'left outer join gu_dong on dong_complex.dongNo = gu_dong.idNo'

        outer_join_4 = f'left outer join city_gu on gu_dong.guNo = city_gu.idNo'

        outer_join_5 = f'left outer join city_info on city_gu.cityNo = city_info.cityNo'

        outer_join_6 = f'inner join (select c.*, max(c.price) from (SELECT a.* from complex_price_info as a join (select complex_price_info.idNo, max(complex_price_info.date) as date from complex_price_info group by complex_price_info.idNo) b on a.idNO = b.idNo and a.date = b.date) as c group by c.idNo) as v on v.idNo = complex_article.complexNo'

        outer_join_6 = f'left outer join (select complex_price_info.idNo as complexNo, complex_price_info.ptpNo as ptpNo, max(complex_price_info.date) as date, complex_price_info.price as price from complex_price_info group by complexNo, ptpNo) v on v.complexNo=article_info.hscpNo and v.ptpNo = article_info.ptpNo'

        if where==None:
            sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4} {outer_join_5} {outer_join_6}'
            print('='*100, f'sql : {sql}', sep='\n')
                
        else :
            sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4} {outer_join_5} {outer_join_6} {where}'
            print('='*100, f'sql : {sql}', sep='\n')
        
        try:
            cur.execute(sql)
            dic = []
            for row in cur.fetchall():
                dic.append({key : row[key] for key in row.keys()})
            conn.close()
            return dic
        except :
            return None


class Tab4_table:

    def get_data(self, where=None):
        fileName = f'naverLand{time_str}'
        fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
        conn = sqlite3.connect(fileDir)
        conn.create_function("REGEXP", 2, regexp)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        if where==None:
            sql = f'select date, price from complex_price_info'
            cur.execute(sql)
        else :
            sql = f'select date, price from complex_price_info {where}'
            cur.execute(sql)

        dic = []
        for row in cur.fetchall():
            dic.append({key : row[key] for key in row.keys()})
        conn.close()

        return dic

# if __name__ == '__main__':
    # ex : '1100000000' -> seoul / '4100000000' -> guenggi

    # data = [['서울시', '1100000000'], ['경기도', '4100000000']]

    # fileName = f'naverLand{time_str}.db'
    # fileDir = Path.cwd() / 'naverLand' / 'db' / fileName

    # conn = sqlite3.connect(fileDir)
    # cur = conn.cursor()

    # query = f'create table city_info (cityName Text, cityNo Text)'
    # cur.execute(query)

    # for i in data :
    #     query = f'''insert into city_info values ('{i[0]}', {i[1]})'''
    #     print(query)
    #     cur.execute(query)
    # conn.commit()
    
    # conn.close()


    # fileName = 'naverLand(20220207-231600).db'
    # fileDir = Path.cwd() / 'naverLand' / 'db' / fileName

    # conn = sqlite3.connect(fileDir)
    # cur = conn.cursor()

    # query = 'select * from city_gu'
    # cur.execute(query)

    # for row in cur.fetchall():
    #     query = f"insert into city_gu values ('{row[0]}', '{row[1]}', 4100000000)"
    #     cur.execute(query)
    
    # conn.commit()
    # conn.close()