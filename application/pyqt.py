import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

sys.path.append('C:/Users/user/PycharmProjects/naverLand')
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
        # self.set_detailGroupBox()
        # self.set_brokerGroupBox()

        self.tabs2 = QTabWidget()
        self.tab3 = QTableWidget()
        self.tab4 = QTableWidget()
        self.tabs2.addTab(self.tab3, 'table4')
        self.tabs2.addTab(self.tab4, 'table5')

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.tabs1)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addSpacing(24)
        self.rightLayout.addWidget(self.mainGroupBox)
        # self.rightLayout.addWidget(self.detailGroupBox)
        # self.rightLayout.addWidget(self.brokerGroupBox)
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

        self.label_data = sqlQuery.label().get_data(where=where)[0]
        self.update_mainGroupBox_label()
        # self.set_detailGroupBox()
        # self.set_brokerGroupBox()

        complexNo = self.tab1_data[row].get('complexNo')
        print('='*100, f'row : {complexNo}', sep='\n')

        where = whereClause.tab4_WhereHandler().get_where_clause(complexNo)

        self.tab4_data = sqlQuery.Tab4_table().get_data(where=where)
        self.set_tab4()


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
        print('='*100, f'label_Data : \n{self.label_data}', sep='\n')

        self.mainGroupBox = QGroupBox('Main Information')
    
    def set_mainGroupBox_layout(self):

        labelVBox = QVBoxLayout()
        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_1)
        labelHBox.addWidget(self.ql_2)
        labelVBox.addLayout(labelHBox)

        self.mainGroupBox.setLayout(labelVBox)

    def set_mainGroupBox_label(self):  

        self.ql_1 = QLabel()
        i = self.label_data.get('articleName')      
        self.ql_1.setText(f'article name : {i}')
        self.ql_1.repaint()

        self.ql_2 = QLabel()
        i = self.label_data.get('aptConstructionCompanyName')
        self.ql_2.setText(f'contruct firm : {i}')
        self.ql_2.repaint()

    def update_mainGroupBox_label(self):  

        i = self.label_data.get('articleName')      
        self.ql_1.setText(f'article name : {i}')
        self.ql_1.repaint()


        i = self.label_data.get('aptConstructionCompanyName')
        self.ql_2.setText(f'contruct firm : {i}')
        self.ql_2.repaint()

    def set_detailGroupBox(self):
        if self.label_data == None:
            label_data = {}
        else : 
            label_data = self.label_data[0]

        self.detailGroupBox = QGroupBox('Detail Information')
        labelVBox = QVBoxLayout()
        
        labelLst = [
                [('expose start date', 'exposeStartYMD'), ('expose end date', 'exposeEndYMD')],
                [('room count', 'roomCount'), ('management cost', 'monthlyManagementCost')],
                [('bathroom count', 'bathroomCount'), ('include item', 'monthlyManagementCostInclusdeItemName')],
                [('direction', 'direction'), ('time to subway', 'walkingTimeToNearSubway')],
                [('description', 'articleFeatureDescription')],
                [('detail description', 'detailDescription')]
                ]

        for row in labelLst:
            labeHBox = QHBoxLayout()
            if len(row)>1:
                for label in row:
                    label = QLabel(f'{label[0]} : {label_data.get(label[1])}')
                    labeHBox.addWidget(label)
            else:
                label = row[0]
                label = QLabel(f'{label[0]} : {label_data.get(label[1])}')
                labeHBox.addWidget(label)
            labelVBox.addLayout(labeHBox)

        self.detailGroupBox.setLayout(labelVBox)


    def set_brokerGroupBox(self):
        if self.label_data == None:
            label_data = {}
        else : 
            label_data = self.label_data[0]

        self.brokerGroupBox = QGroupBox('Broker Information')
        labelVBox = QVBoxLayout()
        
        labelLst = [
                [('broker name', 'realtorName'), ('representative', 'representativeName')],
                [('address', 'address')],
                [('telephon', 'representiveTelNo'), ('cell phone', 'cellPhoneNo')]
                ]

        for row in labelLst:
            labeHBox = QHBoxLayout()
            if len(row)>1:
                for label in row:
                    label = QLabel(f'{label[0]} : {label_data.get(label[1])}')
                    labeHBox.addWidget(label)
            else:
                label = row[0]
                label = QLabel(f'{label[0]} : {label_data.get(label[1])}')
                labeHBox.addWidget(label)
            labelVBox.addLayout(labeHBox)
        
        self.brokerGroupBox.setLayout(labelVBox)

    def set_tab4(self):
        
        cols = ['date', 'real price']
        self.tab4.setColumnCount(len(cols))
        self.tab4.setRowCount(len(self.tab4_data))
        
        self.tab4.setHorizontalHeaderLabels(cols)
        self.tab4.horizontalHeader().setStyleSheet("::section{background-color : #05111b;" "color:white;" "border-style : solid;}")

        # create table data

        self.set_tab4_contents()
    
    def set_tab4_contents(self):
        db_cols = ['date', 'price']
        for row_tuple in enumerate(self.tab4_data) :  # rows
            for col_tuple in enumerate(db_cols) : #cols
                self.tab4.setItem(row_tuple[0], col_tuple[0], QTableWidgetItem(str(row_tuple[1].get(col_tuple[1]))))

        self.tab4.setEditTriggers(QTableWidget.NoEditTriggers)
        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    app.exec()
   