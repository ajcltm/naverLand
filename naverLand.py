from dataclasses import dataclass, field, asdict
from typing import List
import requests
import time

class GuListProvider:

    def get_data(self):
        url = 'https://new.land.naver.com/api/regions/list?cortarNo=1100000000'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',
            
            'Host': 'new.land.naver.com',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        return r.json()

    def get_generator(self):
        guList = self.get_data()
        return (guList['regionList'][k]['cortarNo'] for k in [0])

class DongListProvider:

    def get_data(self, dong):
        url = f'https://new.land.naver.com/api/regions/list?cortarNo={dong}'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',

            'Host': 'new.land.naver.com',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        return r.json()

    def get_generator(self, dong):
        dongList = self.get_data(dong)
        # return (dongList['regionList'][0]['cortarNo'] for k in range(len(dongList['regionList'])))
        return (dongList['regionList'][0]['cortarNo'] for k in [0])

class ComplexListProvider:

    def get_data(self, cortarNo):
        url = f'https://new.land.naver.com/api/regions/complexes?cortarNo={cortarNo}&realEstateType=APT&order='
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',

            'Host': 'new.land.naver.com',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        return r.json()

    def get_generator(self, cortarNo):
        complexList = self.get_data(cortarNo)
        # return (complexList['complexList'][0]['complexNo'] for k in range(len(complexList['complexList'])))
        return (complexList['complexList'][0]['complexNo'] for k in [0])
    

class ArticleListProvider:

    def get_data(self, complexNo, tradeType='A1'):            #tradeType  A1: 매매, B1: 전세
        url = f'https://new.land.naver.com/api/articles/complex/{complexNo}?realEstateType=APT&tradeType={tradeType}&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo={complexNo}&buildingNos=&areaNos=&type=list&order=rank'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',

            'Host': 'new.land.naver.com',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        return r.json()

    def get_generator(self, complexNo):
        articleList = self.get_data(complexNo)
        return ((articleList['articleList'][k]['articleNo'], complexNo) for k in range(len(articleList['articleList'])))
        # return ((articleList['articleList'][0]['articleNo'], complexNo) for k in [0])

class ArticleInfoProvider:

    def get_article_info_data(self, articleNo):
        url = f'https://new.land.naver.com/api/articles/{articleNo}?complexNo='
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',
            'Cookie': 'NNB=XDAEADAWTN2V6; NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; ASID=d3cfd3330000017b6b53b7920000006c; nx_ssl=2; _ga=GA1.2.1641582590.1602312031; _ga_7VKFYR6RV1=GS1.1.1640622961.64.0.1640622961.60; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.ipaddress_city=1100000000; landHomeFlashUseYn=N; nhn.realestate.article.trade_type_cd=A1; realestate.beta.lastclick.cortar=1168010300; REALESTATE=Tue%20Jan%2011%202022%2000%3A10%3A43%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1641827444',
            'Host': 'new.land.naver.com',
            'Referer': 'https://new.land.naver.com/complexes/8928?ms=37.496437,127.07371950000001,17&a=APT&b=A1:B1&e=RETAIL',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        return r.json()

    def get_complex_price_data(self, complexNo):
        url = f'https://new.land.naver.com/api/complexes/{complexNo}/prices?complexNo={complexNo}&year=5&tradeType=A1&areaNo=1&type=chart'
        print(url)
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDI0MzM3MDAsImV4cCI6MTY0MjQ0NDUwMH0.0E_bLezMEZWh-H_YEXWAU3gwjpUiyc-NPS_9Dbx_BRw',
            'Connection': 'keep-alive',
            'Host': 'new.land.naver.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        return r.json()

    def get_data(self, tuple):
        articleNo = tuple[0]
        complexNo = tuple[1]
        article_info_data = self.get_article_info_data(articleNo)
        complex_price_data = self.get_complex_price_data(complexNo)
        return {'article_info_data':article_info_data, 'complex_price_data':complex_price_data}
    
    def get_generator(self, tuple):
        dic = self.get_data(tuple)
        return (dic for k in [0])

@dataclass
class ComplexArticle:
    complexNo : str
    articleNoList : List = field(default_factory=List)

class ComplexArticleProvider:

    def get_data(self, complexNo):
        articleList = ArticleListProvider().get_data(complexNo, 'A1')['articleList']
        articleNoList = [article.get('articleNo') for article in articleList]
        data = ComplexArticle(complexNo, articleNoList)
        return data

    def get_generator(self, complexNo):
        data = self.get_data(complexNo)
        return (data for k in [0])

