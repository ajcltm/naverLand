from dataclasses import dataclass, field, asdict
import pandas as pd
from datetime import datetime
from typing import List
import saveLoad

@dataclass
class GuDC:
    idNo : str
    name : str
    cityNo : str

time = '20220122-180119'

@dataclass
class GuDCs:
    data : list() = field(default_factory=list)

    def __post_init__(self):
        df = saveLoad.SqlLoader().load(f'naverLand({time})', 'city_gu')
        df_to_dict = df.to_dict('records')
        self.data = [GuDC(**dic) for dic in df_to_dict]

    def get_by_idNo(self, idNo):
        return [dc for dc in self.data if dc.idNo == idNo]

    def get_by_name(self, name):
        return [dc for dc in self.data if dc.name == name]
    
    def get_by_cityNo(self, cityNo):
        return [dc for dc in self.data if dc.cityNo == cityNo]
        


@dataclass
class DongDC:
    idNo : str
    name : str
    guNo : str


@dataclass
class DongDCs:
    data : list() = field(default_factory=list)

    def __post_init__(self):
        df = saveLoad.SqlLoader().load(f'naverLand({time})', 'gu_dong')
        df_to_dict = df.to_dict('records')
        self.data = [DongDC(**dic) for dic in df_to_dict]

    def get_by_idNo(self, idNo):
        return [dc for dc in self.data if dc.idNo == idNo]

    def get_by_name(self, name):
        return [dc for dc in self.data if dc.name == name]
    
    def get_by_guNo(self, guNo):
        return [dc for dc in self.data if dc.guNo == guNo]


@dataclass
class ComplexDC:
    idNo : str
    name : str
    dongNo : str
    realEstateTypeCode : str
    cortarAddress : str
    detailAddress :str
    totalHouseholdCount : str
    totalBuildingCount : str
    highFloor : int
    lowFloor : int
    useApproveYmd : str


@dataclass
class ComplexDCs:
    data : list() = field(default_factory=list)

    def __post_init__(self):
        df = saveLoad.SqlLoader().load(f'naverLand({time})', 'dong_complex')
        df_to_dict = df.to_dict('records')
        self.data = [ComplexDC(**dic) for dic in df_to_dict]

    def get_by_idNo(self, idNo):
        return [dc for dc in self.data if dc.idNo == idNo]

    def get_by_name(self, name):
        return [dc for dc in self.data if dc.name == name]
    
    def get_by_dongNo(self, dongNo):
        return [dc for dc in self.data if dc.dongNo == dongNo]


@dataclass
class ArticleDC:
    idNo : str
    name : str
    complexNo : str


@dataclass
class ArticleDCs:
    data : list() = field(default_factory=list)

    def __post_init__(self):
        df = saveLoad.SqlLoader().load(f'naverLand({time})', 'complex_article')
        df_to_dict = df.to_dict('records')
        self.data = [ArticleDC(**dic) for dic in df_to_dict]

    def get_by_idNo(self, idNo):
        return [dc for dc in self.data if dc.idNo == idNo]

    def get_by_name(self, name):
        return [dc for dc in self.data if dc.name == name]
    
    def get_by_dongNo(self, dongNo):
        return [dc for dc in self.data if dc.dongNo == dongNo]



@dataclass
class ArticleInfoDC:
    articleNo : str
    articleName : str
    exposeStartYMD : str
    exposeEndYMD : str
    articleConfirmYMD : str
    aptName : str
    aptHouseholdCount : str
    aptConstructionCompanyName : str
    aptUseApproveYmd : str
    totalDongCount : str
    realestateTypeCode : str
    tradeTypeName : str
    verificationTypeCode : str
    cityName : str
    divisionName : str
    sectionName : str
    householdCountByPtp : str
    walkingTimeToNearSubway : str
    detailAddress : str
    roomCount : str
    bathroomCount : str
    moveInTypeCode : str
    moveInDiscussionPossibleYN : str
    monthlyManagementCost : str
    monthlyManagementCostIncludeItemName : str
    buildingName : str
    articleFeatureDescription : str
    detailDescription : str
    floorLayerName : str

    floorInfo : str
    priceChangeState : str
    dealOrWarrantPrc : str
    direction : str
    latitude : str
    longitude : str
    entranceTypeName : str

    rentPrice : str
    dealPrice : str
    warrantPrice : str
    allWarrantPrice : str
    financePrice : str
    premiumPrice : str
    isalePrice : str
    allRentPrice : str
    priceBySpace : str
    bondPrice : str
    middlePayment : str

    realtorName : str
    representativeName : str
    address : str
    representativeTelNo : str
    cellPhoneNo : str

    supplySpace : str
    exclusiveSpace : str
    exclusiveRate : str

    # tagList : List = field(default_factory=List)
    tagList : str


