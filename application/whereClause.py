import sqlite3
from pathlib import Path
from numpy import where
import pandas as pd
import re

class tab1_WhereHandler:
    
    def set_where_dict(self):
        db_cols = ['cityNo', 'gu', 'dong', 'complex', 'articleNo', 'articleName',
                    'realestateTypeCode', 'aptUseApproveYmd', 'dealPrice',
                    'wrrantPrice', 'householdCountByPtp', 'exposeStartYMD',
                    'tradeTypeName']
        
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


class label_WhereHandler:

    def get_where_clause(self, articleNo):
        where = f'''where articleNo = {articleNo}'''
        return where


class tab4_WhereHandler:

    def get_where_clause(self, complexNo):
        where = f'''where idNo = {complexNo}'''
        return where


if __name__ == '__main__':
    target_col = 'article_info.articleNo'
    text = '''222, 111'''
    tab1_WhereHandler().handle_comma(text, target_col)
    
    dic = tab1_WhereHandler().set_where_dict()
    dic = {'a' : 'a'}
    result = tab1_WhereHandler().get_where_clause(dic)
    print(result)

