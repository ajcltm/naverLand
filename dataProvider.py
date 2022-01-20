import requests
import time
import random
import dataclass

class RandomSleep:

    def sleep(self):
        range_option = {'quicker': [0, .5], 'slower': [.5, 2], 'stop': [10, 15]}
        sleepLevel = random.choices(['quicker', 'slower', 'stop'], weights=[.6, .39, .01])
        range = range_option.get(sleepLevel[0])
        if sleepLevel[0] == 'stop' : print('Now taking a rest in a seconds')
        time.sleep(random.uniform(range[0], range[1]))

class GuDataProvider:

    def get_data(self):

        RandomSleep().sleep()
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
        try: 
            data = r.json()
        except :
            data = None
        return data

    def get_generator(self):
        data = self.get_data()
        if data == None :
            return (dataclass.GuDC(**{'idNo':None, 'name':None, 'cityNo':'1100000000'}) for k in [0])
        guNoList = [data['regionList'][k]['cortarNo'] for k in range(0, len(data['regionList']))]
        guNameList = [data['regionList'][k]['cortarName'] for k in range(0, len(data['regionList']))]
        generator = (dataclass.GuDC(**{'idNo':guNoList[k], 'name':guNameList[k], 'cityNo':'1100000000'}) for k in range(0, len(data['regionList'])))
        return generator


class DongDataProvider:

    def get_data(self, gu):

        RandomSleep().sleep()
        url = f'https://new.land.naver.com/api/regions/list?cortarNo={gu}'
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
        try: 
            data = r.json()
        except :
            print(f'{gu} : json failed')
            data = None
        return data

    def get_generator(self, gu):
        data = self.get_data(gu)
        if data == None :
            return (dataclass.DongDC(**{'idNo':None, 'name':None, 'guNo': gu}) for k in [0])
        dongNoList = [data['regionList'][k]['cortarNo'] for k in range(0, len(data['regionList']))]
        dongNameList = [data['regionList'][k]['cortarName'] for k in range(0, len(data['regionList']))]
        generator = (dataclass.DongDC(**{'idNo':dongNoList[k], 'name':dongNameList[k], 'guNo': gu}) for k in range(0, len(data['regionList'])))
        return generator


class ComplexDataProvider:

    def get_data(self, dong):

        RandomSleep().sleep()
        url = f'https://new.land.naver.com/api/regions/complexes?cortarNo={dong}&realEstateType=APT&order='
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
        try: 
            data = r.json()
        except :
            print(f'{dong} : json failed')
            data = None
        return data
    
    def get_generator(self, dong):
        data = self.get_data(dong)
        if data == None:
            keys = ['idNo', 'name', 'dongNo', 'realEstateTypeCode', 'cortarAddress', 'detailAddress', 
                    'totalHouseholdCount', 'totalBuildingCount', 'highFloor', 'lowFloor', 'useApproveYmd']
            dic = {key : None for key in keys}
            return (dataclass.ComplexDC(**dic) for k in [0])
        print(f'{dong} : dongNo')
        complexNoList = [data['complexList'][k].get('complexNo') for k in range(0, len(data['complexList']))]
        complexNameList = [data['complexList'][k].get('complexName') for k in range(0, len(data['complexList']))]
        typeCodeList = [data['complexList'][k].get('realEstateTypeCode') for k in range(0, len(data['complexList']))]
        addressList = [data['complexList'][k].get('cortarAddress') for k in range(0, len(data['complexList']))]
        addressDeList = [data['complexList'][k].get('detailAddress') for k in range(0, len(data['complexList']))]
        hCountList = [data['complexList'][k].get('totalHouseholdCount') for k in range(0, len(data['complexList']))]
        bCountList = [data['complexList'][k].get('totalBuildingCount') for k in range(0, len(data['complexList']))]
        hFloor = [data['complexList'][k].get('highFloor') for k in range(0, len(data['complexList']))]
        lFloor = [data['complexList'][k].get('lowFloor') for k in range(0, len(data['complexList']))]
        apprrList = [data['complexList'][k].get('useApproveYmd') for k in range(0, len(data['complexList']))]

        generator = (dataclass.ComplexDC(**{'idNo':complexNoList[k],
                                         'name':complexNameList[k], 
                                        'dongNo': dong,
                                        'realEstateTypeCode':typeCodeList[k],
                                        'cortarAddress':addressList[k],
                                        'detailAddress':addressDeList[k],
                                        'totalHouseholdCount':hCountList[k],
                                        'totalBuildingCount':bCountList[k],
                                        'highFloor':hFloor[k],
                                        'lowFloor':lFloor[k],
                                        'useApproveYmd':apprrList[k]}) for k in range(0, len(data['complexList'])))
        return generator


