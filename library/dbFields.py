from dataclasses import dataclass, field

city_info = [
    'cityName',
    'cityNo'
]

city_gu_fields = [
    'idNo',
    'name',
    'cityNo'
]

gu_dong_fields = [
    'idNo',
    'name',
    'guNo'
]

dong_complex_fields = [
    'idNo',
    'name',
    'dongNo',
    'realEstateTypeCode',
    'cortarAddress',
    'detailAddress',
    'totalHouseholdCount',
    'totalBuildingCount',
    'highFloor',
    'lowFloor',
    'useApproveYmd'
]

complex_article_fields = [
    'idNo',
    'name',
    'complexNo'
]

article_info_fields =[
    'articleNo', 
    'articleName', 
    'exposeStartYMD', 
    'exposeEndYMD',
    'articleConfirmYMD', 
    'aptName', 
    'aptHouseholdCount',
    'aptConstructionCompanyName', 
    'aptUseApproveYmd', 
    'totalDongCount',
    'realestateTypeCode', 
    'tradeTypeName', 
    'verificationTypeCode',
    'cityName', 
    'divisionName', 
    'sectionName', 
    'householdCountByPtp',
    'walkingTimeToNearSubway', 
    'detailAddress', 
    'roomCount',
    'bathroomCount', 
    'moveInTypeCode', 
    'moveInDiscussionPossibleYN',
    'monthlyManagementCost', 
    'monthlyManagementCostIncludeItemName',
    'buildingName', 
    'articleFeatureDescription', 
    'detailDescription',
    'floorLayerName', 
    'floorInfo', 
    'priceChangeState', 
    'dealOrWarrantPrc',
    'direction', 
    'latitude', 
    'longitude',
    'entranceTypeName', 
    'rentPrice',
    'dealPrice', 
    'warrantPrice', 
    'allWarrantPrice', 
    'financePrice',
    'premiumPrice', 
    'isalePrice', 
    'allRentPrice', 
    'priceBySpace',
    'bondPrice', 
    'middlePayment', 
    'realtorName', 
    'representativeName',
    'address', 
    'representativeTelNo', 
    'cellPhoneNo', 
    'supplySpace',
    'exclusiveSpace', 
    'exclusiveRate', 
    'tagList'
]

complex_price_info_fields = [
    'idNo',
    'ptpNo',
    'date',
    'price',
    'pct_change'
]

basic_fields = [
    'cityName', 
    'cityNo', 
    'gu', 
    'dong', 
    'complex', 
    'articleNo', 
    'articleName', 
    'exposeStartYMD', 
    'exposeEndYMD', 
    'articleConfirmYMD', 
    'aptName', 
    'aptHouseholdCount', 
    'aptConstructionCompanyName', 
    'aptUseApproveYmd', 
    'totalDongCount', 
    'realestateTypeCode', 
    'tradeTypeName', 
    'verificationTypeCode', 
    'divisionName', 
    'sectionName', 
    'dongName',
    'householdCountByPtp', 
    'walkingTimeToNearSubway', 
    'detailAddress', 
    'roomCount', 
    'bathroomCount', 
    'moveInTypeCode', 
    'moveInDiscussionPossibleYN', 
    'monthlyManagementCost', 
    'monthlyManagementCostIncludeItemName', 
    'buildingName', 
    'articleFeatureDescription', 
    'detailDescription', 
    'floorLayerName', 
    'floorInfo', 
    'priceChangeState', 
    'dealOrWarrantPrc', 
    'direction', 
    'latitude', 
    'longitude', 
    'entranceTypeName', 
    'rentPrice', 
    'dealPrice', 
    'warrantPrice', 
    'allWarrantPrice', 
    'financePrice', 
    'premiumPrice', 
    'isalePrice', 
    'allRentPrice', 
    'priceBySpace', 
    'bondPrice', 
    'middlePayment', 
    'realtorName', 
    'representativeName', 
    'address', 
    'representativeTelNo', 
    'cellPhoneNo', 
    'supplySpace', 
    'exclusiveSpace', 
    'exclusiveRate', 
    'tagList', 
    'complexNo', 
    'ptpNo', 
    'date', 
    'price', 
    'pct_change',
    'fullAddress'
]

@dataclass
class Fields:
    fields_dct : dict = field(default_factory=dict)

    def __post_init__(self):
        self.fields_dct = {
            'city_info' : city_info,
            'city_gu' : city_gu_fields,
            'gu_dong' : gu_dong_fields,
            'dong_complex' : dong_complex_fields,
            'complex_article' : complex_article_fields,
            'article_info' : article_info_fields,
            'complex_price_info' : complex_price_info_fields,
            'basic_info' : basic_fields
        }


if __name__ == '__main__':

    print(Fields().fields_dct['city_gu'])