class Looper:

    def __init__(self, operator, nextLooper=None):
        self.operator = operator
        self.nextLooper = nextLooper

    def execute(self, generator):
        print('excute')
        return (self.operator.get_generator(i) for sub_generator in generator for i in sub_generator)
    
    def handle_request(self, generator):
        if self.nextLooper :
            print('next lopper!')
            result = self.nextLooper.handle_request(self.execute(generator))
            return result
        else :
            print('my lopper!')
            result = self.execute(generator)
            return result


@dataclass
class ArticleDataClass:
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

    realPriceDataXList : List = field(default_factory=List)
    realPriceDataYList : List = field(default_factory=List)


class ArticleDataClassTransfier:

    def get_generator(self, articleInfo):
        articleInfoData = articleInfo.get('article_info_data')

        articleDetail = articleInfoData.get('articleDetail')
        articleNo = articleDetail.get('articleNo')
        articleName = articleDetail.get('articleName')
        exposeStartYMD = articleDetail.get('exposeStartYMD')
        exposeEndYMD = articleDetail.get('exposeEndYMD')
        articleConfirmYMD = articleDetail.get('articleConfirmYMD')
        aptName = articleDetail.get('aptName')
        aptHouseholdCount = articleDetail.get('aptHouseholdCount')
        aptConstructionCompanyName = articleDetail.get('aptConstructionCompanyName')
        aptUseApproveYmd = articleDetail.get('aptUseApproveYmd')
        totalDongCount = articleDetail.get('totalDongCount')
        realestateTypeCode = articleDetail.get('realestateTypeCode')
        tradeTypeName = articleDetail.get('tradeTypeName')
        verificationTypeCode = articleDetail.get('verificationTypeCode')
        cityName = articleDetail.get('cityName')
        divisionName = articleDetail.get('divisionName')
        sectionName = articleDetail.get('sectionName')
        householdCountByPtp = articleDetail.get('householdCountByPtp')
        walkingTimeToNearSubway = articleDetail.get('walkingTimeToNearSubway')
        detailAddress = articleDetail.get('detailAddress')
        roomCount = articleDetail.get('roomCount')
        bathroomCount = articleDetail.get('bathroomCount')
        moveInTypeCode = articleDetail.get('moveInTypeCode')
        moveInDiscussionPossibleYN = articleDetail.get('moveInDiscussionPossibleYN')
        monthlyManagementCost = articleDetail.get('monthlyManagementCost')
        monthlyManagementCostIncludeItemName = articleDetail.get('monthlyManagementCostIncludeItemName')
        buildingName = articleDetail.get('buildingName')
        articleFeatureDescription = articleDetail.get('articleFeatureDescription')
        detailDescription = articleDetail.get('detailDescription')
        floorLayerName = articleDetail.get('floorLayerName')
        tagList = articleDetail.get('tagList')
        
        articleAddition = articleInfoData['articleAddition']
        floorInfo = articleAddition.get('floorInfo')
        priceChangeState = articleAddition.get('priceChangeState')
        dealOrWarrantPrc = articleAddition.get('dealOrWarrantPrc')
        direction = articleAddition.get('direction')
        latitude = articleAddition.get('latitude')
        longitude = articleAddition.get('longitude')

        articleFacility = articleInfoData['articleFacility']       
        entranceTypeName = articleFacility.get('entranceTypeName')

        articlePrice = articleInfoData['articlePrice']  
        
        rentPrice = articlePrice.get('rentPrice')
        dealPrice = articlePrice.get('dealPrice')
        warrantPrice = articlePrice.get('warrantPrice')
        allWarrantPrice = articlePrice.get('allWarrantPrice')
        financePrice = articlePrice.get('financePrice')
        premiumPrice = articlePrice.get('premiumPrice')
        isalePrice = articlePrice.get('isalePrice')
        allRentPrice = articlePrice.get('allRentPrice')
        priceBySpace = articlePrice.get('priceBySpace')
        bondPrice = articlePrice.get('bondPrice')
        middlePayment = articlePrice.get('middlePayment')
        
        articleRealtor = articleInfoData['articleRealtor']  
    
        realtorName = articleRealtor.get('realtorName')
        representativeName = articleRealtor.get('representativeName')
        address = articleRealtor.get('address')
        representativeTelNo = articleRealtor.get('representativeTelNo')
        cellPhoneNo = articleRealtor.get('cellPhoneNo')

        articleSpace = articleInfoData['articleSpace'] 
        supplySpace = articleSpace.get('supplySpace')
        exclusiveSpace = articleSpace.get('exclusiveSpace')
        exclusiveRate = articleSpace.get('exclusiveRate')

        complex_price_data = articleInfo.get('complex_price_data')
        realPriceDataXList = complex_price_data.get('realPriceDataXList')
        realPriceDataYList = complex_price_data.get('realPriceDataYList')


        data = ArticleDataClass(
            articleNo,articleName,exposeStartYMD,exposeEndYMD,articleConfirmYMD,aptName,aptHouseholdCount,aptConstructionCompanyName,aptUseApproveYmd,totalDongCount,realestateTypeCode
            ,tradeTypeName,verificationTypeCode,cityName,divisionName,sectionName,householdCountByPtp,walkingTimeToNearSubway,detailAddress,roomCount,bathroomCount,moveInTypeCode,
            moveInDiscussionPossibleYN,monthlyManagementCost,monthlyManagementCostIncludeItemName,buildingName,articleFeatureDescription,detailDescription,floorLayerName,
            floorInfo, priceChangeState, dealOrWarrantPrc, direction, latitude, longitude, entranceTypeName, rentPrice, dealPrice, warrantPrice, allWarrantPrice, financePrice, 
            premiumPrice, isalePrice, allRentPrice, priceBySpace, bondPrice, middlePayment, realtorName, representativeName, address, representativeTelNo, cellPhoneNo, supplySpace,
            exclusiveSpace, exclusiveRate, tagList, realPriceDataXList, realPriceDataYList) 
            
        return (data for i in [0])



