parentPath='c:/Users/ajcltm/PycharmProjects/naverLand'
import sys
sys.path.append(parentPath)
from library import dbFields

import dataclasses
import sqlite3


class GeneralQuery :

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
    
    def get(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        attr = self.get_attr(sql)
        _dataclass = dataclasses.make_dataclass('Data', attr)
        data = (_dataclass(**{key: data[i] for i, key in enumerate(attr)}) for data in cur.fetchall())
        return data

    def get_attr(self, sql):
        sql = sql.replace(',', '')
        lst = sql.split()
        s = lst.index('select')
        e = lst.index('from')
        attr = lst[s+1:e]
        if attr[0] == '*':
            table_name = lst[e+1]
            attr = dbFields.Fields().fields_dct[table_name]
        return attr

class BasicQuery:

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def get(self, where=None):
        self.conn.row_factory = sqlite3.Row
        cur = self.conn.cursor()

        cols = ['city_info.cityName as cityName', 'city_gu.cityNo', 'city_gu.name as gu', 'gu_dong.name as dong', 'dong_complex.name as complex',
                'article_info.articleNo', 'article_info.articleName', 'article_info.exposeStartYMD', 'article_info.exposeEndYMD',
                'article_info.articleConfirmYMD', 'article_info.aptName', 'article_info.aptHouseholdCount',
                'article_info.aptConstructionCompanyName', 'article_info.aptUseApproveYmd', 'article_info.totalDongCount',
                'article_info.realestateTypeCode', 'article_info.tradeTypeName', 'article_info.verificationTypeCode',
                'article_info.cityName', 'article_info.divisionName', 'article_info.sectionName', 'article_info.householdCountByPtp',
                'article_info.walkingTimeToNearSubway', 'article_info.detailAddress', 'article_info.roomCount',
                'article_info.bathroomCount', 'article_info.moveInTypeCode', 'article_info.moveInDiscussionPossibleYN',
                'article_info.monthlyManagementCost', 'article_info.monthlyManagementCostIncludeItemName',
                'article_info.buildingName', 'article_info.articleFeatureDescription as articleFeatureDescription', 'article_info.detailDescription',
                'article_info.floorLayerName', 'article_info.floorInfo', 'article_info.priceChangeState', 'article_info.dealOrWarrantPrc',
                'article_info.direction', 'article_info.latitude', 'article_info.longitude',
                'article_info.entranceTypeName', 'article_info.rentPrice',
                'article_info.dealPrice', 'article_info.warrantPrice', 'article_info.allWarrantPrice', 'article_info.financePrice',
                'article_info.premiumPrice', 'article_info.isalePrice', 'article_info.allRentPrice', 'article_info.priceBySpace',
                'article_info.bondPrice', 'article_info.middlePayment', 'article_info.realtorName', 'article_info.representativeName',
                'article_info.address', 'article_info.representativeTelNo', 'article_info.cellPhoneNo', 'article_info.supplySpace',
                'article_info.exclusiveSpace', 'article_info.exclusiveRate', 'article_info.tagList',
                'v.complexNo as complexNo', 'v.ptpNo as ptpNo', 'v.date as date', 'v.price as price', 'v.pct_change as pct_change',
                '(dong_complex.cortarAddress || " " || dong_complex.detailAddress) as fullAddress']

        cols_str = ', '.join(cols)

        outer_join_1 = f'left outer join complex_article on article_info.articleNo = complex_article.idNo'

        outer_join_2 = f'left outer join dong_complex on complex_article.complexNo = dong_complex.idNo'

        outer_join_3 = f'left outer join gu_dong on dong_complex.dongNo = gu_dong.idNo'

        outer_join_4 = f'left outer join city_gu on gu_dong.guNo = city_gu.idNo'

        outer_join_5 = f'left outer join city_info on city_gu.cityNo = city_info.cityNo'

        outer_join_6 = f'inner join (select c.*, max(c.price) from (SELECT a.* from complex_price_info as a join (select complex_price_info.idNo, max(complex_price_info.date) as date from complex_price_info group by complex_price_info.idNo) b on a.idNO = b.idNo and a.date = b.date) as c group by c.idNo) as v on v.idNo = complex_article.complexNo'

        outer_join_6 = f'left outer join (select complex_price_info.idNo as complexNo, complex_price_info.ptpNo as ptpNo, max(complex_price_info.date) as date, complex_price_info.price as price, complex_price_info.pct_change as pct_change from complex_price_info group by complexNo, ptpNo) v on v.complexNo=article_info.hscpNo and v.ptpNo = article_info.ptpNo'

        if where :
            sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4} {outer_join_5} {outer_join_6} {where}'
        else :
            sql = f'select {cols_str} from article_info {outer_join_1} {outer_join_2} {outer_join_3} {outer_join_4} {outer_join_5} {outer_join_6}'
        cur.execute(sql)
        attr = dbFields.Fields().fields_dct['basic_info']
        _dataclass = dataclasses.make_dataclass('Data', attr)
        return (_dataclass(**{key: data[i] for i, key in enumerate(attr)}) for data in cur.fetchall())

if __name__ == '__main__':
    from pathlib import Path
    file_name = 'naverLand(20220309-132731)_preprocessed.db'
    db_path = Path().cwd().joinpath('naverLand', 'db', file_name)
    print(db_path)
    # sql = f'select * from article_info'
    # q = Query(db_path).get(sql)
    # print(list(q)[:1])
    q = BasicQuery(db_path).get(where="where dealPrice<price ")
    print([(data.complex, data.dealPrice, data.price) for data in list(q)][:10])