class ComplexPriceDataProvider:

    def get_data(self, complexNo):

        RandomSleep().sleep()
        url = f'https://new.land.naver.com/api/complexes/{complexNo}/prices?complexNo={complexNo}&year=5&tradeType=A1&areaNo=1&type=chart'
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
        try: 
            data = r.json()
        except :
            print(f'{complexNo} : json failed')
            data = None
        return data

    def get_generator(self, complexNo):
        data = self.get_data(complexNo)
        if data == None:
            return (dataclass.ComplexPriceDC(**{'idNo':None, 'date':None, 'price':None}) for k in [0])
        date = data.get('realPriceDataXList')[1:]
        price = data.get('realPriceDataYList')[1:]

        return (dataclass.ComplexPriceDC(**{'idNo':complexNo, 'date':date, 'price':price}) for k in [0])


class ArticleDataProvider:

    def get_data(self, complexNo, tradeType='A1'):            #tradeType  A1: 매매, B1: 전세
        
        RandomSleep().sleep()
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
        try: 
            data = r.json()
        except :
            print(f'{complexNo} : json failed')
            data = None
        return data

    def get_generator(self, complexNo):
        data = self.get_data(complexNo)
        if data == None:
            return (dataclass.ArticleDC(**{'idNo':None, 'name':None, 'complexNo':None}) for k in [0])
        dataList = data.get('articleList')
        if dataList == None:
            return (dataclass.ArticleDC(**{'idNo':None, 'name':None, 'complexNo':None}) for k in [0])
        articleNoList = [dataList[k]['articleNo'] for k in range(0, len(dataList))]
        articleNameList = [dataList[k]['articleName'] for k in range(0, len(dataList))]
        return (dataclass.ArticleDC(**{'idNo':articleNoList[k], 'name':articleNameList[k], 'complexNo': complexNo}) for k in range(len(dataList)))


class ArticleInfoDataProvider:

    def get_data(self, articleNo):

        RandomSleep().sleep()
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
        try: 
            data = r.json()
        except :
            print(f'{articleNo} : json failed')
            data = None
        return data
    
    def get_generator(self, articleNo):
        ad_keys = ['articleNo', 'articleName', 'exposeStartYMD','exposeEndYMD','articleConfirmYMD','aptName','aptHouseholdCount','aptConstructionCompanyName','aptUseApproveYmd',
        'totalDongCount', 'realestateTypeCode', 'tradeTypeName', 'verificationTypeCode', 'cityName', 'divisionName', 'sectionName', 'householdCountByPtp',
        'walkingTimeToNearSubway', 'detailAddress', 'roomCount', 'bathroomCount', 'moveInTypeCode', 'moveInDiscussionPossibleYN', 'monthlyManagementCost', 'monthlyManagementCostIncludeItemName',
        'buildingName', 'articleFeatureDescription', 'detailDescription', 'floorLayerName']
        aa_keys = ['floorInfo', 'priceChangeState', 'dealOrWarrantPrc','direction','latitude','longitude']
        af_keys = ['entranceTypeName']
        ap_keys = ['rentPrice', 'dealPrice', 'warrantPrice', 'allWarrantPrice', 'financePrice',
        'premiumPrice', 'isalePrice', 'allRentPrice', 'priceBySpace', 'bondPrice', 'middlePayment']
        ar_keys = ['realtorName', 'representativeName', 'address','representativeTelNo','cellPhoneNo', 'supplySpace', 'exclusiveSpace', 'exclusiveRate']
        adt_keys = ['tagList']

        data = self.get_data(articleNo)

        if data == None:
            keys = ad_keys + aa_keys + af_keys + ap_keys + ar_keys + adt_keys
            dic = {key : None for key in keys}
            return (dataclass.ArticleInfoDC(**dic) for k in [0])

        ad = data.get('articleDetail')
        if ad == None:
            ad_dict = {k : None for k in ad_keys}
            adt_dict_ = {k : None for k in adt_keys}
        else :
            ad_dict = {k : ad.get(k) for k in ad_keys}
            adt_dict = {k : ad.get(k) for k in adt_keys}
            adt_dict_ = {item[0] : " ".join(item[1]) for item in adt_dict.items()} 

        aa = data.get('articleFacility')
        if aa == None:
            aa_dict = {k : None for k in aa_keys}
        else :  
            aa_dict = {k : aa.get(k) for k in aa_keys}

        af = data.get('articleAddition')
        if af == None:
            af_dict = {k : None for k in af_keys}
        else :
            af_dict = {k : af.get(k) for k in af_keys}

        ap = data.get('articlePrice')
        if ap == None:
            ap_dict = {k : None for k in ap_keys}
        else :
            ap_dict = {k : ap.get(k) for k in ap_keys}

        ar = data.get('articleRealtor')
        if ar == None:
            ar_dict = {k : None for k in ar_keys}
        else :
            ar_dict = {k : ar.get(k) for k in ar_keys}

        final_dict = dict(ad_dict, **aa_dict, **af_dict, **ap_dict, **ar_dict, **adt_dict_)
        return (dataclass.ArticleInfoDC(**final_dict) for k in [0])