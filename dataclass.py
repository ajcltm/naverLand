from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List

@dataclass
class GuDC:
    idNo : str
    name : str
    cityNo : str


@dataclass
class DongDC:
    idNo : str
    name : str
    guNo : str


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

    tagList : List = field(default_factory=List)