if __name__ == '__main__' :

    # guList = GuListProvider().get_data()
    # print('='*100)
    # print(f'GuList :\n {guList}')

    # gangnamgu = guList['regionList'][0]['cortarNo']
    # dongList = DongListProvider().get_data(gangnamgu)
    # print('='*100)
    # print(f'dongList :\n {dongList}')

    # gaepodong = dongList['regionList'][0]['cortarNo']

    # complexList = ComplexListProvider().get_data(gaepodong)
    # print('='*100)
    # print(f'complexList :\n {complexList}')

    # lg_apt = complexList['complexList'][0]['complexNo']
    # article = ArticleListProvider().get_data(lg_apt, 'A1')
    # print('='*100)
    # print(f'article :\n {article}')
    # articleNo = article['articleList'][0]['articleNo']

    # article_1_info = ArticleInfoProvider().get_data(articleNo)
    # print('='*100)
    # print(f'article info :\n {article_1_info}')

    # article_no = '2200337131'
    # article_1_info = ArticleInfoProvider().get_data(article_no)
    # print('='*100)
    # print(f'article info :\n {article_1_info}')
    # data = ArticleDataClassTransfier().transfer(article_1_info)
    # print('='*100)
    # print(f'data :\n {data}')


    # article_info = export_target_tag(tag_='세안고').export_article_info()
    # print(article_info)

    gu_generator = (GuListProvider().get_generator() for i in [0])
    print('='*100)
    print(f'GuList :\n {gu_generator}')

    dongOperator = DongListProvider()
    complexOperator = ComplexListProvider()
    articleOperator = ArticleListProvider()
    articleInfoOperator = ArticleInfoProvider()
    articleDataClassOperator = ArticleDataClassTransfier()

    articleDataLooper = Looper(articleDataClassOperator)
    articleInfoLooper = Looper(articleInfoOperator, articleDataLooper)
    articleLopper = Looper(articleOperator, articleInfoLooper)
    complexLooper = Looper(complexOperator, articleLopper)
    dongLooper = Looper(dongOperator, complexLooper)

    data_generator = dongLooper.handle_request(gu_generator)
    print(data_generator)
    
    for k in data_generator:
        print('='*100)
        print(list(k))
    
    # complexNo = '8928'
    # complexArticle = ComplexArticleProvider().get_data(complexNo)
    # print(f'complex - article : {complexArticle}')

    # reverse = {articleNo : complexArticle.complexNo for articleNo in complexArticle.articleNoList}
    # print(reverse)
    # import pandas as pd
    # print(pd.Series(reverse.values(), index=reverse.keys()))

