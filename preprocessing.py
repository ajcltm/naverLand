from datetime import datetime
from typing import Optional, Union, List
from pydantic import BaseModel, validator
from tqdm import tqdm
from pathlib import Path
import sqlite3
import pandas as pd


class City_gu(BaseModel):
    idNo: str
    name: str
    cityNo: str


class Gu_dong(BaseModel):
    idNo: str
    name: str
    guNo: str


class Dong_complex(BaseModel):

    idNo: str
    name: str
    dongNo: str
    realEstateTypeCode: str
    cortarAddress: str
    detailAddress: str
    totalHouseholdCount: int
    totalBuildingCount: int
    highFloor: int
    lowFloor: int
    useApproveYmd: Optional[str]

    @validator('useApproveYmd')
    def datetime_validate(cls, v):
        if v:
            if len(v) >6:
                return datetime.strptime(v, '%Y%m%d').strftime('%Y-%m-%d')
            elif len(v) == 6:
                return datetime.strptime(v, '%Y%m').strftime('%Y-%m-%d')
            elif len(v) == 4:
                return datetime.strptime(v, '%y%m').strftime('%Y-%m-%d')


class Complex_article(BaseModel):
    idNo: str
    name: str
    complexNo: str


class Article_info(BaseModel):
    articleNo: str
    articleName: str
    hscpNo: str
    ptpNo: Optional[str]
    ptpName: Optional[str]
    exposeStartYMD: Optional[str]
    exposeEndYMD: Optional[str]
    articleConfirmYMD: Optional[str]
    aptName: Optional[str]
    aptHouseholdCount: Optional[int]
    aptConstructionCompanyName: Optional[str]
    aptUseApproveYmd: Optional[str]
    totalDongCount: Optional[int]
    realestateTypeCode: Optional[str]
    tradeTypeName: Optional[str]
    verificationTypeCode: Optional[str]
    cityName: Optional[str]
    divisionName: Optional[str]
    sectionName: Optional[str]
    householdCountByPtp: Optional[int]
    walkingTimeToNearSubway: Optional[int]
    detailAddress: Optional[str]
    roomCount: Optional[str]
    bathroomCount: Optional[str]
    moveInTypeCode: Optional[str]
    moveInDiscussionPossibleYN: Optional[str]
    monthlyManagementCost: Optional[int]
    monthlyManagementCostIncludeItemName: Optional[str]
    buildingName: Optional[str]
    articleFeatureDescription: Optional[str]
    detailDescription: Optional[str]
    floorLayerName: Optional[str]
    floorInfo: Optional[str]
    priceChangeState: Optional[str]
    dealOrWarrantPrc: Optional[str]
    direction: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    entranceTypeName: Optional[str]
    rentPrice: Optional[int]
    dealPrice: Optional[int]
    warrantPrice: Optional[int]
    allWarrantPrice: Optional[int]
    financePrice: Optional[int]
    premiumPrice: Optional[int]
    isalePrice: Optional[int]
    allRentPrice: Optional[int]
    priceBySpace: Optional[float]
    bondPrice: Optional[int]
    middlePayment: Optional[int]
    realtorName: Optional[str]
    representativeName: Optional[str]
    address: Optional[str]
    representativeTelNo: Optional[str]
    cellPhoneNo: Optional[str]
    supplySpace: Optional[float]
    exclusiveSpace: Optional[float]
    exclusiveRate: Optional[float]
    tagList: Optional[str]


    @validator('*')
    def zero_validate(cls, v):
        if v == 0:
            return None
        else:
            return v

    @validator('exposeStartYMD', 'exposeEndYMD', 'articleConfirmYMD', 'aptUseApproveYmd')
    def exposeStartYMD_validate(cls, v):
        if v:
            if len(v) >6:
                return datetime.strptime(v, '%Y%m%d').strftime('%Y-%m-%d')
            elif len(v) == 6:
                return datetime.strptime(v, '%Y%m').strftime('%Y-%m-%d')
            elif len(v) == 4:
                return datetime.strptime(v, '%y%m').strftime('%Y-%m-%d')

    @validator('articleFeatureDescription', 'detailDescription', 'tagList')
    def articleFeatureDescription_validator(cls, v):
        if v:
            return v.replace("'", "")

    @validator('roomCount', 'bathroomCount', pre=True)
    def roomCount_validator(cls, v):
        if v == '-':
            return None
        else:
            return v

class Complex_price_info(BaseModel):
    idNo: Optional[str]
    ptpNo: Optional[str]
    date: Optional[str]
    price: Optional[int]
    pct_change: Optional[float]

class Pct_chagne(BaseModel):
    file_path : Path
    pct_change : List[Union[float, None]]

    @validator('pct_change', pre=True)
    def get_pct_change(cls, v, values):
        con = sqlite3.connect(values['file_path'])
        cur = con.cursor()
        query = 'select * from complex_price_info'
        df = pd.read_sql(query, con, index_col=None)
        df['pct_change'] = df.groupby(['idNo', 'ptpNo']).price.pct_change()
        df = df.where(pd.notnull(df), None)
        pct_change_lst=df.loc[:, 'pct_change'].to_list()
        return pct_change_lst

class Query:

    def get_query(self, table, data):
        dic = data.dict()
        values = dic.values()

        values_part_lst = [self.get_string_format(value) for value in values]
        values_part = ', '.join(values_part_lst)
        query = f'''INSERT INTO {table} VALUES ({values_part})'''
        return query

    def get_string_format(self, value):
        if type(value) == str:
            return f"'{value}'"
        elif value == None:
            return "Null"
        else:
            return f'{value}'


