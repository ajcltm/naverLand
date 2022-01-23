




if __name__ == '__main__' :
    
    import dataclass


    # dcs = dataclass.GuDCs()
    # print('='*100, 'data :', dcs.data, sep='\n')
    # print('='*100, 'get_by_idNo result :', dcs.get_by_idNo('1162000000'), sep='\n')
    # print('='*100, 'get_by_name result :', dcs.get_by_name('강남구'), sep='\n')
    # print('='*100, 'get_by_cityNo result :', dcs.get_by_cityNo('1100000000'), sep='\n')

    # print('='*100, 'AND result', [i for i in dcs.get_by_cityNo('1100000000') if i in dcs.get_by_name('강남구')], sep='\n')
    # print('='*100, 'OR result', dcs.get_by_cityNo('1100000000') + dcs.get_by_name('강남구'), sep='\n')



    # dcs = dataclass.DongDCs()
    # print('='*100, 'data :', dcs.data, sep='\n')
    # print('='*100, 'get_by_idNo result :', dcs.get_by_idNo('1168010300'), sep='\n')
    # print('='*100, 'get_by_name result :', dcs.get_by_name('화곡동'), sep='\n')
    # print('='*100, 'get_by_guNo result :', dcs.get_by_guNo('1150000000'), sep='\n')

    # print('='*100, 'AND result', [i for i in dcs.get_by_guNo('1150000000') if i in dcs.get_by_name('화곡동')], sep='\n')
    # print('='*100, 'OR result', dcs.get_by_guNo('1150000000') + dcs.get_by_name('화곡동'), sep='\n')

    # dcs = dataclass.ComplexDCs()
    # print('='*100, 'data :', dcs.data, sep='\n')
    # print('='*100, 'get_by_idNo result :', dcs.get_by_idNo('8928'), sep='\n')
    # print('='*100, 'get_by_name result :', dcs.get_by_name('LG개포자이'), sep='\n')
    # print('='*100, 'get_by_dongNo result :', dcs.get_by_dongNo('1168010300'), sep='\n')

    # print('='*100, 'AND result', [i for i in dcs.get_by_dongNo('1168010300') if i in dcs.get_by_name('LG개포자이')], sep='\n')
    # print('='*100, 'OR result', dcs.get_by_dongNo('1168010300') + dcs.get_by_name('LG개포자이'), sep='\n')

    # filter = pd.DataFrame([{'name' : i.name, 'count': i.totalHouseholdCount} for i in dcs.data if i.totalHouseholdCount>4000])
    # print('='*100, 'filter result', filter, sep='\n')
    # Create_preprocessed_complex_price_db().excute()

    dcs = dataclass.ArticleInfoDCs()
    print('='*100, 'data :', dcs.data, sep='\n')

