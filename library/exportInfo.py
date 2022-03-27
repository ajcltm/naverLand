def export_article(dict_data):
    db_fields = [
        'cityName', 'gu', 'dong', 'complex', 'articleName', 'articleNo',
        'dealPrice', 'price', 'pct_change', 'allWarrantPrice',  
        'householdCountByPtp','aptUseApproveYmd', 'exposeStartYMD',
        'realestateTypeCode', 'tradeTypeName'
    ]

    data = {i : dict_data.get(i) for i in db_fields}
    return data

def export_main_info(dict_data):
    db_cols = [
        'articleName', 'aptUseApproveYmd', 'fullAddress', 'dealPrice', 
        'price', 'allWarrantPrice', 'financePrice', 'supplySpace', 
        'exclusiveSpace', 'exclusiveRate', 'walkingTimeToNearSubway', 
        'totalDongCount', 'aptHouseholdCount', 'floorInfo', 'entranceTypeName'
    ]

    data = {i : dict_data.get(i) for i in db_cols}
    return data

def export_detail_info(dict_data):
    db_cols = [
        'aptConstructionCompanyName', 'exposeStartYMD', 'exposeEndYMD',
        'roomCount', 'bathroomCount', 'monthlyManagementCost', 
        'monthlyManagementCostInclusdeItemName', 'direction', 
        'articleFeatureDescription'
    ]

    data = {i : dict_data.get(i) for i in db_cols}
    return data

def export_broker_info(dict_data):
    db_cols = [
        'realtorName', 'representativeName', 
        'address', 'telephon', 'cellPhoneNo'
    ]

    data = {i : dict_data.get(i) for i in db_cols}
    return data