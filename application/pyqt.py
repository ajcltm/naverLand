import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

sys.path.append('C:/Users/ajcltm/PycharmProjects/naverLand')
import dataclass
import sqlQuery
import cellLineEdit
import whereClause


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab1_init_data = sqlQuery.Tab1_table().get_data()
        self.tab1_data = self.tab1_init_data
        self.where = whereClause.tab1_WhereHandler().set_where_dict()

        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200, 1000, 700)

        self.tabs1 = QTabWidget()

        self.tab1 = QTableWidget()
        self.tab1.resize(400, 500)
        self.set_tab1()
        self.tab2 = QTableWidget()
        self.tab2.resize(400, 500)
        # self.set_tab2()

        self.tabs1.addTab(self.tab1, 'table1')
        self.tabs1.addTab(self.tab2, 'table2')

        self.table3 = QTableWidget()
        self.table3.move(100, 0)

        self.tabs2 = QTabWidget()
        self.tab4 = QTableWidget()
        self.tab5 = QTableWidget()
        self.tabs2.addTab(self.tab4, 'table4')
        self.tabs2.addTab(self.tab5, 'table5')

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.tabs1)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addSpacing(24)
        self.rightLayout.addWidget(self.table3)
        self.rightLayout.addWidget(self.tabs2)
        

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.leftLayout)
        self.layout.addLayout(self.rightLayout)

        self.setLayout(self.layout)
    
    # def set_tab1(self):

    #     dcs = [dc for dc in self.complexDCs.data if dc.idNo in self.complexKeys]
        
    #     cols = ['complexNo', 'name', 'address', 'type', 'count', 'hFloor', 'Ymd']

    #     self.tab1.setColumnCount(len(cols))
    #     self.tab1.setRowCount(len(self.complexKeys))
        
    #     self.tab1.setHorizontalHeaderLabels(cols)
    #     self.tab1.horizontalHeader().setStyleSheet("::section{background-color : #194350;" "color:white;" "border-style : solid;}")

    #     # create line Editers
    #     for tuple in enumerate(cols): 
    #         self.tab1.setCellWidget(0, tuple[0], QLineEdit())

    #     # create table data
    #     for tuple in enumerate(dcs) :  # rows
    #         self.tab1.setItem(tuple[0]+1, 0, QTableWidgetItem(self.complexKeys[tuple[0]]))
    #         self.tab1.setItem(tuple[0]+1, 1, QTableWidgetItem(tuple[1].name))
    #         self.tab1.setItem(tuple[0]+1, 2, QTableWidgetItem(tuple[1].cortarAddress +' '+ tuple[1].detailAddress))
    #         self.tab1.setItem(tuple[0]+1, 3, QTableWidgetItem(tuple[1].realEstateTypeCode))
    #         self.tab1.setItem(tuple[0]+1, 4, QTableWidgetItem(str(tuple[1].totalHouseholdCount)))
    #         self.tab1.setItem(tuple[0]+1, 5, QTableWidgetItem(str(tuple[1].highFloor)))
    #         self.tab1.setItem(tuple[0]+1, 6, QTableWidgetItem(tuple[1].useApproveYmd))

    def set_tab1(self):
        
        cols = ['cityNo', 'city', 'dong', 'complex','articleNo', 'articleName', 'estateType', 'ApproveYmd', 'dealPrice', 'warrantPrice','hhCount','exposeYMD', 'tradeTypeName',]
        self.tab1.setColumnCount(len(cols))
        self.tab1.setRowCount(len(self.tab1_data))
        
        self.tab1.setHorizontalHeaderLabels(cols)
        self.tab1.horizontalHeader().setStyleSheet("::section{background-color : #05111b;" "color:white;" "border-style : solid;}")

        # create table data

        self.set_tab1_contents()

        # create line Editers
    
        self.set_cell_lineEdit()
    
    def set_tab1_contents(self):
        self.tab1.setRowCount(len(self.tab1_data)+1)
        db_cols = ['cityNo', 'gu', 'dong', 'complex', 'articleNo', 'articleName',
                    'realestateTypeCode', 'aptUseApproveYmd', 'dealPrice',
                    'wrrantPrice', 'householdCountByPtp', 'exposeStartYMD',
                    'tradeTypeName']
        for row_tuple in enumerate(self.tab1_data) :  # rows
            for col_tuple in enumerate(db_cols) : #cols
                self.tab1.setItem(row_tuple[0]+1, col_tuple[0], QTableWidgetItem(str(row_tuple[1].get(col_tuple[1]))))

        self.tab1.setEditTriggers(QTableWidget.NoEditTriggers)

    def set_tab1_contents_test(self):
        
        db_cols = ['cityNo', 'gu', 'dong', 'complex', 'articleNo', 'articleName',
                    'realestateTypeCode', 'aptUseApproveYmd', 'dealPrice',
                    'wrrantPrice', 'householdCountByPtp', 'exposeStartYMD',
                    'tradeTypeName']
        data = [{key: 'a' for key in db_cols}]
        print(f'test_data : {data}')
        self.tab1.setRowCount(len(data)+1)
        for row_tuple in enumerate(data) :  # rows
            for col_tuple in enumerate(db_cols) : #cols
                self.tab1.setItem(row_tuple[0]+1, col_tuple[0], QTableWidgetItem(str(row_tuple[1].get(col_tuple[1]))))

        self.tab1.setEditTriggers(QTableWidget.NoEditTriggers)

    def set_cell_lineEdit(self):
        self.cityNo_le = QLineEdit()
        self.tab1.setCellWidget(0, 0, self.cityNo_le)

        self.gu_le = QLineEdit()
        self.tab1.setCellWidget(0, 1, self.gu_le)

        self.dong_le = QLineEdit()
        self.tab1.setCellWidget(0, 2, self.dong_le)

        self.complex_le = QLineEdit()
        self.tab1.setCellWidget(0, 3, self.complex_le)

        self.articleNo_le = QLineEdit()
        self.tab1.setCellWidget(0, 4, self.articleNo_le)
        # self.articleNo_le.textChanged.connect(self.cellLineEditClicked)
        self.articleNo_le.returnPressed.connect(self.articleNo_cellLineEditClicked)

        self.articleName_le = QLineEdit()
        self.tab1.setCellWidget(0, 5, self.articleName_le)
        self.articleName_le.returnPressed.connect(self.articleName_cellLineEditClicked)

        self.estateType_le = QLineEdit()
        self.tab1.setCellWidget(0, 6, self.estateType_le)

        self.aptUseYMD_le = QLineEdit()
        self.tab1.setCellWidget(0, 7, self.aptUseYMD_le)

        self.dealPrice_le = QLineEdit()
        self.tab1.setCellWidget(0, 8, self.dealPrice_le)

        self.wrrantPrice_le = QLineEdit()
        self.tab1.setCellWidget(0, 9, self.wrrantPrice_le)

        self.hhCount_le = QLineEdit()
        self.tab1.setCellWidget(0, 10, self.hhCount_le)

        self.exposeStartYMD_le = QLineEdit()
        self.tab1.setCellWidget(0, 11, self.exposeStartYMD_le)

        self.tradeTypeName_le = QLineEdit()
        self.tab1.setCellWidget(0, 12, self.tradeTypeName_le)
    
    def articleNo_cellLineEditClicked(self):
        text = self.articleNo_le.text()
        target_col = 'article_info.articleNo'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = self.where
        dic['articleNo'] = where_content
        self.where = dic
        print('='*100, self.where, sep='\n')
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(self.where)
        print('='*100, f'where_clause : {where_clause}', sep='\n')
        self.tab1_data = sqlQuery.Tab1_table().get_data(where=where_clause)

        self.set_tab1_contents()

    def articleName_cellLineEditClicked(self):
        text = self.articleName_le.text()
        target_col = 'article_info.articleName'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = self.where
        dic['articleName'] = where_content
        self.where = dic
        print('='*100, self.where, sep='\n')
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(self.where)
        print('='*100, f'where_clause : {where_clause}', sep='\n')
        print(f'where_clause : {where_clause}')
        self.tab1_data = sqlQuery.Tab1_table().get_data(where=where_clause)
    
        self.set_tab1_contents()

        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    app.exec()
    # import time
    # start = time.time()
    # dcs = dataclass.ArticleInfoDCs().data

    # end = time.time()
    
    # print(f'dcs loading : {end - start} seconds')

    # start = time.time()
    # arDcs = dataclass.ArticleDCs().data
    # end = time.time()

    # print(f'arDcs loading : {end - start}')

    # start = time.time()
    # articleKeys = [dc.idNo for dc in arDcs]
    # end = time.time()

    # print(f'articleKeys loading : {end - start}')

    # start = time.time()
    # article_filtered = [dc for dc in dcs if dc.articleNo in articleKeys]

    # end = time.time()

    # print(f'filted loading : {end - start}')


    # start = time.time()
    # article_filtered = [dc for dc in dcs if dc.articleNo == articleKeys[10000]]

    # end = time.time()

    # print(f'filted loading 2 : {end - start}')