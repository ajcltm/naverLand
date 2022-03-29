parentPath='c:/Users/ajcltm/PycharmProjects/naverLand'
import sys
sys.path.append(parentPath)
from library import query
import exportInfo
import pandas as pd
from dataclasses import asdict
import plotly.express as px
import webbrowser

class NaverLand:

    def __init__(self, db_path):
        self.db_path = db_path
        print(f"{db_path}")

    def query_info(self, where : str) -> None:
        queryData = query.BasicQuery(self.db_path).get(where)
        dict_data = (asdict(data) for data in queryData)

        dict_data_for_df = (exportInfo.export_article(data) for data in dict_data)
        self.queryInfo = self.transfer_dataFrame(dict_data_for_df)

    def get_info(self, articleNo : list) -> None:
        self.articleNo = articleNo
        formated = ','.join(articleNo)
        queryData = query.BasicQuery(self.db_path).get(where=f'where articleNo in ({formated})')
        # queryData = query.BasicQuery(self.db_path).get(where=f'where articleNo = {articleNo}')
        dict_data = list(asdict(data) for data in queryData)

        dict_data_for_df = (exportInfo.export_main_info(data) for data in dict_data)
        self.mainInfo = self.transfer_dataFrame_for_get_info(dict_data_for_df)

        dict_data_for_df = (exportInfo.export_detail_info(data) for data in dict_data)
        self.detailInfo = self.transfer_dataFrame_for_get_info(dict_data_for_df)

        dict_data_for_df = (exportInfo.export_broker_info(data) for data in dict_data)
        self.brokerInfo = self.transfer_dataFrame_for_get_info(dict_data_for_df)

        dfs = []
        for i, data in enumerate(dict_data):
            data_object_for_df = self.get_price_info(dict_data[i]['complexNo'], dict_data[i]['ptpNo'])
            df = self.transfer_dataFrame_for_get_price_info(data_object_for_df, i)
            dfs.append(df)
        self.priceInfo = pd.concat(dfs)

    def get_price_info(self, complexNo, ptpNo) :
        sql=f'select * from complex_price_info where idNo = {complexNo} and ptpNo = {ptpNo}'
        return query.GeneralQuery(self.db_path).get(sql)

    def get_graph(self):
        fig = px.scatter(self.priceInfo, x="date", y="price", color="idNo",)
        # fig.update_traces(quartilemethod="inclusive") # or "inclusive", or "linear" by default

        fig.update_layout(
            autosize=False,
            width=300,
            height=200,
            margin=dict(l=6, r=8, b=6, t=8, pad=0),
            paper_bgcolor="LightSteelBlue"
        )
        fig.update_layout(uniformtext_minsize=4, uniformtext_mode='hide', xaxis_title=None, yaxis_title=None, showlegend=False)
        fig.update_layout(plot_bgcolor='#001c40', paper_bgcolor='#001c40', font_color='#ffffff', width=350, height=220)
        fig.update_traces(marker=dict(size=9,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
        fig.show()

    def get_images(self, articleNo):
        sql = f'select complexNo from complex_article where idNo = {articleNo}'
        data = list(query.GeneralQuery(self.db_path).get(sql))[0]
        webbrowser.open(f"https://land.naver.com/info/complexGallery.naver?rletNo={data.complexNo}")

    def get_map(self, articleNo):
        queryData = query.BasicQuery(self.db_path).get(where=f'where articleNo = {articleNo}')
        dict_data = list(asdict(data) for data in queryData)
        search_format = dict_data[0]['fullAddress'].replace(' ', '%20')
        print(search_format)
        webbrowser.open(f"https://map.naver.com/v5/search/{search_format}")


    def transfer_dataFrame(self, data):
        return pd.DataFrame(data)

    def transfer_dataFrame_for_get_info(self, data):
        return pd.DataFrame(data, index = self.articleNo).transpose()

    def transfer_dataFrame_for_get_price_info(self, data, i):
        df = pd.DataFrame(data)
        df['idNo'] = self.articleNo[i]
        return df

if __name__ == '__main__':
    from pathlib import Path
    file_name = 'naverLand(20220309-132731)_preprocessed.db'
    db_path = Path().cwd().joinpath('naverLand', 'db', file_name)
    nl = NaverLand(db_path)

    # where = 'where dong = "개포동"' 
    # nl.query_info(where = where)
    # print(nl.queryInfo)

    nl.get_info(articleNo=['2207055437','2207173712'])
    print(nl.mainInfo)
    print(nl.detailInfo)
    print(nl.brokerInfo)
    print(nl.priceInfo)
    nl.get_graph()
    nl.get_images('2207055437')
    nl.get_map('2207055437')



