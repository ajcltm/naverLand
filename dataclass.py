from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List
import saveLoad

@dataclass
class GuDC:
    idNo : str
    name : str
    cityNo : str

@dataclass
class GuDCs:
    data : list() = field(default_factory=list)

    def __post_init__(self):
        df = saveLoad.SqlLoader().load('map', 'city_gu')
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
        df = saveLoad.SqlLoader().load('map', 'gu_dong')
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
        df = saveLoad.SqlLoader().load('map', 'dong_complex')
        df_to_dict = df.to_dict('records')
        self.data = [ComplexDC(**dic) for dic in df_to_dict]

    def get_by_idNo(self, idNo):
        return [dc for dc in self.data if dc.idNo == idNo]

    def get_by_name(self, name):
        return [dc for dc in self.data if dc.name == name]
    
    def get_by_dongNo(self, dongNo):
        return [dc for dc in self.data if dc.dongNo == dongNo]


@dataclass
class ComplexPriceDC :
    idNo : str
    date : List = field(default_factory=List)
    price : List = field(default_factory=List)

@dataclass
class ArticleDC:
    idNo : str
    name : str
    complexNo : str

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