@dataclass
class ArticleInfoDCs:
    data : list() = field(default_factory=list)

    def __post_init__(self):
        df = saveLoad.SqlLoader().load(f'naverLand({time})', 'article_Info')
        df.loc[:, 'exposeStartYMD'] = pd.to_datetime(df.exposeStartYMD, format='%Y%m%d')
        df.loc[:, 'exposeEndYMD'] = pd.to_datetime(df.exposeEndYMD, format='%Y%m%d')
        df.loc[:, 'articleConfirmYMD'] = pd.to_datetime(df.articleConfirmYMD, format='%Y%m%d')
        df.aptHouseholdCount = df.aptHouseholdCount.astype('int')
        # df.loc[:, 'aptUseApproveYmd'] = pd.to_datetime(df.aptUseApproveYmd, format='%Y%m')
        df.totalDongCount = df.totalDongCount.astype('int')
        df.householdCountByPtp = df.householdCountByPtp.astype('int')
        df.walkingTimeToNearSubway = df.walkingTimeToNearSubway.astype('int')
        df.roomCount = df.roomCount.apply(pd.to_numeric, errors = 'coerce')
        df.monthlyManagementCost = df.monthlyManagementCost.apply(pd.to_numeric, errors = 'coerce')
        df.rentPrice = df.rentPrice.apply(pd.to_numeric, errors = 'coerce')
        df.dealPrice = df.dealPrice.apply(pd.to_numeric, errors = 'coerce')
        df.warrantPrice = df.warrantPrice.apply(pd.to_numeric, errors = 'coerce')
        df.allWarrantPrice = df.allWarrantPrice.apply(pd.to_numeric, errors = 'coerce')
        df.financePrice = df.financePrice.apply(pd.to_numeric, errors = 'coerce')
        df.premiumPrice = df.premiumPrice.apply(pd.to_numeric, errors = 'coerce')
        df.isalePrice = df.isalePrice.apply(pd.to_numeric, errors = 'coerce')
        df.allRentPrice = df.allRentPrice.apply(pd.to_numeric, errors = 'coerce')
        df.priceBySpace = df.priceBySpace.apply(pd.to_numeric, errors = 'coerce')
        df.bondPrice = df.bondPrice.apply(pd.to_numeric, errors = 'coerce')
        df.middlePayment = df.middlePayment.apply(pd.to_numeric, errors = 'coerce')
        df.bondPrice = df.bondPrice.apply(pd.to_numeric, errors = 'coerce')

        df_to_dict = df.to_dict('records')
        self.data = [ArticleInfoDC(**dic) for dic in df_to_dict]

    def get_by_idNo(self, idNo):
        return [dc for dc in self.data if dc.idNo == idNo]

    def get_by_name(self, name):
        return [dc for dc in self.data if dc.name == name]


@dataclass
class ComplexPriceDC :
    idNo : str
    pct_change : float
    date : List = field(default_factory=List)
    price : List = field(default_factory=List)


@dataclass
class ComplexPriceDCs :
    data : list() = field(default_factory=list)

    def __post_init__(self):
        df = saveLoad.SqlLoader().load(f'naverLand({time})', 'complex_price_info')
        df.loc[:, 'date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
        df = df.assign(pct_change = df.groupby(['idNo']).price.pct_change().apply(lambda x: round(x, 3)))
        date_dict = df.groupby(['idNo'])['date'].apply(list).to_dict()
        price_dict = df.groupby(['idNo'])['price'].apply(list).to_dict()
        pct_dict = df.groupby(['idNo'])['pct_change'].apply(list).to_dict()
        df_to_dict = ({'idNo':key, 'date':date_dict.get(key), 'price':price_dict.get(key), 'pct_change' : pct_dict.get(key)
                        } for key in date_dict.keys())
        self.data = [ComplexPriceDC(**dic) for dic in df_to_dict]
