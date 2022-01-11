from dataclasses import dataclass, field
from typing import List
import requests
import time

class GuListProvider:

    def get_regionList(self):
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

class DongListProvider:

    def get_regionList(self, dong):
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

class ComplexListProvider:

    def get_complexList(self, cortarNo):
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

class ArticleListProvider:

    def get_articleList(self, complexNo, tradeType='A1'):            #tradeType  A1: 매매, B1: 전세
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

class ArticleInfoProvider:

    def get_articleInfo(self, articleNo):
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
    tagList : List = field(default_factory=List)



class ArticleDataClassTransfier:

    def transfer(self, articleInfo):
        articleDetail = articleInfo.get('articleDetail')
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
        
        articleAddition = articleInfo['articleAddition']
        data = ArticleDataClass(
            articleNo,articleName,exposeStartYMD,exposeEndYMD,articleConfirmYMD,aptName,aptHouseholdCount,aptConstructionCompanyName,aptUseApproveYmd,totalDongCount,realestateTypeCode
            ,tradeTypeName,verificationTypeCode,cityName,divisionName,sectionName,householdCountByPtp,walkingTimeToNearSubway,detailAddress,roomCount,bathroomCount,moveInTypeCode,
            moveInDiscussionPossibleYN,monthlyManagementCost,monthlyManagementCostIncludeItemName,buildingName,articleFeatureDescription,detailDescription,floorLayerName,tagList)
        return data


class export_target_tag:

    def __init__(self, tag_):
        self.tag = tag_

    def export_article_info(self):
        guList = GuListProvider().get_regionList()['regionList']
        for k in range(0, len(guList)) :
            time.sleep(1)
            gu = guList[k]['cortarNo']
            dongList = DongListProvider().get_regionList(gu)['regionList']
            for i in range(0, len(dongList)):
                time.sleep(1)
                dong = dongList[i]['cortarNo']
                complexList = ComplexListProvider().get_complexList(dong)['complexList']
                for z in range(0, len(complexList)):
                    time.sleep(1)
                    complexNo = complexList[z]['complexNo']
                    articleList = ArticleListProvider().get_articleList(complexNo, 'A1')['articleList']
                    for w in range(0, len(articleList)):
                        time.sleep(1)
                        articleNo = articleList[w]['articleNo']
                        article_info = ArticleInfoProvider().get_articleInfo(articleNo)
                        keys = list(article_info.keys())
                        tagList = article_info[keys[0]].get('tagList')
                        print(tagList)
                        if self.tag in tagList :
                            print(article_info)
                            return article_info

if __name__ == '__main__' :

    # guList = GuListProvider().get_regionList()
    # print('='*100)
    # print(f'GuList :\n {guList}')

    # gangnamgu = guList['regionList'][0]['cortarNo']
    # dongList = DongListProvider().get_regionList(gangnamgu)
    # print('='*100)
    # print(f'dongList :\n {dongList}')

    # gaepodong = dongList['regionList'][0]['cortarNo']

    # complexList = ComplexListProvider().get_complexList(gaepodong)
    # print('='*100)
    # print(f'complexList :\n {complexList}')

    # lg_apt = complexList['complexList'][0]['complexNo']
    # article = ArticleListProvider().get_articleList(lg_apt, 'A1')
    # print('='*100)
    # print(f'article :\n {article}')
    # articleNo = article['articleList'][0]['articleNo']

    # article_1_info = ArticleInfoProvider().get_articleInfo(articleNo)
    # print('='*100)
    # print(f'article info :\n {article_1_info}')

    article_no = '2200337131'
    article_1_info = ArticleInfoProvider().get_articleInfo(article_no)
    print('='*100)
    print(f'article info :\n {article_1_info}')
    data = ArticleDataClassTransfier().transfer(article_1_info)
    print('='*100)
    print(f'data :\n {data}')


    # article_info = export_target_tag(tag_='세안고').export_article_info()
    # print(article_info)
