import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

sys.path.append('C:/Users/ajcltm/PycharmProjects/naverLand')
import dataclass
import sqlQuery


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab1_data = sqlQuery.Init_tab1_table().get_data()

        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200, 1000, 700)

        self.tabs1 = QTabWidget()

        self.tab1 = QTableWidget()
        self.tab1.resize(400, 500)
        # self.set_tab1()
        self.tab2 = QTableWidget()
        self.tab2.resize(400, 500)
        self.set_tab2()

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

    def set_tab2(self):
        
        data = self.tab1_data

        cols = ['cityNo', 'city', 'dong', 'complex','articleNo', 'articleName', 'estateType', 'ApproveYmd', 'dealPrice', 'warrantPrice','hhCount','exposeYMD', 'tradeTypeName',]
        self.tab2.setColumnCount(len(cols))
        self.tab2.setRowCount(len(data))
        
        self.tab2.setHorizontalHeaderLabels(cols)
        self.tab2.horizontalHeader().setStyleSheet("::section{background-color : #05111b;" "color:white;" "border-style : solid;}")

        # create line Editers
        for tuple in enumerate(cols): 
            self.tab2.setCellWidget(0, tuple[0], QLineEdit())

        # create table data
        for tuple in enumerate(data) :  # rows
            self.tab2.setItem(tuple[0]+1, 0, QTableWidgetItem(tuple[1].get('cityNo')))
            self.tab2.setItem(tuple[0]+1, 1, QTableWidgetItem(tuple[1].get('city')))
            self.tab2.setItem(tuple[0]+1, 2, QTableWidgetItem(tuple[1].get('dong')))
            self.tab2.setItem(tuple[0]+1, 3, QTableWidgetItem(tuple[1].get('complex')))
            self.tab2.setItem(tuple[0]+1, 4, QTableWidgetItem(tuple[1].get('articelNo')))
            self.tab2.setItem(tuple[0]+1, 5, QTableWidgetItem(tuple[1].get('articleName')))
            self.tab2.setItem(tuple[0]+1, 6, QTableWidgetItem(tuple[1].get('realestateTypeCode')))
            self.tab2.setItem(tuple[0]+1, 7, QTableWidgetItem(tuple[1].get('aptUseApproveYmd')))
            self.tab2.setItem(tuple[0]+1, 8, QTableWidgetItem(tuple[1].get('dealPrice')))
            self.tab2.setItem(tuple[0]+1, 9, QTableWidgetItem(tuple[1].get('warrantPrice')))
            self.tab2.setItem(tuple[0]+1, 10, QTableWidgetItem(tuple[1].get('householdCountByPtp')))
            self.tab2.setItem(tuple[0]+1, 11, QTableWidgetItem(tuple[1].get('exposeStartYMD')))
            self.tab2.setItem(tuple[0]+1, 12, QTableWidgetItem(tuple[1].get('tradeTypeName')))
        
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