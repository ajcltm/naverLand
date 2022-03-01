import sqlite3
from pathlib import Path
from unicodedata import numeric
from numpy import where
import pandas as pd
import re

class tab1_WhereHandler:
    
    def set_where_dict(self):
        db_cols = ['cityName', 'gu', 'dong', 'complex', 'articleNo', 'articleName',
                    'dealPrice', 'realPrice',
                    'allWarrantPrice', 'householdCountByPtp', 'aptUseApproveYmd','exposeStartYMD',
                    'realestateTypeCode', 'tradeTypeName', 'search']
        
        dic ={key : None for key in db_cols}
        print(dic)

        return dic

    def get_where_clause(self, dic):
        
        lst = [item[1] for item in dic.items() if item[1] != None]

        if lst : 
            return 'where ' + ' and '.join(lst)
        
        return None

    def handle_comma(self, text, target_col):

        lst = text.split(',')

        if len(lst) >1 : 
            lst = [f'''"{i.strip()}"''' for i in lst]
            str_ = ','.join(lst)
            where = f'''{target_col} in ({str_}) '''
        else :
            where = f'''{target_col} REGEXP '^{lst[0]}' '''
        print(where)

        return where

    def handle_comma_numeric(self, text, target_col):

        lst = text.split(',')

        if len(lst)>1 : 
            lst = text.split(',')
            print(lst)
            wheres = [self.handle_numeric(i.strip(), target_col) for i in lst]
            print(f'wheres : {wheres}')
            where = ' and '.join(wheres)

        else :
            where = self.handle_numeric(text, target_col)
        
        print(f'where : {where}')

        return where

    def handle_numeric(self, text, target_col):
        correctDic = {'>' : '>', '>=':'>=', '=>':'>=', '<':'<', '<=':'<=', '<=':'<=', '=':'='}
        reverseDic = {'>' : '<', '>=':'<=', '>=':'<=', '<':'>', '=<':'>=', '<=':'>=', '=':'='}

        symbol = re.findall(r'[^\d]+', text)[0].strip()
        print(f'symbol: {symbol}')
        split_lst = text.split(symbol)
        print(f'split_lst : {split_lst}')

        for item in enumerate(split_lst):
            if len(item[1].strip())>0:
                numeric = item[1].strip()
                trueOrFalse = item[0]
            else:
                numeric, trueOrFalse = None, None

        if trueOrFalse == 0:
            final_symbol = reverseDic.get(symbol)
        else:
            final_symbol = correctDic.get(symbol)
        print(f'final_symbol : {final_symbol}')

        try :
            where = f'{target_col}' + final_symbol + numeric
        except:
            where = 'warning'
        print(where)
        return where

    def handle_searchLideEdit(self, text):

        dic = {'city': 'cityName', 'gu': 'gu', 'dong' : 'dong', 'complex' : 'complex', 
                'articleName' : 'articleName', 'articleNo' : 'articleNo', 
                'dealPrice' : 'dealPrice', 'realPrice' : 'v.price', 'allWarrant' : 'allWarrantPrice',
                'hhCount' : 'householdCountByPtp',  'ApproveYmd' : 'aptUseApproveYmd', 'exposeYMD':'exposeStartYMD', 
                'estateType': 'realestateTypeCode','tradeType' : 'tradeTypeName'}

        keys = dic.keys()
        text_ = text
        for i in keys:
            value = dic.get(i)
            text_ = text_.replace(i, value)
        return text_

class label_WhereHandler:

    def get_where_clause(self, articleNo):
        where = f'''where articleNo = {articleNo}'''
        return where


class tab4_WhereHandler:

    def get_where_clause(self, complexNo, ptpNo):
        where = f'''where idNo = {complexNo} and ptpNo = {ptpNo}'''
        return where


if __name__ == '__main__':
    text = '''dealPrice > realPrice'''

    where_content = tab1_WhereHandler().handle_searchLideEdit(text)
    print(where_content)

