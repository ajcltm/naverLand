import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

sys.path.append('C:/Users/ajcltm/PycharmProjects/naverLand')
import dataclass
import sqlQuery
import whereClause


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab1_init_data = sqlQuery.Tab1_table().get_data()
        self.tab1_data = self.tab1_init_data
        self.where = whereClause.tab1_WhereHandler().set_where_dict()
        self.label_data = {}
        self.tab4_data = None

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

        self.set_mainGroupBox()
        self.set_mainGroupBox_label()
        self.set_mainGroupBox_layout()

        self.set_detailGroupBox()
        self.set_detailGroupBox_label()
        self.set_detailGroupBox_layout()

        self.set_brokerGroupBox()
        self.set_brokerGroupBox_label()
        self.set_brokerGroupBox_layout()

        self.tabs2 = QTabWidget()
        self.tab3 = QWidget()
        tab3_layout = QHBoxLayout()
        self.fig = plt.Figure()
        self.tab3_plot = FigureCanvas(self.fig)
        self.tab3_table = QTableWidget()
        tab3_layout.addWidget(self.tab3_plot)
        tab3_layout.addWidget(self.tab3_table)
        self.tab3.setLayout(tab3_layout)


        self.tab4 = QWidget()
        tab4_layout = QHBoxLayout()
        self.tab4.setLayout(tab4_layout)
        
        self.tab4 = QTableWidget()
        self.tabs2.addTab(self.tab3, 'tab3')
        self.tabs2.addTab(self.tab4, 'tab4')

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.tabs1)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addSpacing(24)
        self.rightLayout.addWidget(self.mainGroupBox)
        self.rightLayout.addWidget(self.detailGroupBox)
        self.rightLayout.addWidget(self.brokerGroupBox)
        self.rightLayout.addWidget(self.tabs2)
        
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.leftLayout)
        self.layout.addLayout(self.rightLayout)

        self.setLayout(self.layout)
    

    def set_tab1(self):
        
        cols = ['cityNo', 'city', 'dong', 'complex','articleNo', 'articleName', 'estateType', 'ApproveYmd', 'dealPrice', 'realPrice', 'warrantPrice','hhCount','exposeYMD', 'tradeTypeName']
        self.tab1.setColumnCount(len(cols))
        self.tab1.setRowCount(len(self.tab1_data))
        
        self.tab1.setHorizontalHeaderLabels(cols)
        self.tab1.horizontalHeader().setStyleSheet("::section{background-color : #05111b;" "color:white;" "border-style : solid;}")

        # create table data

        self.set_tab1_contents()

        # create line Editers
    
        self.set_cell_lineEdit()

        self.tab1.clicked.connect(self.tab1Clicked)
    
    def set_tab1_contents(self):
        self.tab1.setRowCount(len(self.tab1_data)+1)
        db_cols = ['cityNo', 'gu', 'dong', 'complex', 'articleNo', 'articleName',
                    'realestateTypeCode', 'aptUseApproveYmd', 'dealPrice', 'price', 
                    'wrrantPrice', 'householdCountByPtp', 'exposeStartYMD',
                    'tradeTypeName']
        for row_tuple in enumerate(self.tab1_data) :  # rows
            for col_tuple in enumerate(db_cols) : #cols
                self.tab1.setItem(row_tuple[0]+1, col_tuple[0], QTableWidgetItem(str(row_tuple[1].get(col_tuple[1]))))

        self.tab1.setEditTriggers(QTableWidget.NoEditTriggers)

    def tab1Clicked(self):

        row = self.tab1.currentIndex().row()-1

        articleNo = self.tab1_data[row].get('articleNo')
        print('='*100, f'row : {articleNo}', sep='\n')

        where = whereClause.label_WhereHandler().get_where_clause(articleNo)

        self.label_data = sqlQuery.Tab1_table().get_data(where=where)[0]
        self.set_mainGroupBox_label(update=True)
        self.set_detailGroupBox_label(update=True)
        self.set_brokerGroupBox_label(update=True)

        complexNo = self.tab1_data[row].get('complexNo')
        print('='*100, f'row : {complexNo}', sep='\n')

        where = whereClause.tab4_WhereHandler().get_where_clause(complexNo)

        self.tab4_data = sqlQuery.Tab4_table().get_data(where=where)
        self.set_tab3_table()


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

        self.realPrice_le = QLineEdit()
        self.tab1.setCellWidget(0, 9, self.realPrice_le)

        self.wrrantPrice_le = QLineEdit()
        self.tab1.setCellWidget(0, 10, self.wrrantPrice_le)

        self.hhCount_le = QLineEdit()
        self.tab1.setCellWidget(0, 11, self.hhCount_le)

        self.exposeStartYMD_le = QLineEdit()
        self.tab1.setCellWidget(0, 12, self.exposeStartYMD_le)

        self.tradeTypeName_le = QLineEdit()
        self.tab1.setCellWidget(0, 13, self.tradeTypeName_le)
    
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


    def set_mainGroupBox(self):

        self.mainGroupBox = QGroupBox('Main Information')

    def set_mainGroupBox_label(self, update=False):  

        if update == False :
            self.ql_articleName = QLabel()
        i = self.label_data.get('articleName')      
        self.ql_articleName.setText(f'article name : {i}')
        self.ql_articleName.repaint()

        if update == False :
            self.ql_aptUseApproveYmd = QLabel()
        i = self.label_data.get('aptUseApproveYmd')
        self.ql_aptUseApproveYmd.setText(f'approve date : {i}')
        self.ql_aptUseApproveYmd.repaint()

        if update == False :
            self.ql_fullAddress = QLabel()
        i = self.label_data.get('fullAddress')
        self.ql_fullAddress.setText(f'address : {i}')
        self.ql_fullAddress.repaint()

        if update == False :
            self.ql_dealPrice = QLabel()
        i = self.label_data.get('dealPrice')
        self.ql_dealPrice.setText(f'deal price : {i}')
        self.ql_dealPrice.repaint()

        if update == False :
            self.ql_price = QLabel()
        i = self.label_data.get('price')
        self.ql_price.setText(f'real price : {i}')
        self.ql_price.repaint()

        if update == False :
            self.ql_allWarrantPrice = QLabel()
        i = self.label_data.get('allWarrantPrice')
        self.ql_allWarrantPrice.setText(f'all warrant price : {i}')
        self.ql_allWarrantPrice.repaint()

        if update == False :
            self.ql_financePrice = QLabel()
        i = self.label_data.get('financePrice')
        self.ql_financePrice.setText(f'finance price : {i}')
        self.ql_financePrice.repaint()

        if update == False :
            self.ql_supplySpace = QLabel()
        i = self.label_data.get('supplySpace')
        self.ql_supplySpace.setText(f'supply space : {i}')
        self.ql_supplySpace.repaint()

        if update == False :
            self.ql_exclusiveSpace = QLabel()
        i = self.label_data.get('exclusiveSpace')
        self.ql_exclusiveSpace.setText(f'exclusive space : {i}')
        self.ql_exclusiveSpace.repaint()

        if update == False :
            self.ql_exclusiveRate = QLabel()
        i = self.label_data.get('exclusiveRate')
        self.ql_exclusiveRate.setText(f'exclusive rate : {i}')
        self.ql_exclusiveRate.repaint()

        if update == False :
            self.ql_walkingTimeToNearSubway = QLabel()
        i = self.label_data.get('walkingTimeToNearSubway')
        self.ql_walkingTimeToNearSubway.setText(f'time to subway : {i}')
        self.ql_walkingTimeToNearSubway.repaint()

        if update == False :
            self.ql_totalDongCount = QLabel()
        i = self.label_data.get('totalDongCount')
        self.ql_totalDongCount.setText(f'dong count : {i}')
        self.ql_totalDongCount.repaint()

        if update == False :
            self.ql_aptHouseholdCount = QLabel()
        i = self.label_data.get('aptHouseholdCount')
        self.ql_aptHouseholdCount.setText(f'house count : {i}')
        self.ql_aptHouseholdCount.repaint()

        if update == False :
            self.ql_floorInfo = QLabel()
        i = self.label_data.get('floorInfo')
        self.ql_floorInfo.setText(f'floor info : {i}')
        self.ql_floorInfo.repaint()

        if update == False :
            self.ql_entranceTypeName = QLabel()
        i = self.label_data.get('entranceTypeName')
        self.ql_entranceTypeName.setText(f'entrance type : {i}')
        self.ql_entranceTypeName.repaint()


    def set_mainGroupBox_layout(self):
        labelVBox = QVBoxLayout()

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_articleName)
        labelHBox.addWidget(self.ql_aptUseApproveYmd)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_fullAddress)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_dealPrice)
        labelHBox.addWidget(self.ql_price)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_allWarrantPrice)
        labelHBox.addWidget(self.ql_financePrice)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_supplySpace)
        labelHBox.addWidget(self.ql_exclusiveSpace)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_exclusiveRate)
        labelHBox.addWidget(self.ql_walkingTimeToNearSubway)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_totalDongCount)
        labelHBox.addWidget(self.ql_aptHouseholdCount)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_floorInfo)
        labelHBox.addWidget(self.ql_entranceTypeName)
        labelVBox.addLayout(labelHBox)

        self.mainGroupBox.setLayout(labelVBox)
    

    def set_detailGroupBox(self):

        self.detailGroupBox = QGroupBox('detail Information')


    def set_detailGroupBox_label(self, update=False):  

        if update == False :
            self.ql_aptConstructionCompanyName = QLabel()
        i = self.label_data.get('aptConstructionCompanyName')
        self.ql_aptConstructionCompanyName.setText(f'construction firm : {i}')
        self.ql_aptConstructionCompanyName.repaint()

        if update == False :
            self.ql_exposeStartYMD = QLabel()
        i = self.label_data.get('exposeStartYMD')      
        self.ql_exposeStartYMD.setText(f'expose start date : {i}')
        self.ql_exposeStartYMD.repaint()

        if update == False :
            self.ql_exposeEndYMD = QLabel()
        i = self.label_data.get('exposeEndYMD')
        self.ql_exposeEndYMD.setText(f'expose end date : {i}')
        self.ql_exposeEndYMD.repaint()

        if update == False :
            self.ql_roomCount = QLabel()
        i = self.label_data.get('roomCount')
        self.ql_roomCount.setText(f'room count : {i}')
        self.ql_roomCount.repaint()

        if update == False :
            self.ql_bathroomCount = QLabel()
        i = self.label_data.get('bathroomCount')
        self.ql_bathroomCount.setText(f'bathroom count : {i}')
        self.ql_bathroomCount.repaint()

        if update == False :
            self.ql_monthlyManagementCost = QLabel()
        i = self.label_data.get('monthlyManagementCost')
        self.ql_monthlyManagementCost.setText(f'management cost : {i}')
        self.ql_monthlyManagementCost.repaint()

        if update == False :
            self.ql_monthlyManagementCostInclusdeItemName = QLabel()
        i = self.label_data.get('monthlyManagementCostInclusdeItemName')
        self.ql_monthlyManagementCostInclusdeItemName.setText(f'include item : {i}')
        self.ql_monthlyManagementCostInclusdeItemName.repaint()

        if update == False :
            self.ql_direction = QLabel()
        i = self.label_data.get('direction')
        self.ql_direction.setText(f'direction : {i}')
        self.ql_direction.repaint()

        if update == False :
            self.ql_articleFeatureDescription = QLabel()
        i = self.label_data.get('articleFeatureDescription')
        self.ql_articleFeatureDescription.setText(f'description : {i}')
        self.ql_articleFeatureDescription.repaint()


    def set_detailGroupBox_layout(self):
        labelVBox = QVBoxLayout()

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_aptConstructionCompanyName)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_exposeStartYMD)
        labelHBox.addWidget(self.ql_exposeEndYMD)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_roomCount)
        labelHBox.addWidget(self.ql_bathroomCount)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_monthlyManagementCost)
        labelHBox.addWidget(self.ql_monthlyManagementCostInclusdeItemName)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_direction)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_articleFeatureDescription)
        labelVBox.addLayout(labelHBox)

        self.detailGroupBox.setLayout(labelVBox)


    def set_brokerGroupBox(self):

        self.brokerGroupBox = QGroupBox('broker Information')


    def set_brokerGroupBox_label(self, update=False):  

        if update == False :
            self.ql_realtorName = QLabel()
        i = self.label_data.get('realtorName')
        self.ql_realtorName.setText(f'broker name : {i}')
        self.ql_realtorName.repaint()

        if update == False :
            self.ql_representativeName = QLabel()
        i = self.label_data.get('representativeName')      
        self.ql_representativeName.setText(f'representative : {i}')
        self.ql_representativeName.repaint()

        if update == False :
            self.ql_address = QLabel()
        i = self.label_data.get('address')
        self.ql_address.setText(f'broker address : {i}')
        self.ql_address.repaint()

        if update == False :
            self.ql_representiveTelNo = QLabel()
        i = self.label_data.get('telephon')
        self.ql_representiveTelNo.setText(f'telephon : {i}')
        self.ql_representiveTelNo.repaint()

        if update == False :
            self.ql_cellPhoneNo = QLabel()
        i = self.label_data.get('cellPhoneNo')
        self.ql_cellPhoneNo.setText(f'cell phone : {i}')
        self.ql_cellPhoneNo.repaint()


    def set_brokerGroupBox_layout(self):
        labelVBox = QVBoxLayout()

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_realtorName)
        labelHBox.addWidget(self.ql_representativeName)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_address)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_representiveTelNo)
        labelHBox.addWidget(self.ql_cellPhoneNo)
        labelVBox.addLayout(labelHBox)

        self.brokerGroupBox.setLayout(labelVBox)


    def set_tab3_table(self):
        
        cols = ['date', 'real price']
        self.tab3_table.setColumnCount(len(cols))
        self.tab3_table.setRowCount(len(self.tab4_data))
        
        self.tab3_table.setHorizontalHeaderLabels(cols)
        self.tab3_table.horizontalHeader().setStyleSheet("::section{background-color : #05111b;" "color:white;" "border-style : solid;}")

        # create table data

        self.set_tab3_table_contents()
    
    def set_tab3_table_contents(self):
        db_cols = ['date', 'price']
        for row_tuple in enumerate(self.tab4_data) :  # rows
            for col_tuple in enumerate(db_cols) : #cols
                self.tab3_table.setItem(row_tuple[0], col_tuple[0], QTableWidgetItem(str(row_tuple[1].get(col_tuple[1]))))

        self.tab3_table.setEditTriggers(QTableWidget.NoEditTriggers)
        

    def set_tab3_plot(self):
        self.tab4_data
        ax = self.fig.add_subplot(111)
        ax.plot(df.index, df['Adj Close'], label='Adj Close')
        ax.plot(df.index, df['MA20'], label='MA20')
        ax.plot(df.index, df['MA60'], label='MA60')
        ax.legend(loc='upper right')
        ax.grid()

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    app.exec()
   