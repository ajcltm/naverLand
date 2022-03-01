from pathlib import Path
from datetime import datetime
import sqlite3

import preprocessing

from pydantic import parse_obj_as
from typing import List
from tqdm import tqdm

class Merge:

    def __init__(self, fileLst):
        self.fileLst = fileLst
        self.tableLst = ['city_gu', 'gu_dong', 'dong_complex', 'complex_article', 'article_info', 'complex_price_info']
        self.city_gu_field = ['idNo', 'name', 'cityNo']
        self.city_gu_field_type = ['TEXT', 'TEXT', 'TEXT']

        self.gu_dong_field = ['idNo', 'name', 'guNo']
        self.gu_dong_field_type = ['TEXT', 'TEXT', 'TEXT']

        self.dong_complex_field = ['idNo', 'name', 'dongNo', 'realEstateTypeCode', 'cortarAddress', 'detailAddress', 'totalHouseholdCount', 'totalBuildingCount', 'highFloor', 'lowFloor', 'useApproveYmd']
        self.dong_complex_field_type = ['TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER', 'DATE']
        
        self.complex_article_field = ['idNo', 'name', 'complexNo']
        self.complex_article_field_type = ['TEXT', 'TEXT', 'TEXT']

        self.article_info_field = ['articleNo', 'articleName', 'hscpNo', 'ptpNo', 'ptpName',
         'exposeStartYMD', 'exposeEndYMD',
        'articleConfirmYMD', 'aptName', 'aptHouseholdCount',
        'aptConstructionCompanyName', 'aptUseApproveYmd', 'totalDongCount',
        'realestateTypeCode', 'tradeTypeName', 'verificationTypeCode',
        'cityName', 'divisionName', 'sectionName', 'householdCountByPtp',
        'walkingTimeToNearSubway', 'detailAddress', 'roomCount',
        'bathroomCount', 'moveInTypeCode', 'moveInDiscussionPossibleYN',
        'monthlyManagementCost', 'monthlyManagementCostIncludeItemName',
        'buildingName', 'articleFeatureDescription', 'detailDescription',
        'floorLayerName', 'floorInfo' , 'priceChangeState', 'dealOrWarrantPrc',
        'direction', 'latitude', 'longitude',
        'entranceTypeName', 'rentPrice',
        'dealPrice', 'warrantPrice', 'allWarrantPrice', 'financePrice',
        'premiumPrice', 'isalePrice', 'allRentPrice', 'priceBySpace',
        'bondPrice', 'middlePayment', 'realtorName', 'representativeName',
        'address', 'representativeTelNo', 'cellPhoneNo', 'supplySpace',
        'exclusiveSpace', 'exclusiveRate', 'tagList']

        self.article_info_field_type = ['TEXT', 'TEXT', 'TEXT', 'TEXT', 'Text',
         'DATE', 'DATE',
        'DATE', 'TEXT', 'INTEGER',
        'TEXT', 'DATE', 'INTEGER',
        'TEXT', 'TEXT', 'TEXT',
        'TEXT', 'TEXT', 'TEXT', 'INTEGER',
        'INTEGER', 'TEXT', 'INTEGER',
        'INTEGER', 'TEXT', 'TEXT',
        'INTEGER', 'TEXT',
        'TEXT', 'TEXT', 'TEXT',
        'TEXT', 'INTEGER' , 'TEXT', 'TEXT',
        'TEXT', 'INTEGER', 'INTEGER',
        'TEXT', 'INTEGER',
        'INTEGER', 'INTEGER', ' INTEGER', 'INTEGER',
        'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER',
        'INTEGER', 'INTEGER', 'TEXT', 'TEXT',
        'TEXT', 'TEXT', 'TEXT', 'REAL',
        'REAL', 'REAL', 'TEXT']

        self.complex_price_info_field = ['idNo', 'ptpNo','date', 'price', 'pct_change']
        self.complex_price_info_field_type = ['TEXT', 'TEXT','DATE', 'INTEGER', 'REAL']

        self.file_path = self.create_file()
        self.con_ = sqlite3.connect(self.file_path)
        self.cur_ = self.con_.cursor()

    def create_file(self, fileName = None):
        filePath = self.get_file_path(fileName)
        con = sqlite3.connect(filePath)
        cur = con.cursor()

        field_lst = self.make_create_table_query()

        for i, table in enumerate(self.tableLst):
            field = field_lst[i]
            field_part = ', '.join(field)
            query = f'CREATE TABLE {table} ({field_part})'
            cur.execute(query)
        con.commit()
        cur.close()

        return filePath

    def get_file_path(self, fileName):
        dir = Path.cwd().joinpath('naverLand', 'db')
        if fileName:
            filePath = dir / f'{fileName}.db'
        else :
            time = datetime.now().strftime('%Y%m%d-%H%M%S')
            filePath = dir / f'naverLand({time}).db'
        return filePath

    def make_create_table_query(self):
        city_gu = [' '.join([field, self.city_gu_field_type[i]]) for i, field in enumerate(self.city_gu_field)]
        gu_dong = [' '.join([field, self.gu_dong_field_type[i]]) for i, field in enumerate(self.gu_dong_field)]
        dong_complex = [' '.join([field, self.dong_complex_field_type[i]]) for i, field in enumerate(self.dong_complex_field)]
        complex_article = [' '.join([field, self.complex_article_field_type[i]]) for i, field in enumerate(self.complex_article_field)]
        article_info = [' '.join([field, self.article_info_field_type[i]]) for i, field in enumerate(self.article_info_field)]
        complex_price_info = [' '.join([field, self.complex_price_info_field_type[i]]) for i, field in enumerate(self.complex_price_info_field)]
        return [city_gu, gu_dong, dong_complex, complex_article, article_info, complex_price_info]


    def merge_file(self):
        self.merge_city_gu()
        self.merge_gu_dong()
        self.merge_dong_complex()
        self.merge_complex_article()
        self.merge_article_info()
        self.merge_complex_price_info()
        self.con_.close()

    def merge_city_gu(self):

        self.cur_.execute('BEGIN TRANSACTION')
        for f in self.fileLst:
            print('='*150, f'now working with the file : {f}', sep='\n')
            con, cur = self.get_selected_cursor(f, 'city_gu')
            print('='*100, f'now inserting data : city_gu', sep='\n')
            data = self.get_dict_format_lst(cur, self.city_gu_field)
            city_gu_lst = parse_obj_as(List[preprocessing.City_gu], data)
            self.implement_query(city_gu_lst, 'city_gu')
        self.cur_.execute('END TRANSACTION')
        con.close()

    def merge_gu_dong(self):

        self.cur_.execute('BEGIN TRANSACTION')
        for f in self.fileLst:
            print('='*150, f'now working with the file : {f}', sep='\n')
            con, cur = self.get_selected_cursor(f, 'gu_dong')
            print('='*100, f'now inserting data : gu_dong', sep='\n')
            data = self.get_dict_format_lst(cur, self.gu_dong_field)
            gu_dong_lst = parse_obj_as(List[preprocessing.Gu_dong], data)
            self.implement_query(gu_dong_lst, 'gu_dong')
        self.cur_.execute('END TRANSACTION')
        con.close()

    def merge_dong_complex(self):

        self.cur_.execute('BEGIN TRANSACTION')
        for f in self.fileLst:
            print('='*150, f'now working with the file : {f}', sep='\n')
            con, cur = self.get_selected_cursor(f, 'dong_complex')
            print('='*100, f'now inserting data : dong_complex', sep='\n')
            data = self.get_dict_format_lst(cur, self.dong_complex_field)
            dong_complex_lst = parse_obj_as(List[preprocessing.Dong_complex], data)
            self.implement_query(dong_complex_lst, 'dong_complex')
        self.cur_.execute('END TRANSACTION')
        con.close()


    def merge_complex_article(self):

        self.cur_.execute('BEGIN TRANSACTION')
        for f in self.fileLst:
            print('='*150, f'now working with the file : {f}', sep='\n')
            con, cur = self.get_selected_cursor(f, 'complex_article')
            print('='*100, f'now inserting data : complex_article', sep='\n')
            data = self.get_dict_format_lst(cur, self.complex_article_field)
            complex_article_lst = parse_obj_as(List[preprocessing.Complex_article], data)
            self.implement_query(complex_article_lst, 'complex_article')
        self.cur_.execute('END TRANSACTION')
        con.close()

    def merge_article_info(self):

        self.cur_.execute('BEGIN TRANSACTION')
        for f in self.fileLst:
            print('='*150, f'now working with the file : {f}', sep='\n')
            con, cur = self.get_selected_cursor(f, 'article_info')
            print('='*100, f'now inserting data : article_info', sep='\n')
            data = self.get_dict_format_lst(cur, self.article_info_field)
            article_info_lst = parse_obj_as(List[preprocessing.Article_info], data)
            self.implement_query(article_info_lst, 'article_info')
        self.cur_.execute('END TRANSACTION')
        con.close()

    def merge_complex_price_info(self):
        self.cur_.execute('BEGIN TRANSACTION')
        for f in self.fileLst:
            print('='*150, f'now working with the file : {f}', sep='\n')
            con, cur = self.get_selected_cursor(f, 'complex_price_info')
            print('='*100, f'now inserting data : complex_price_info', sep='\n')
            data = self.get_dict_format_lst(cur, self.complex_price_info_field)
            pct_change_lst = self.get_pct_change(f)
            data = self.replace_pct_change(data, pct_change_lst)
            complex_price_info_lst = parse_obj_as(List[preprocessing.Complex_price_info], data)
            self.implement_query(complex_price_info_lst, 'complex_price_info')
        self.cur_.execute('END TRANSACTION')
        con.close()

    def get_pct_change(self, f):
        data = preprocessing.Pct_chagne(file_path=f, pct_change=[])
        return data.pct_change

    def replace_pct_change(self, dic_lst, pct_change_lst):
        for i, dic in enumerate(dic_lst):
            dic['pct_change'] = pct_change_lst[i]
        return dic_lst

    def get_selected_cursor(self, filePath, table):
        con = sqlite3.connect(filePath)
        cur = con.cursor()
        query = f'select * from {table}'
        cur.execute(query)
        return con, cur 

    def get_dict_format_lst(self, cur, feild):
        data = []
        for row in cur.fetchall():
            dic = {key : row[i] for i, key in enumerate(feild)}
            data.append(dic)
        return data

    def implement_query(self, lst, table):
        for values in tqdm(lst, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
            query = preprocessing.Query().get_query(table, values)
            self.cur_.execute(query)
        

if __name__ == '__main__':
    file = Path.cwd().joinpath('naverLand', 'db', 'naverLand(20220205-152900).db')
    file_ = Path.cwd().joinpath('naverLand', 'db', 'naverLand(20220207-231600).db')
    Merge([file, file_]).merge_file()


        

