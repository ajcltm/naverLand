parentPath='c:/Users/ajcltm/PycharmProjects/naverLand'
import sys
sys.path.append(parentPath)
from library import query
import exportInfo
import pandas as pd
from dataclasses import asdict
import plotly.express as px

class NaverLand:

    def __init__(self, db_path):
        self.db_path = db_path
        print(f"{db_path}")

    def query_info(self, where) -> None:
        queryData = query.BasicQuery(self.db_path).get(where)
        dict_data = (asdict(data) for data in queryData)

        dict_data_for_df = (exportInfo.export_article(data) for data in dict_data)
        self.queryInfo = self.transfer_dataFrame(dict_data_for_df)

    def get_info(self, articleNo) -> None:
        queryData = query.BasicQuery(self.db_path).get(where=f'where articleNo = {articleNo}')
        dict_data = list(asdict(data) for data in queryData)

        dict_data_for_df = (exportInfo.export_main_info(data) for data in dict_data)
        self.mainInfo = self.transfer_dataFrame_for_get_info(dict_data_for_df)

        dict_data_for_df = (exportInfo.export_detail_info(data) for data in dict_data)
        self.detailInfo = self.transfer_dataFrame_for_get_info(dict_data_for_df)

        dict_data_for_df = (exportInfo.export_broker_info(data) for data in dict_data)
        self.brokerInfo = self.transfer_dataFrame_for_get_info(dict_data_for_df)

        data_object_for_df = self.get_price_info(dict_data[0]['complexNo'], dict_data[0]['ptpNo'])
        self.priceInfo = self.transfer_dataFrame(data_object_for_df)

    def get_price_info(self, complexNo, ptpNo) :
        sql=f'select * from complex_price_info where idNo = {complexNo} and ptpNo = {ptpNo}'
        return query.GeneralQuery(self.db_path).get(sql)

    def get_graph(self):
        fig = px.scatter(self.priceInfo, x="date", y="price")
        # fig.update_traces(quartilemethod="inclusive") # or "inclusive", or "linear" by default

        fig.update_layout(
            autosize=False,
            width=300,
            height=200,
            margin=dict(l=6, r=8, b=6, t=8, pad=0),
            paper_bgcolor="LightSteelBlue"
        )
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_title=None, yaxis_title=None)
        fig.show()

    def transfer_dataFrame(self, data):
        return pd.DataFrame(data)

    def transfer_dataFrame_for_get_info(self, data):
        return pd.DataFrame(data, index=['naverLand']).transpose()


if __name__ == '__main__':
    from pathlib import Path
    file_name = 'naverLand(20220309-132731)_preprocessed.db'
    db_path = Path().cwd().joinpath('naverLand', 'db', file_name)
    nl = NaverLand(db_path)

    # where = 'where dong = "개포동"' 
    # nl.query_info(where = where)
    # print(nl.queryInfo)

    nl.get_info(articleNo='2204166923')
    print(nl.priceInfo)
    nl.get_graph()



